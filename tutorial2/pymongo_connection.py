import pymongo

# Username: userK65
# Password: ANBcJRBjrHxWbyXy
# Database Name: sampledb
# Connection URL: mongodb://userK65:ANBcJRBjrHxWbyXy@mongodb/sampledb
# Routes external traffic
# http://mongodb-mongo.192.168.99.101.nip.io 

CLIENT = pymongo.MongoClient('mongodb',
username='userK65',
password= 'ANBcJRBjrHxWbyXy'
)

db = CLIENT['workshop'] #base de datos workshop

print(CLIENT['workshop'])
#['database']['collection']
coll = CLIENT['workshop']['usuarios']
print(coll)

myitem = coll.insert_one({'name':'Pepe'}).insert_id #insert_id atributo agrega id al elemento

print(myitem)

retrieved_item = coll.find_one({'name':'Pepe'})
print(retrieved_item)

usuarios = [
    {"_id":1, 'name':'Alejandro'},
    {"_id":2, 'name':'Praveen'}
]

ids_usuarios = coll.insert_many(usuarios).insert_ids
print(ids_usuarios)

users = []
for row in  coll.find():
    users.append(row)
# print(len(users))
print(users)

coll.delete_many({})
users = []
for row in  coll.find():
    users.append(row)

