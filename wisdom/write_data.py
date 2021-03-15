import collections
import sys
import codecs

new_rule_list = {'s1H','s1W','s1a','s2','s2a','s3','sA','sC','sD','s3a','s4','s4a','sp2'}

#順序付き辞書型になっているが順番は関係ない
pack_list = collections.OrderedDict()

pack_list['s1W']='S[ソード]'
pack_list['s1H']='S[シールド]'
pack_list['s1a']='S[VMAXライジング]'
pack_list['s2']='S[反逆クラッシュ]'
pack_list['s2a']='S[爆炎ウォーカー]'
pack_list['s3']='S[ムゲンゾーン]'
pack_list['s3a']='S[伝説の鼓動]'
pack_list['s4']='S[仰天のボルテッカー]'
pack_list['sA']='S[スターターセット(5種)]'
pack_list['sC']='S[スターターリザードン・オーロンゲ]'
pack_list['sD']='S[Vスターターセット]'
#pack_list['sm5+']='SM「ウルトラフォース」'
#pack_list['sm5M']='SM「ウルトラムーン」'
#pack_list['sm5S']='SM「ウルトラサン」'
#pack_list['sm6']='SM「禁断の光」'
#pack_list['sm6a']='SM「ドラゴンストーム」'
#pack_list['sm6b']='SM「チャンピオンロード」'
#pack_list['sm7']='SM「裂空のカリスマ」'
#pack_list['sm7a']='SM「迅雷スパーク」'
#pack_list['sm7b']='SM「フェアリーライズ」'
#pack_list['sm8']='SM「超爆インパクト」'
#pack_list['sm8a']='SM「ダークオーダー」'
#pack_list['sm8b']='SM「GXウルトラシャイニー」'
pack_list['sm9']='SM「タッグボルト」'
pack_list['sm9a']='SM「ナイトユニゾン」'
pack_list['sm9b']='SM「フルメタルウォール」'
pack_list['sm10']='SM「ダブルブレイズ」'
pack_list['sm10a']='SM[ジージーエンド]'
pack_list['sm10b']='SM[スカイレジェンド]'
pack_list['sm11']='SM[ミラクルツイン]'
pack_list['sm11a']='SM[リミックスバウト]'
pack_list['sm11b']='SM[ドリームリーグ]'
pack_list['sm12']='SM[オルタージェネシス]'
pack_list['sm12a']='SM[タッグオールスターズ]'
#pack_list['SME']='SM「スターターセット伝説」'
#pack_list['smI']='SM[ブイズスターター]'
pack_list['smK']='SM「トレーナーバトルデッキ」'
pack_list['smM']='SM[エフィデオスターター]'
pack_list['smP2']='SM[名探偵ピカチュウ]'
pack_list['sp1']='S[ザシアン+ザマゼンタBOX]'
pack_list['sp2']='S[VMAXスペシャルセット]'
pack_list['s4a']='S[シャイニースターV]'
pack_list['sC2']='S[VMAX初代御三家スターターセット]'
pack_list['s5I']='S[一撃マスター]'
pack_list['s5R']='S[連撃マスター]'
pack_list['sF']='S[プレミアムトレーナーBOX ICHIGEKI,RENGEKI]'
pack_list['s5a']='S[双璧のファイター]'
pack_list['PROMO']='プロモ'

#9902からwisdom内のidが始まる
wisdom_id = 9902

def pokemon(data,weapon_number,pack):
  global wisdom_id
  resist_text = '-20'
  text_tag = ''
  text_ability = ''
  text_weapon1 = ''
  text_weapon2 = ''
  text_weapon3 = ''
  resist_text = ''

  #ソードシールドから-30になったので条件で置き換え
  for pack in new_rule_list:
    if (data['resist'] != '--'):
        resist_text = data['resist'] + '-20'
        if (data['pack'] == pack) :
          resist_text = data['resist'] + '-30'
  
  for pack_name in list(pack_list.keys()):
    if(data['pack'] == pack_name):
      data['pack_name'] = pack_list[str(pack_name)]

  #にげるのに必要なエネルギーを数字に置き換え
  if (data['retreat'] == '--'):
    data['retreat'] = 0
  if (data['retreat'] == '無'):
    data['retreat'] = 1
  elif (data['retreat'] == '無無'):
    data['retreat'] = 2
  elif (data['retreat'] == '無無無'):
    data['retreat'] = 3
  elif (data['retreat'] == '無無無無'):
    data['retreat'] = 4

    
  text_head = str(wisdom_id) + ',' + data['name'] + ',' + data['type'] + ',' + data['evolution'] + 'ポケモン,' + str(data['hp']) + ',' + data['weak'] + '×2,' +  resist_text + ',' + str(data['retreat']) + ',' + 'U,' + data['pack_name'] + ',' + data['pack'] + ','

  if(data['TAG'] == 'True'):
    text_tag = ',【タッグチーム】,'

  if (data['ability'] == 'True'):
    text_ability = '【特性】' + data['ability_name'] + ',,' + data['ability_effect'] +','

  if (weapon_number >= 1):
    text_weapon1 = data['weapon_name'] + ',' + data['weapon_energy'] + ' ' + str(data['weapon_damage']) + ',' + data['weapon_effect'] + ','

  if (weapon_number >= 2):
    text_weapon2 = data['weapon2_name'] + ',' + data['weapon2_energy'] + ' ' + str(data['weapon2_damage']) + ',' + data['weapon2_effect'] + ','

  if (weapon_number == 3):
    text_weapon3 = data['weapon3_name'] + ',' + data['weapon3_energy'] + ' ' + str(data['weapon3_damage']) + ',' + data['weapon3_effect'] + ','

  sum_text = text_head +text_tag + text_ability + text_weapon1 + text_weapon2 + text_weapon3

  print(sum_text)
  wisdom_id = wisdom_id + 1

def traners(data,pack):
  global wisdom_id
  for pack_name in list(pack_list.keys()):
    if(data['pack'] == pack_name):
      data['pack_name'] = pack_list[str(pack_name)]
  
  text = str(wisdom_id) + ',' + data['name'] + ',,' + 'トレーナーカード,0,,,0,U,'+ data['pack_name'] + ',' + data['pack'] + ',' + data['kind'] + ',,' + data['effect']

  print(text)
  wisdom_id = wisdom_id + 1

def special_energy(data,pack):
  global wisdom_id
  for pack_name in list(pack_list.keys()):
    if(data['pack'] == pack_name):
      data['pack_name'] = pack_list[str(pack_name)]
  text = str(wisdom_id) + ',' + data['name'] + ',無,' + 'エネルギーカード,0,,,0,U,' + data['pack_name'] + ',' + data['pack'] + ',' + '特殊エネルギーカード,,' + data['effect']

  print(text)
  wisdom_id = wisdom_id + 1

def basic_energy(data,pack):
  global wisdom_id
  for pack_name in list(pack_list.keys()):
    if(data['pack'] == pack_name):
      data['pack_name'] = pack_list[str(pack_name)]
  
  data['type'] = data['name'].replace('エネルギー','')
  text = str(wisdom_id) + ',' + data['name'] + ',' + data['type'] + ',エネルギーカード,0,,,0,-,-,,基本エネルギーカード,,,,,,,,,,,,,,'

  print(text)
  wisdom_id = wisdom_id + 1
  