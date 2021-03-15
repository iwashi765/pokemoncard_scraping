import sys
import requests
import re
import uuid
import pokemon_mkdb
import goods_mkdb
import suport_mkdb
import energy_mkdb
import stadium_mkdb

from bs4 import BeautifulSoup

#パック名はPROMOで固定し、IDを手打ちで入力する

pack = "PROMO"

#追加する分を入力
#s_promo_list = {38886,39211,39212,39246}

s_promo_list = [39246,39212,39211,38886,38616,38615,38612,38609,38496,38495,38255,38254,38249,38001,37998,37993,37796,37793,37775,37774,37773,37772,37609,37608,37603]
sm_promo_list = [37441,37194,37186,37185,37183,37182,37180,37179,37064,36995,36987,36898,36897,36895,36643,36429,36428,36216,36145,36144,36140]

#smとsでプロモが分かれているので合体

promo_list = sm_promo_list + s_promo_list

#f_min = 37742
#f_max = 37750
#pack = 'basic_energy'

#画像取得用の関数
def get_picture(imgs):
    #imgs = bs4obj.select('img')[2].get('src')
    image_url = "https://www.pokemon-card.com/"+ imgs
    req = requests.get(image_url)
    path = "../picture_data/" + str(pack)+"/"+str(url_number) + ".jpg"
    with open(path,'wb') as file:
        file.write(req.content)

#カード詳細ページのURLからスクレイピングを行う
#for url_number in range(f_min,f_max+1):
for url_number in promo_list:
    url = "https://www.pokemon-card.com/card-search/details.php/card/"+str(url_number)+"/regu/XY"
    get_url_info = requests.get(url)
    bs4obj = BeautifulSoup(get_url_info.text, 'lxml')
    if bs4obj.select('.RightBox .mt20')[0].get_text() != '':
            #ポケモン、グッズ、ポケモンのどうぐ、サポート、スタジアム、基本エネルギー、特殊エネルギーで処理ファイル分け
            #ポケモンの場合はポケモン名が入っているので、elseでポケモンだと判断する
            if bs4obj.select('.RightBox .mt20')[0].get_text() == 'グッズ':    
                goods_mkdb.goods(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'ポケモンのどうぐ':
                goods_mkdb.goods(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'サポート':
                suport_mkdb.suport(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'スタジアム':
                stadium_mkdb.stadium(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == '基本エネルギー':
                energy_mkdb.energy(bs4obj)
            elif bs4obj.select('.RightBox .mt20')[0].get_text() == '特殊エネルギー':
                energy_mkdb.energy(bs4obj)
            #なぞの化石がトレーナーズ表記になってるのでバグ回避
#            elif bs4obj.select('.RightBox .mt20')[0].get_text() == 'トレーナーズ':
#                no_use = ''
            else:
                pokemon_mkdb.pokemon(bs4obj)
            #カードのIDを出力
            print(url_number)
            #カードのパック名を出力
            print(pack)
            #後でカード毎に分けるために/を出力
            print('/')
            # 2021/3/12 時点でwebサイトに合わせて仕様変更
            imgs = bs4obj.select('img')[1].get('src')
#            imgs = bs4obj.select('img')[2].get('src')
            get_picture(imgs)


#def get_picture(imgs):
    #imgs = bs4obj.select('img')[2].get('src')
#    image_url = "https://www.pokemon-card.com/"+ imgs
#    req = requests.get(image_url)
#    path = "../picture_data/" + str(pack)+"/"+str(url_number) + ".jpg"
#    with open(path,'wb') as file:
#        file.write(req.content)
