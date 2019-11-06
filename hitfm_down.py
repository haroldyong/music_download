#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# @author:feiyang
# @date:2019-11-06
#
import urllib
import requests
import json
import sys
import os


# begin function 
def download_hitfm_music( music_type ,page_index):
   # 消息头数据
    headers = {
                'Connection': 'keep-alive',
                'Content-Length': '123',
                'Cache-Control': 'max-age=0',
                'Origin':'https://passport.csdn.net',
                'Upgrade-Insecure-Requests':'1',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Referer': 'http://www.hitfm.cn/category/live',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cookie': 'JSESSIONID=8511501B56A8AB66F0FE45BCCA3F26F7',
     
                }

    #目标url
    url = 'http://www.hitfm.cn/hitlhsrv/srv/top20/songList'

    #参数

    payload = 'type='+str(music_type)+ '&pageIndex='+str(page_index)


    response = requests.post(url, data=payload, headers=headers,verify=False)

    # 返回响应头

    if 200 != response.status_code :
        print 'resonse error!'
        return
     

    # 返回内容
    j= response.json()
    #print j
    if j['con'] is None :
        #print 'resonse empty!'
        return
    for item in j['con'] :
        song_name = item['ssong']
        download_url = item['songurl']
        song_name = song_name.replace("/","_")
        new_name = '/Users/harold/Downloads/hitfm/mp3/'+song_name.replace(" ","_")+'.mp3'

        #print new_name   
        #print download_url
        if os.path.exists(new_name):
            break
        else :    
            urllib.urlretrieve(download_url, new_name)


#end function download_hitfm_music






#调用
music_type=0
while music_type<10 :
    page_index=0
    while page_index<100 :
        download_hitfm_music(music_type,page_index)
        #print str(music_type)+'--'+ str(page_index) 
        page_index+=1
    music_type+=1

print 'success plz check mp3 files!'
sys.exit()


