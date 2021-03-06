import os
import re
import sys
import json
import requests
from vamerger import VAMerger
from downloader import Downloader


def convert_cookie_to_dict(cookie):
    cookies = dict([x.split("=", 1) for x in cookie.split("; ")])
    return cookies


def check_result_code(result):
    if result["code"] != 0:
        print(result)
        sys.exit(256)


def get_bangumi_info(media_id):
    params = {"media_id": media_id}
    response = requests.get(
        "http://api.bilibili.com/pgc/review/user", params=params)
    result = json.loads(response.content)
    check_result_code(result)
    return result["result"]["media"]


def get_detailed_bangumi_info_from_season_id(season_id):
    params = {"season_id": season_id}
    response = requests.get(
        "http://api.bilibili.com/pgc/view/web/season", params=params)
    result = json.loads(response.content)
    check_result_code(result)
    return result["result"]


def get_detailed_bangumi_info_from_ep_id(ep_id):
    params = {"ep_id": ep_id}
    response = requests.get(
        "http://api.bilibili.com/pgc/view/web/season", params=params)
    result = json.loads(response.content)
    check_result_code(result)
    return result["result"]


def get_last_token_in_url(url):
    pos_slash = url.rfind('/')
    pos_question = url.rfind('?')
    if pos_question == -1:
        pos_question = len(url)
    return url[pos_slash:pos_question]


def get_numbers_in_str(string):
    result = ''
    for ch in string:
        if ord(ch) >= 48 and ord(ch) <= 57:
            result += ch
    return result


def get_detailed_info_from_url(url):
    url = url.rstrip('/')
    if re.fullmatch('.*://www.bilibili.com/bangumi/media/.*', url):
        media_id = get_numbers_in_str(get_last_token_in_url(url))
        season_id = get_bangumi_info(media_id)["season_id"]
        print('media_id = {}'.format(media_id))
        return get_detailed_bangumi_info_from_season_id(season_id)
    else:
        ep_id = get_numbers_in_str(get_last_token_in_url(url))
        print('ep_id = {}'.format(ep_id))
        return get_detailed_bangumi_info_from_ep_id(ep_id)


def get_bangumi_download_info(cookie, aid, cid):
    header = {"referer": "http://www.bilibili.com"}
    params = {"aid": aid, "cid": cid, "qn": 112, "fnval": 0b111111010000}
    response = requests.get(
        "http://api.bilibili.com/pgc/player/web/playurl", headers=header, params=params, cookies=cookie)
    result = json.loads(response.content)
    check_result_code(result)
    return result["result"]


def get_bangumi_downloads(cookie, aid, cid):
    downinfo = get_bangumi_download_info(cookie, aid, cid)["dash"]
    audios = downinfo["audio"]
    videos = downinfo["video"]
    return ([audios[0]["base_url"]], [videos[0]["base_url"]])


def download_bangumi(url, dest, num=64, refurl=""):
    header = {'referer': refurl,
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'}
    if not Downloader(url, num, dest, header=header).run():
        print('\x1b[031mDownload failed: {} -> {}\x1b[0m'.format(url, dest))


def download_all_from_info(cookie, info, destdir, doclean=False):
    counta = 0
    countv = 0
    episodes = info["episodes"]
    for ep in episodes:
        aid = ep["aid"]
        cid = ep["cid"]
        refurl = ep["share_url"]
        print('aid={}, cid={}'.format(aid, cid))
        aurls, vurls = get_bangumi_downloads(cookie, aid, cid)
        assert(len(aurls) == len(vurls))
        for url in aurls:
            counta += 1
            download_bangumi(url, os.path.join(
                destdir, str(counta) + ".ogg"), refurl=refurl)
        for url in vurls:
            countv += 1
            download_bangumi(url, os.path.join(
                destdir, str(countv) + ".flv"), refurl=refurl)
    for i in range(1, counta + 1):
        apath = os.path.join(destdir, str(i) + ".ogg")
        vpath = os.path.join(destdir, str(i) + ".flv")
        opath = os.path.join(destdir, str(i) + ".mp4")
        VAMerger(apath, vpath, opath).run()
        if doclean:
            os.remove(apath)
            os.remove(vpath)
