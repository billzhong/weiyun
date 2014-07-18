WeiYun Downloader
=================

This script will fetch WeiYun's real URL and call `wget` to download.

GetIt
-----

###You need [python](http://www.python.org) to run this script.

```bash
wget https://raw.github.com/billzhong/weiyun/master/weiyun.py
```

Usage
-----
```
weiyun.py [-h] [--resume] url
```

For example, the url is `http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c`:

```bash
python weiyun.py http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c
```

### --resume

Resume getting a partially-downloaded file.

For example:

```bash
python weiyun.py http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c --resume
```

Note
----
Only tested in `python 2.7.5` and `wget 1.15`.

Only supported single share file without password.



中文
====

本脚本用来获取微云网盘的真实下载地址，并调用 `wget` 来下载。

获取
----

需要 [Python](http://www.python.org) 环境。

```bash
wget https://raw.github.com/billzhong/weiyun/master/weiyun.py
```

用法
----

```
weiyun.py [-h] [--resume] url
```

例如，地址是 `http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c` ：

```bash
python weiyun.py http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c
```

### --resume

继续下载之前未下载完的文件。

例如：

```bash
python weiyun.py http://share.weiyun.com/01118854b800d71077ffd4f37df15a2c --resume
```

备注
----
仅在 `python 2.7.5` 和 `wget 1.15` 下测试。

只支持无密码的单个分享文件。