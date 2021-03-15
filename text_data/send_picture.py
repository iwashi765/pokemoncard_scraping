import os
import google.cloud.storage

folder_list = {
    'PROMO','sm5S','sm5M','sm5+','sm6','sm6a','sm6b','sm7','sm7a','sm7b','sm8','sm8a','sm8b','smE',
    'sm9','sm9a','sm9b','sm10','sm10a','sm10b','sm11','sm11a','sm11b','sm12','sm12a','smI','smM',
    's1H','s1W','s1a','s2','s2a','sA','sC','smP2','sp1'
}

storage_client = google.cloud.storage.Client()
bucket_name = 'cardsimulator-dda2b.appspot.com'
bucket = storage_client.get_bucket(bucket_name)

def data_read():
    for pack in folder_list:
        inputfile = str(pack) + '/home/ex-pc/work/card/simulator/' +str(pack)+ '/data.txt'
        with open(inputfile,mode='r') as f:
            data = f.read().splitlines()
            card_number = data.count('/')
            for number in range(card_number):
                send_data(data,pack)

def send_data(data,pack):
#    for pack in folder_list:
        source_file_name = '/home/ex-pc/work/card/simulator/picture_data/' +str(pack)+ '/'+str(data['id']) +'.jpg'
        blob = bucket.blob(os.path.basename(source_file_name))
        blob.upload_from_filename(source_file_name)

#print('success')