# Bilibili Bangumi Downloader

[中文版本](https://github.com/yaoxi-std/bilibili-bangumi-downloader/blob/main/readme.zh.md)

This is a python3 script which allows you to download a series of bangumi.

## How to use?

The video url can be **either** Bangumi URL **or** Video URL. For example:
- `https://www.bilibili.com/bangumi/media/md191`
- `https://www.bilibili.com/bangumi/play/ep95847?from_spmid=666.19.0.0`

## Example (from source)

First, make sure that `python3`, `axel` and `ffmpeg` runs correctly.

Take out your cookie from bilibili.com and paste it into `cookie.txt`.

Then, run `main.py` (you may need to open it with python on Windows). Input video URL and download directory, and it will start downloading automatically. You can choose whether to keep the `.flv` and `.ogg` files after the `.mp4` files are generated.

```sh
$ /usr/bin/python3 "/Users/yaoxi-std/Documents/project/bilibili-bangumi-downloader/main.py"
Video URL: https://www.bilibili.com/bangumi/media/md191
Download to: ~/Downloads/is_the_order_a_rabbit
Clean .flv/.ogg in download directory? [Y/n] (default n): Y
...
```

## Example (from binary)

Download the binary files from [release page](https://github.com/yaoxi-std/bilibili-bangumi-downloader/releases), then open `bbdown` directly.

```sh
$ ./bbdown
Video URL: https://www.bilibili.com/bangumi/media/md191
Download to: ~/Downloads/is_the_order_a_rabbit
Clean .flv/.ogg in download directory? [Y/n] (default n): Y
...
```

## Results

![result](img/result.png)
