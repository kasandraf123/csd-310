from pymongo import MongoClient
url = "mongodb+srv://kfigueroa:sriPkzN6yGv4ig75@cluster0.e6rald6.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech
print (db.list_collection_names())
