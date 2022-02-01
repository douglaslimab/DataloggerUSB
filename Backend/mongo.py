import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mongo_data_logger"]
mycoll = mydb["temperature"]

my_dictionary = {"id": 0, "temp": 15}

out = mycoll.insert_one(my_dictionary)
print(out)