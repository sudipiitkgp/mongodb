import pymongo
client = pymongo.MongoClient("mongodb+srv://sudippaik:usuitakumi@cluster0.v3yyqhf.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name":"sudip",
    "email" : "sudip@gmail.com",
    "surname" : "paik"
}
db1 = client['mongo']
coll = db1['test']
coll.insert_one(d )
\