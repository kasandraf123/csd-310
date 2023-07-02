import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://kfigueroa:sriPkzN6yGv4ig75@cluster0.e6rald6.mongodb.net/pytech")
db = client["pytech"]
collection = db["students"]

#1.  print current contents of students collection
print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for x in collection.find():
	print("STUDENT ID: " + str(x['_id']))
	print("First Name: " + x['First Name'])
	print("Last Name: " + x['Last Name'] + "\n")

#2.  update last name of student with id 1007
update = {'_id': 1007}
#print(update)
updatevalue = {'$set': {'Last Name': 'Valdez'}}
#print(updatevalue)
collection.update_one(update,updatevalue)

#3.  print updated record of student with id 1007
find_one = {"_id": 1007}
#print(find_one)
results = collection.find_one(find_one)
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print("STUDENT ID: " + str(results['_id']))
print("First Name: " + results['First Name'])
print("Last Name: " + results['Last Name'] + "\n\n")

print("End of program, press any key to continue...")
