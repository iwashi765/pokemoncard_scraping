#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:13:03 2020

@author: ex-pc
"""
import shutil
import tempfile
import urllib.request
import requests,bs4

def goods(obj):
    #種類
    print(obj.select('.RightBox .mt20')[0].get_text())
    #グッズ名
    print(obj.select('section h1')[0].get_text())
    #説明文の行数
    list = len(obj.select('.RightBox p'))
    #行数分だけ繰り返し(グッズの基本ルールはカット)
    #効果文の範囲が複数行の場合があるため文の開始を挿入
    print('begin_effect')
    for effect in range(0,list-1):
        effecttext = str(obj.select('.RightBox p')[effect])
        list = obj.select('.RightBox p')[effect].select('span')
        #文中のタイプの取得で余分に入るタグを除去
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

