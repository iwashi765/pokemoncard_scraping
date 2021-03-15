# card_bot
元データ:トレーナーズウェブサイト https://www.pokemon-card.com/card-search/ の各カードの詳細ページ  

スクレイピングの手順  
1:データを追加したいパックまたはスターターのURL内の数字(カードID)の範囲をメモ  
2:text_data,picture_dataの各フォルダ内にパックまたはスターターの名前(sm2Lとか)でディレクトリを作成  
scrapingフォルダ内のdo_scraping.pyを (最小のカードID) (最大のカードID) (パック名) の3つの引数を入れて、
結果の出力ファイルを../text_data/(パック名)/data.txtに出力する形式で実行  
$~/card_bot/scraping get_picture.py > ../text_data/(pack名)/add_data.txt  
3:text_data内のmain.pyを実行  
これでtext_data/(パック名)内にカードID毎のテキスト内容が、picture_data/(パック名)内にカードID毎のカード画像が得られます。
