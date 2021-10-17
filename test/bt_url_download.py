#!/usr/bin/env python2
# coding: utf-8
# @desc python通过BT种子生成磁力链接
# @author pythontab.com
# 20180622:修复解析部份torrent文件出错的问题,举个栗子:
#	http://www.btbtt.me/attach-download-fid-950-aid-4411663.htm
import bencode
import sys
import hashlib
import base64
import urllib
import appex,clipboard,webbrowser,console,os,shutil
from zipfile import ZipFile

def convertBt2URL(torrentPath):
    #读取种子文件
    torrent = open('http://releases.ubuntu.com/12.04/ubuntu-12.04.1-desktop-i386.iso.torrent', 'rd').read()
    #计算meta数据
    #metadata = bencode.bdecode(torrent)
    flag=2
    while flag:
        try:
            metadata = bencode.bdecode(torrent)
            break
        except bencode.BTL.BTFailure,e:
            if flag==1:
               raise e
            print '出错了,尝试进行修复...'
            torrent=torrent[:-1]
            flag-=1
    hashcontents = bencode.bencode(metadata['info'])
    digest = hashlib.sha1(hashcontents).digest()
    b32hash = base64.b32encode(digest)
    url = 'magnet:?xt=urn:btih:' + b32hash
    #打印
    print url
    return url

def convertFinish(url):
    clipboard.set(url)
    console.hud_alert('已经复制到剪贴板！')
    webbrowser.open('wb1307639798://')
    appex.finish()

# 解压缩文件到指定目录,目录不存在则创建
def unzip(src, path):
    if not os.path.exists(path):
        os.makedirs(path)

    zip_obj = ZipFile(src, mode='r')
    for info in zip_obj.filelist:
        zip_obj.extract(member=info, path=path)
    zip_obj.close()

def file_name_list(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.torrent':
                L.append(os.path.join(root, file))
    return L

def main():
    console.clear()
    if appex.is_running_extension():
        file_path = appex.get_file_path()
        file_name = os.path.basename(file_path)
        file_ext = os.path.splitext(file_name)[-1]
        if file_path:
            print(file_path)
            if file_ext == '.torrent':
                url = convertBt2URL(file_path)
                convertFinish(url)
            elif file_ext == '.zip':
                dest_path = os.path.expanduser('~/Documents')
                dest_path = os.path.join(dest_path, 'bt2url' + os.path.splitext(file_name)[0])
                unzip(file_path, dest_path)
                name_list = file_name_list(dest_path)
                if len(name_list) == 0:
                    console.hud_alert('别瞎搞！压根没有种子', 'error', 1)
                else:
                    url = ''
                    i = 0
                    for name in name_list:
                        url = url + convertBt2URL(name)
                        if i != len(name_list)-1:
                            url = url + '\r\n'
                        i = i+1
                    if os.path.exists(dest_path):
                        shutil.rmtree(dest_path)
                    convertFinish(url)
            else:
                console.hud_alert('别瞎搞！这不是种子', 'error', 1)
    else:
        console.hud_alert('别瞎搞！在分享扩展中打运行该脚本', 'error', 1)

if __name__ == '__main__':
    main()
