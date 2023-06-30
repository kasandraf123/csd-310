from pymongo import MongoClient
client = MongoClient("mongodb+srv://kfigueroa:sriPkzN6yGv4ig75@cluster0.e6rald6.mongodb.net/pytech")
db = client["pytech"]
collection = db["students"]
updateone = ({"_id" : 1010}, {set : {"Last Name" : "Danger"}})
collection.insert_one("post")  
                                  