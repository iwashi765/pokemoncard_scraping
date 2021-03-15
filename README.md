# 動作手順
元データ:トレーナーズウェブサイト https://www.pokemon-card.com/card-search/ の各カードの詳細ページ  
動作環境:python3.6以降

スクレイピングの手順  
1:データを追加したいパックまたはスターターのURL内の数字(カードID)の範囲をメモ  
2:text_data,picture_dataの各フォルダ内にパックまたはスターターの名前(sm2Lとか)でディレクトリを作成  
3:scrapingフォルダ内のdo_scraping.pyを (最小のカードID) (最大のカードID) (パック名) の3つの引数を入れて、
結果の出力ファイルを../text_data/(パック名)/data.txtに出力する形式で実行  
例 $~/pokemoncard_scraping/scraping/do_scraping.py 39268 39337 s5a > ../text_data/s5a/data.txt  
4:text_data内のmain.pyを実行  
これでtext_data/(パック名)内にカードID毎のテキスト内容が、picture_data/(パック名)内にカードID毎のカード画像が得られます。
