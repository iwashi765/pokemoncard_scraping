# 動作手順
元データ:トレーナーズウェブサイト https://www.pokemon-card.com/card-search/ の各カードの詳細ページ  
動作環境:python3.6以降

スクレイピングの手順  
1:データを追加したいパックまたはスターターのURL内の数字(カードID)の範囲をメモ  
2:text_data,picture_dataの各フォルダ内にパックまたはスターターの名前(sm2Lとか)でディレクトリを作成  
3:scrapingフォルダ内のdo_scraping.pyを (最小のカードID) (最大のカードID) (パック名) の3つの引数を入れて、
結果の出力ファイルを../text_data/(パック名)/data.txtに出力する形式で実行  
例 $python3 ~/pokemoncard_scraping/scraping/do_scraping.py 39268 39337 s5a > ../text_data/s5a/data.txt  
4:text_data内のmain.pyを実行  
これでtext_data/(パック名)内にカードID毎のテキスト内容が、picture_data/(パック名)内にカードID毎のカード画像が得られます  

※wisdom-EXにデータを追加する場合    
データ編  
5:wisdom内のmake_text_Data.py,write_data.pyを開き、folder_list内に追加したいパック名を追加  
6:$python3 ~/wisdom/main.py > pokemon.txt  
の形で一旦.txt形式で出力し、wisdomの仕様に合わせてShiftJIS形式に変換する  
$nkf -s pokemon.txt > pokemon_text.dat  
7:出力した.datをwisdom-EX内のものと置き換える    
画像編  
8:picture/resize内にパック名でディレクトリを作成  
9:image_resize.pyを開き、追加したパック名をfolder_listに追加  
10:image_resize.pyを実行すると、縮小した画像がpicture/resize内の各フォルダに生成されるので、これらをwisdom-EX内の画像データと置き換える    
パック名編  
11:wisdom-EX内のpokemon_expansion.datを開き、追加したパック名を追記する  

以上の手順で、wisdom-EXのデッキ作成を起動した際にカードが画像付きで反映されます
