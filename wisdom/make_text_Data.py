import output_data
import collections


folder_list = collections.OrderedDict()

#folder_list['smE']='SM「スターターセット伝説」'
#folder_list['sm5S']='SM「ウルトラサン」'
#folder_list['sm5M']='SM「ウルトラムーン」'
#folder_list['sm5+']='SM「ウルトラフォース」'
#folder_list['sm6']='SM「禁断の光」'
#folder_list['sm6a']='SM「ドラゴンストーム」'
#folder_list['sm6b']='SM「チャンピオンロード」'
#folder_list['sm7']='SM「裂空のカリスマ」'
#folder_list['sm7a']='SM「迅雷スパーク」'
#folder_list['smI']='SM[ブイズスターター]'
#folder_list['sm7b']='SM「フェアリーライズ」'
#folder_list['sm8']='SM「超爆インパクト」'
#folder_list['sm8a']='SM「ダークオーダー」'
#folder_list['sm8b']='SM「GXウルトラシャイニー」'
folder_list['sm9']='SM「タッグボルト」'
folder_list['sm9a']='SM「ナイトユニゾン」'
folder_list['smK']='SM「トレーナーバトルデッキ」'
folder_list['sm9b']='SM「フルメタルウォール」'
folder_list['sm10']='SM「ダブルブレイズ」'
folder_list['sm10a']='SM[ジージーエンド]'
folder_list['sm10b']='SM[スカイレジェンド]'
folder_list['sm11']='SM[ミラクルツイン]'
folder_list['smM']='SM[エフィデオスターター]'
folder_list['sm11a']='SM[リミックスバウト]'
folder_list['sm11b']='SM[ドリームリーグ]'
folder_list['smP2']='SM[名探偵ピカチュウ]'
folder_list['sm12']='SM[オルタージェネシス]'
folder_list['sm12a']='SM[タッグオールスターズ]'
folder_list['sA']='S[スターターセット(5種)]'
folder_list['s1W']='S[ソード]'
folder_list['s1H']='S[シールド]'
folder_list['sp1']='S[ザシアン+ザマゼンタBOX]'
folder_list['s1a']='S[VMAXライジング]'
folder_list['s2']='S[反逆クラッシュ]'
folder_list['sC']='S[スターター(2種)]'
folder_list['s2a']='S[爆炎ウォーカー]'
folder_list['s3']='S[ムゲンゾーン]'
folder_list['sD']='S[Vスターター]'
folder_list['s3a']='S[伝説の鼓動]'
folder_list['s4']='S[仰天のボルテッカー]'
folder_list['sp2']='S[VMAXスペシャルセット]'
folder_list['s4a']='S[シャイニースターV]'
folder_list['sC2']='S[VMAX初代御三家スターターセット]'
folder_list['s5I']='S[一撃マスター]'
folder_list['s5R']='S[連撃マスター]'
folder_list['sF']='S[プレミアムトレーナーBOX ICHIGEKI,RENGEKI]'
folder_list['s5a']='S[双璧のファイター]'
folder_list['PROMO']='プロモ'

def order_data(card_number,pack):
    #開始の数字が取得できないので加工前データを読み込んで加工
  for file_number in range(card_number):
    path = '../text_data/' + str(pack) + '/' + str(file_number) + '.txt'
    with open(path,mode='r') as r:
            data = r.read().splitlines()
            title = data[0]
            if title == 'ポケモン':
                output_data.pokemon_output(data,pack)
            elif title == 'グッズ':
                output_data.traner_output(data,pack)
            elif title == 'ポケモンのどうぐ':
                output_data.traner_output(data,pack)
            elif title == 'サポート':
                output_data.traner_output(data,pack)
            elif title == 'スタジアム':
                output_data.traner_output(data,pack)
            elif title == '特殊エネルギー':
                output_data.energy_output(data,pack)
            elif title == '基本エネルギー':
                output_data.basic_energy_output(data,pack)


def load_data():
    #パックごとに収録カードの枚数のためのデータ読み込み 発売順にするためにordereddictにした
  for pack in folder_list.keys():
    inputfile = '../text_data/' + str(pack) + '/data.txt'
    with open(inputfile,mode='r') as f:
            data = f.read().splitlines()
            for row in range(len(data)):
                data[row] = data[row].replace('\xa0','')
            #/の数でデータ数を取得
            card_number = data.count('/')
            order_data(card_number,pack)