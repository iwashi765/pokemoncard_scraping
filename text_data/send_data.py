#import firebase_admin
import collections
#from firebase_admin import credentials
#from firebase_admin import firestore

#default_app = firebase_admin.initialize_app()
#db = firestore.client()

def pokemon_db(data,pack):
    #cred = '/home/ex-pc/work/card/cardsimulator-dda2b-firebase-adminsdk-ntvxn-6eb360ef52.json'

#    if data['ability'] == 'True':
#        data['ability'] = True
#    elif data['ability'] == 'False':
#        data['ability'] = False
#    if data['GX'] == 'True':
#        data['GX'] = True
#    elif data['GX'] == 'False':
#        data['GX'] = False
#    if data['TAG'] == 'True':
#        data['TAG'] = True
#    elif data['TAG'] == 'False':
#        data['TAG'] = False

#firebaseのデータベースにデータ追加
#    db.collection(u'pokemon').document(str(data['id'])).set(data)
    print(data['id'])
    write_path = str(pack) + '/' + str(data['id']) + '.txt'
    with open(write_path,mode='w') as w:
        for key in data.keys():
            w.write(str(data[key]) + '\n')


def traners_db(data,pack):
    collection_name = ''
    if data['kind'] == 'グッズ':
        collection_name = 'goods'
    elif data['kind'] == 'ポケモンのどうぐ':
        collection_name = 'tool'
    elif data['kind'] == 'サポート':
        collection_name = 'suport'
    elif data['kind'] == 'スタジアム':
        collection_name = 'stadium'
    #print(data)
#    db.collection(collection_name).document(str(data['id'])).set(data)
    print(data['id'])
    write_path = str(pack) + '/' + str(data['id']) + '.txt'
    with open(write_path,mode='w') as w:
        for key in data.keys():
            w.write(str(data[key]) + '\n')

def basic_energy_db(data,pack):
#    db.collection(u'basicenergy').document(str(data['id'])).set(data)
    print(data['id'])
    write_path = str(pack) + '/' + str(data['id']) + '.txt'
    with open(write_path,mode='w') as w:
        for key in data.keys():
            w.write(str(data[key]) + '\n')

def special_energy_db(data,pack):
#    db.collection(u'specialenergy').document(str(data['id'])).set(data)
    print(data['id'])
    write_path = str(pack) + '/' + str(data['id']) + '.txt'
    with open(write_path,mode='w') as w:
        for key in data.keys():
            w.write(str(data[key]) + '\n')