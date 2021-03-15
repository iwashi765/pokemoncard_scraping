import shutil
import tempfile
import urllib.request
import requests,bs4


########################## function  #############################################

#プリズムスターかの判定
def star(obj):
    if obj.select('section h1')[0].select('span') != []:
        return True
    else:
        return False

#特性を持つかの判定
def ability(obj):
    if obj.select('.RightBox .mt20')[0].get_text() == '特性':
        return True
    else:
        return False
    
#GXわざを持つかの判定
def gx(obj,end) :
    if 'GX' in str(obj.select('section h1')[0].get_text()):
        return True
    else:
        return False

#ポケモンの種類、HP、タイプの出力
def output_poke(obj):
    print(obj.select('.RightBox .type')[0].get_text())
    #HP
    print(obj.select('.RightBox .hp-num')[0].get_text())
    #タイプ(クラス名)
    print(obj.select('.RightBox .RightBox-inner div div span')[4].get("class")[0])
    
#特性部分の出力
def output_ability(obj):
    #特性
    print(obj.select('.RightBox .mt20')[0].get_text())
    #特性名
    print(obj.select('.RightBox h4')[0].get_text())
    #特性の効果文
    abilitytext = str(obj.select('.RightBox p')[0])
    list = obj.select('.RightBox p')[0].select('span')
    #効果文にタイプが入っている場合に余計なタグを除去
    num = len(list)
    if num != 0:
        for effectnumber in range(0,num):
            rep = list[effectnumber]
            abilitytext = abilitytext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
    else:
        abilitytext = obj.select('.RightBox p')[0].get_text()
    print(abilitytext)
    #特性の効果文の終わりを挿入
    print('end_ability')

#わざ部分の出力
def output_weapon(obj,begin,end):
    temp_energylist = 0
    start = 0
    gap = 0
    damage = 0
    energylist = 0
    #わざ名を出力    
    print(obj.select('.RightBox .mt20')[begin].get_text())
    for weapon_number in range(begin,end):
        #わざに必要なエネルギーを出力
        #エネルギーの始まりを挿入
        print('begin_energy')
        temp = obj.select('.RightBox h4')[weapon_number].select('.RightBox h4 span')
        energylist = len(temp)
        damage = temp[energylist-1].get_text()
        if temp_energylist != 0:
            start = temp_energylist
            energylist = temp_energylist + energylist
        if damage != '':
            energylist = energylist-1
            gap = 1
        else:
            gap = 0
        for energy_number in range(start,energylist):
            print(obj.select('.RightBox h4 span')[energy_number].get("class")[0])
        temp_energylist = energylist + gap
        #エネルギーの終わりを挿入
        print('end_energy')
        #わざ名とダメージを出力
        print(obj.select('.RightBox h4')[weapon_number].get_text())
        #わざの効果
        #わざの効果のはじまりを出力
        print('begin_weapon')
        weapontext = str(obj.select('.RightBox p')[weapon_number])
        list = obj.select('.RightBox p')[weapon_number].select('span')
        num = len(list)
        if num != 0:
            for effectnumber in range(0,num):
                rep = list[effectnumber]
                weapontext = weapontext.replace(str(rep),str(rep.get('class')[0])).replace('<p>','').replace('</p>','').replace('<br/>','')
        else:
            weapontext = obj.select('.RightBox p')[weapon_number].get_text()
        print(weapontext)
        #わざの効果の終わりを出力
        print('end_weapon')
        
#弱点、抵抗の出力
def output_weak(obj):
    for number in range(0,2):
        print(obj.select('.RightBox table th')[number].get_text())
        if obj.select('.RightBox table td')[number].select('span') == []:
            print('--')
        else:
            print(obj.select('.RightBox table td')[number].select('span')[0].get("class")[0])

#にげるエネルギー
def output_retreet(obj):
    print(obj.select('.RightBox table th')[2].get_text())
    #にげるエネルギーの始まりを挿入
    print('begin_treetenergy')
    if obj.select('.RightBox table td')[2].select('span') == []:
        print('--')
    else:
        list = len(obj.select('.RightBox table td')[2].select('span'))
        for energy_number in range(0,list):
            print(obj.select('.RightBox table td')[2].select('span')[energy_number].get("class")[0])
    #にげるエネルギーの終わりを挿入
    print('end_treetenergy')

#mainから受け取って出力
def pokemon(obj):
    begin = 0
    print('ポケモン')
    #プリズムスターかで分けて名前付け
    if star(obj):
        print(obj.select('section h1')[0].get_text()+'◇')
    else:
        print(obj.select('section h1')[0].get_text())
        #種類~タイプの出力
    output_poke(obj)
    #特性、GX含むわざの数を取得
    a_w_list = len(obj.select('.RightBox h4'))
    end = a_w_list
    #特性をもつ
    if ability(obj):
        output_ability(obj)
        begin = begin + 1
        if begin != end:
            output_weapon(obj,begin,end)
    else:
        #特性を持たない
        output_weapon(obj,begin,end)
        
    #弱点、抵抗
    output_weak(obj)
    output_retreet(obj)

