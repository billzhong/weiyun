#!/usr/bin/env python

import argparse
import urllib2
import re
import json
import distutils.spawn
import subprocess


# call wget to download
def wget_download(download_url, file_name, cookie, referer, resume=False):
    wget_cmd = ['wget',
                '--header=Cookie: dlskey=' + cookie,
                '--referer=' + referer, download_url, '-O', file_name]
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

    # use urllib2 to get html data
    try:
        request = urllib2.Request(args.url)
        request.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0 like Mac OS X) '
                                         'AppleWebKit/537.51.1 (KHTML, like Gecko) '
                                         'Version/7.0 Mobile/11A465 Safari/9537.53')
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

    sharekey = result['share_key']
    dlskey = result['dlskey']
    pdir = result['pdir_key']

    fid = result['file_list'][0]['file_id']
    fn = result['file_list'][0]['file_name']

    refer = 'http://share.weiyun.com/' + sharekey

    # construct url
    url = 'http://web.cgi.weiyun.com/share_dl.fcg?browser=mozilla&os_info=windows' \
          '&fid=' + fid + \
          '&pdir=' + pdir + \
          '&sharekey=' + sharekey

    # download file
    if args.resume:
        wget_download(url, fn, dlskey, refer, True)
    else:
        wget_download(url, fn, dlskey, refer)
