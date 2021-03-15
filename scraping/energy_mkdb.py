#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:19:06 2020

@author: ex-pc
"""

import shutil
import tempfile
import urllib.request
import requests,bs4
#import mkdb

#プリズムスターのカードかどうかを判定する関数
def star(obj):
    #プリズムスターだとこのタグで要素が取得できる
    if obj.select('section h1')[0].select('span') != []:
        return True
    else:
        return False

def energy(obj):
    #エネルギーの種類を出力
    print(obj.select('.RightBox .mt20')[0].get_text())
    #説明文の行数を取得
    list = len(obj.select('.RightBox p'))
    if star(obj):   
        #エネルギー名
        print(obj.select('section h1')[0].get_text()+'◇')
        #プリズムスターの場合行数がずれるので調整
        list = list - 1
    else:
        print(obj.select('section h1')[0].get_text())
    #説明文の行数
    print('begin_effect')
    #行数分だけ繰り返し出力を繰り返し
    for i in range(0,list):
        energytext = str(obj.select('.RightBox p')[i])
        list = obj.select('.RightBox p')[i].select('span')
        
        num = len(list)
        #文中にタイプが入るときは、一緒に取得してしまう余計なタグを除去して文字列として連結して出力する
        if num != 0:
            for effectnumber in range(0,num):
                rep = list[effectnumber]
                energytext = energytext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
        else:
            energytext = obj.select('.RightBox p')[i].get_text()
        print(energytext)
    print('end_effect')