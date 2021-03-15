# card_bot
元データ:トレーナーズウェブサイトの各カードの詳細ページ  

データベースの作成手順  
1:追加されたパックまたはスターターのURL内の数字の範囲をメモ  
2:text_dataフォルダ内にパックまたはスターターの名前(sm2Lとか)でディレクトリを作成  
scrapingフォルダ内のget_picture.pyにメモした数字の範囲をforループの範囲に入力し、結果の出力ファイルをcard_bot/text_data/(パック名)/data.txtに出力する形式で実行  
$~/card_bot/scraping get_picture.py > ../text_data/(pack名)/add_data.txt  
3:text_data内のmain.pyを実行