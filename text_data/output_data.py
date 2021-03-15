import collections
import send_data

#ワザをもつか判定(メタモン◇とかいるし)
def weapon(data):
    for row in range(len(data)):
        if data[row].find('ワザ') != -1:
            return True
       # else:
    return False

#特性をもつか判定
def ability(data):
    length = len(data)
    for row in range(0,length):
        if data[row] == '特性':
            return True
    return False

#特性の効果文を1行にまとめる
def order_ability(data):
    effect = ''
    for row in range (0,len(data)):
        if data[row] == '特性':
            begin_effect = row
        if data[row] == 'end_ability':
            end_effect = row
    for k in range (begin_effect+2,end_effect):
        effect = effect + data[k]
    #ガラル ニャイキングのようなスペースを削除
    effect = effect.replace(' ','')
    return effect

#わざの効果文を1行にまとめる
def order_effect(data):
    effect = ''
    begin_effect = 0
    end_effect = 0
    for row in range (0,len(data)):
        if data[row] == 'begin_effect':
            begin_effect = row
        if data[row] == 'end_effect':
            end_effect = row
    for k in range (begin_effect+1,end_effect):
        effect = effect + data[k]
    #ガラル ニャイキングのようなスペースを削除
    effect = effect.replace(' ','')
    return effect

#にげるエネルギーを1行にまとめる
def order_treet(data):
    energy = ''
    begin_treet = 0
    end_treet = 0
    for row in range (0,len(data)):
        if data[row] == 'begin_treetenergy':
            begin_treet = row
        if data[row] == 'end_treetenergy':
            end_treet = row
    for k in range (begin_treet+1,end_treet):
        energy = energy + data[k]
    return energy

############################# カードの種類毎の出力 ######################################

def pokemon_output(data,pack):
    #出力用のOrderedDictを定義
    #
    
    output_data = collections.OrderedDict()
    output_data['kind'] = data[0]
    output_data['name'] = data[1]
    #1 進化のスペースを削除
    data[2] = data[2].replace(' ','')
    output_data['evolution'] = data[2]
    output_data['hp'] = int(data[3])
    output_data['type'] = data[4]
    #GXポケモンかどうかのフラグ
    if data[1].find('GX') != -1:
        output_data['GX'] = True
    else:
        output_data['GX'] = False
    #Vポケモンかどうかのフラグ
    if data[1].find('V') != -1:
        output_data['V'] = True
    else:
        output_data['V'] = False
    #TAGかどうかのフラグ
    if data[1].find('&') != -1:
        output_data['TAG'] = True
    else:
        output_data['TAG'] = False
    weapon_number = 0
    #ワザをもつかで場合分け
    if weapon(data):
        weapon_number = data.count('begin_energy')
        begin_weapon = [0]*weapon_number
        end_weapon = [0]*weapon_number
        begin_number = 0
        end_number = 0
        #エネルギーの始まりの行と終わりの行をわざの数だけ取得
        for row in range(0,len(data)):
            if data[row] == 'begin_energy':
                begin_weapon[begin_number] = row
                begin_number = begin_number + 1
            if data[row] == 'end_energy':
                end_weapon[end_number] = row
                end_number = end_number + 1

        energy = ['']*weapon_number
        for num in range(weapon_number):
            for k in range (begin_weapon[num]+1,end_weapon[num]):
                energy[num] = energy[num] + data[k]
        
        #効果文の数を取得
        effect_number = data.count('begin_weapon')
        begin_effect = 0
        end_effect = 0
        begin_ef_position = [0]*effect_number
        end_ef_position = [0]*effect_number
        #効果文の開始位置と終了位置を取得
        for row in range(0,len(data)):
            if data[row] == 'begin_weapon':
                begin_ef_position[begin_effect] = row
                begin_effect = begin_effect + 1
            if data[row] == 'end_weapon':
                end_ef_position[end_effect] = row
                end_effect = end_effect+1
        #各begin_energyとend_energyの間を1つの要素(effect)に格納
        effect = ['']*effect_number
        for num in range(effect_number):
            for k in range (begin_ef_position[num]+1,end_ef_position[num]):
                effect[num] = effect[num] + data[k]
            if effect[num] == '':
                effect[num] = '--'
#        temp_name = ['']*weapon_number
        #わざの名前とダメージを分けて出力
        weapon_name = ['']*weapon_number
        weapon_damage = ['']*weapon_number
#        s_weapons = ['']*2
        for row in range (weapon_number):
            weapon_name[row] = data[end_weapon[row]+1]
            weapon_damage[row] = data[end_weapon[row]+2].replace('＋','').replace('ー','').replace('−','').replace('―','').replace('－','').replace('×','')

    output_data['ability'] = False
    #特性を保つ場合は名前と効果文を追加
    if ability(data):
        output_data['ability'] = True
        output_data['ability_name'] = data[6]
        output_data['ability_effect'] = data[7]
    #わざの数によってkeyを増やして追加
    if weapon_number == 1:
        output_data['weapon_energy'] = energy[0]
        output_data['weapon_name'] = weapon_name[0]
        output_data['weapon_damage'] = int(weapon_damage[0])
        output_data['weapon_effect'] = effect[0]
    if weapon_number == 2:
        output_data['weapon_energy'] = energy[0]
        output_data['weapon_name'] = weapon_name[0]
        output_data['weapon_damage'] = int(weapon_damage[0])
        output_data['weapon_effect'] = effect[0]
        output_data['weapon2_energy'] = energy[1]
        output_data['weapon2_name'] = weapon_name[1]
        output_data['weapon2_damage'] = int(weapon_damage[1])
        output_data['weapon2_effect'] = effect[1]
    if weapon_number == 3:
        output_data['weapon_energy'] = energy[0]
        output_data['weapon_name'] = weapon_name[0]
        output_data['weapon_damage'] = int(weapon_damage[0])
        output_data['weapon_effect'] = effect[0]
        output_data['weapon2_energy'] = energy[1]
        output_data['weapon2_name'] = weapon_name[1]
        output_data['weapon2_damage'] = int(weapon_damage[1])
        output_data['weapon2_effect'] = effect[1]
        output_data['weapon3_energy'] = energy[2]
        output_data['weapon3_name'] = weapon_name[2]
        output_data['weapon3_damage'] = int(weapon_damage[2])
        output_data['weapon3_effect'] = effect[2]

    for row in range(len(data)):
        if data[row] == '弱点':
            output_data['weak'] = data[row+1]
        if data[row] == '抵抗力':
            output_data['resist'] = data[row+1]
        if data[row].find('--') != 1:
            output_data['retreat'] = order_treet(data)
    
    output_data['id'] = int(data[len(data)-2])
    output_data['pack'] = data[len(data)-1]
    send_data.pokemon_db(output_data,pack)

def traner_output(data,pack):
    output_data = collections.OrderedDict()
    output_data['kind'] = data[0]
    output_data['name'] = data[1]
    output_data['effect'] = order_effect(data)
    output_data['id'] = int(data[len(data)-2])
    output_data['pack'] = data[len(data)-1]
    send_data.traners_db(output_data,pack)

def energy_output(data,pack):
    output_data = collections.OrderedDict()
    output_data['kind'] = data[0]
    output_data['name'] = data[1]
#    effect = data[2]
#    if data[2] != data[len(data)-3]:
#        effect = str(data[2]) + str(data[len(data)-3])
#    output_data['effect'] = effect
    output_data['effect'] = order_effect(data)
    output_data['id'] = int(data[len(data)-2])
    output_data['pack'] = data[len(data)-1]
    send_data.special_energy_db(output_data,pack)


def basic_energy_output(data,pack):
    output_data = collections.OrderedDict()
    output_data['kind'] = data[0]
    output_data['name'] = data[1]
    output_data['id'] = int(data[len(data)-2])
    output_data['pack'] = data[len(data)-1]
    send_data.basic_energy_db(output_data,pack)

