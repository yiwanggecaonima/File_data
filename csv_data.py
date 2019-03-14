import csv
headers = ['A','b','c','d']
row = [
    ('aaa','bbb','ccc','ddd'),
    ('dsa','fgsweg','ewrew','sfaa'),
]
with open("./haha.csv", "w") as f:
    obj = csv.writer(f)
    obj.writerow(headers)
    for i in row:
        obj.writerow(i)
        
        
with open("./haha.csv", "r") as f:
    obj = f.readlines()
    for i in obj:
        print(i)
#     obj = csv.reader(f)
#     for i in obj:
#         print(i)
