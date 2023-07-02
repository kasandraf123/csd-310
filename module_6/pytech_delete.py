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
    

#2.  insert new student with id 1010
record = { "_id": 1010,
          "First Name": "Jack",
          "Last Name": "Frost"}
collection.insert_one(record)

#3.  call find_one() to display new student with 1010
find_one = {"_id": 1010}
results = collection.find_one(find_one)
print("-- DISPLAYING STUDENT DOCUMENT 1010 --")
print("STUDENT ID: " + str(results['_id']))
print("First Name: " + results['First Name'])
print("Last Name: " + results['Last Name'] + "\n\n")


#4.  delete student with id 1010
delete_one ={"_id": 1010}
collection.delete_one(delete_one)

#5.  display contents of collection after delete
print ("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY AFTER DELETING STUDENT WITH ID 1010 --")
for x in collection.find():
	print("STUDENT ID: " + str(x['_id']))
	print("First Name: " + x['First Name'])
	print("Last Name: " + x['Last Name'] + "\n")
	

print("End of program, press any key to continue...")
