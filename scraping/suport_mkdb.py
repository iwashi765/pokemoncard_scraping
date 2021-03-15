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

def star(obj):
    if obj.select('section h1')[0].select('span') != []:
        return True
    else:
        return False

def suport(obj):
    #種類,プリズムスターだと2要素あるので条件分け
    #説明文の行数を取得
    list = len(obj.select('.RightBox p'))
    #サポートだということを出力
    print(obj.select('.RightBox .mt20')[0].get_text())
    if star(obj):
        print(obj.select('section h1')[0].get_text()+'◇')
        list = list -1
    else:
        print(obj.select('section h1')[0].get_text())

    #行数分だけ繰り返し(サポートの基本ルールはカット)
    #効果文の始めを挿入
    print('begin_effect')
    for effect in range(0,list-1):
        #print(obj.select('.RightBox p')[effect].get_text())
        effecttext = str(obj.select('.RightBox p')[effect])
        list = obj.select('.RightBox p')[effect].select('span')
        #print(effecttext)
        num = len(list)
        if num != 0:
            for effectnumber in range(0,num):
                rep = list[effectnumber]
                effecttext = effecttext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
        else:
            effecttext = obj.select('.RightBox p')[effect].get_text()
        print(effecttext)
    #効果文の終わりを挿入
    print('end_effect')
