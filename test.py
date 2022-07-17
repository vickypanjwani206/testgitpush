import pymongo
import certifi

client = pymongo.MongoClient("mongodb+srv://vicky:vicky9007@cluster0.tlyoc.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())
db = client.test
print(db)

d={
    "name":"Bharat",
    "emaiid":"vickypanjwani206@gmail.com",
    "surname":"panjwani"
}

db1=client['mongotest']
coll=db1['test1']
coll.insert_one(d)

