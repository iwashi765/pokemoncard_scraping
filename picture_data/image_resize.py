from PIL import Image
import collections

#folder_list = {
#    'PROMO','sm5S','sm5M','sm5+','sm6','sm6a','sm6b','sm7','sm7a','sm7b','sm8','sm8a','sm8b','smE',
#    'sm9','sm9a','sm9b','sm10','sm10a','sm10b','sm11','sm11a','sm11b','sm12','sm12a','smI','smM',
#    's1H','s1W','s1a','s2','s2a','sA','sC','smP2','sp1'
#}
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
folder_list['sC']='S[スターターリザードン,オーロンゲ]'
folder_list['s2a']='S[爆炎ウォーカー]'
folder_list['s3']='S[ムゲンゾーン]'
folder_list['sD']='S[Vスタートデッキ]'
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


#wisdom内での通し番号。元データは9901まであったため
wisdom_id = 9902

def resize_picture():
    global wisdom_id
    for pack in folder_list.keys():
        print(pack)
        #ファイル数のためのデータ読み込み
        input_text_data = '../text_data/' + str(pack) + '/data.txt'
        with open(input_text_data,mode='r') as f:
            data = f.read().splitlines()
            #ファイル数を取得
            card_number = data.count('/')
            for file_number in range(card_number):
                text_path = '../text_data/' + str(pack) + '/' + str(file_number) + '.txt' 
                with open(text_path,mode='r') as r:
                    card_data = r.read().splitlines()
                    #カードのデータからidを取得して画像を開くためのpathに追加
                    card_id = card_data[len(card_data)-2]
                    picture_path = './' + str(pack) + '/' + str(card_id) + '.jpg'                           
                    #original_image = Image.open(picture_path).convert('RGB')
                    original_image = Image.open(picture_path)
                    resize_image = original_image.resize((int(40),int(55)))
                    #wisdomで圧縮後の画像を認識させるために名前を変えて保存
                    save_path = 'resize/' + str(pack) + '/pokemon_' + str(wisdom_id) + '.jpg'
                    resize_image.save(save_path)
                    wisdom_id = wisdom_id + 1

resize_picture()