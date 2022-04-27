#!/usr/bin/python3

import os
import videostream as vs

if __name__ == '__main__':
    # Cookie
    cookie = ""
    try:
        with open("cookie.txt", "r") as f:
            cookie = f.read()
    except FileNotFoundError:
        print("cookie.txt not found. Paste your cookie in cookie.txt")
        exit(256)
    cookie = vs.convert_cookie_to_dict(cookie)

    # Input
    video_url = input('Video URL: ')
    record_url = input('Download to: ')
    record_url = os.path.abspath(os.path.expanduser(record_url))
    doclean = input(
        'Clean .flv/.ogg in download directory? [Y/n] (default n): ')

    print('Download from {} to {}'.format(video_url, record_url))

    # Download
    info = vs.get_detailed_info_from_url(video_url)
    vs.download_all_from_info(cookie, info, record_url, doclean == "Y")
