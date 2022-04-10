import pymongo
from pyparsing import col
client = pymongo.MongoClient("mongodb+srv://aditya:Aadi_747392@cluster0.23zaf.mongodb.net/Cluster0?retryWrites=true&w=majority")
db = client['awd']
coll = db['schema']

a = {
    "ed":"wd"
}
coll.insert_one(a)