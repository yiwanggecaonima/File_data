import csv
import json

import pymongo

client = pymongo.MongoClient('127.0.0.1',27017)
# client = pymongo.MongoClient('127.0.0.1',27017)

db = client['QXB']
# datas = db.get_collection('qxb').find({},{'_id':0})
datas = db.get_collection('qxb').find({},{'_id':0,})

with open('qxb.csv', 'a', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([i for i in datas[0].keys()])

for list_item in datas:
    with open('qxb.csv', 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        # for i in list_item.keys()
        # writer.writerow([i for i in list_item.keys()])
        writer.writerow([list_item[i] for i in list_item.keys()])
    print('*' * 10 + '保存成功' + '*' * 10)
