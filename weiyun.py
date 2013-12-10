#!/usr/bin/env python

import argparse
import urllib2
import re
import json
import distutils.spawn
import subprocess


# call wget to download
def wget_download(download_url, file_name, cookie_name, cookie_value, resume=False):
    wget_cmd = ['wget',
                '--header=Cookie: ' + cookie_name + '=' + cookie_value,
                '--referer=' + args.url, download_url, '-O', file_name]
    if resume:
        wget_cmd.append('-c')
    assert distutils.spawn.find_executable(wget_cmd[0]), "Cannot find %s" % wget_cmd[0]
    exit_code = subprocess.call(wget_cmd)
    if exit_code != 0:
        raise Exception('Cannot call wget to download.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WeiYun Downloader')
    parser.add_argument('url', help='WeiYun Share URL')
    parser.add_argument('--resume', help='Resume getting a partially-downloaded file.', action='store_true')
    args = parser.parse_args()

    # check the url contain weiyun.com
    if args.url.find('weiyun.com') == -1:
        raise Exception('URL must contain weiyun.com.')

    # use urllib2 to get html data
    try:
        request = urllib2.Request(args.url)
        request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) \
                            AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10B329 Safari/8536.25')
        html = urllib2.urlopen(request).read()
    except:
        raise Exception('Please check the URL.')

    # check the html data contain <head> keyword
    if html.find('<head>') == -1:
        raise Exception('Cannot get correct html page.')

    # use regexp to search the link data
    try:
        m = re.search('shareInfo = {(.*?)};', html)
        data = '{' + m.group(1) + '}'
        result = json.loads(data)
    except:
        raise Exception('Cannot get the link data.')

    # construct url
    url = 'http://' + result['dl_svr_host'] + ':' + str(result['dl_svr_port']) + '/ftn_handler/' \
        + result['dl_encrypt_url'] + '/?fname=' + result['filename']
    fn = result['filename']
    cn = result['dl_cookie_name']
    cv = result['dl_cookie_value']

    # download file
    if args.resume:
        wget_download(url, fn, cn, cv, True)
    else:
        wget_download(url, fn, cn, cv)