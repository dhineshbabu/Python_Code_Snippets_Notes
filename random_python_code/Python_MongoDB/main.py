import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

cluster = 'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false'
client = MongoClient(cluster)
print(client.list_database_names())
db = client.test
print(db.list_collection_names())

# todo = {'name': 'TestUser1', 'text': 'My First Todo!', 'status': 'open',
#         'tags': ['python', 'coding'], 'date': str(datetime.datetime.utcnow())}

# todo = [{'name': 'TestUser2', 'text': 'My Second Todo!', 'status': 'open',
#         'tags': ['python', 'coding'], 'date': str(datetime.datetime.utcnow())},
#         {'name': 'TestUser3', 'text': 'My Third Todo!', 'status': 'open',
#          'tags': ['python', 'coding'], 'date': str(datetime.datetime.utcnow())}
#         ]

todos = db.todos
# result = todos.insert_one(todo)
# result = todos.insert_many(todo)
# result = todos.find_one()
# result = todos.find_one({'name': 'TestUser2'})
# result = todos.find_one({'name': 'TestUser2', 'text': 'My Second Todo!'})
# result = todos.find_one({'tags': 'python'})
# result = todos.find_one({'_id': ObjectId('6170b2376bf9e6e1b1a09d39')})
# results = todos.find({'tags': 'python'}) #pymongo.cursor.Cursor object
#
# for result in results:
#         print(result)

#  Count documents
# print(todos.count_documents({}))
# print(todos.count_documents({'tags': 'python'}))

# Filtering data for a particular time range
# d = datetime.datetime(2021, 10, 25)
# results = todos.find({'date': {'$lt': d}}).sort('name')
# for result in results:
#         print(result)

#  Removing items from the collection
# result = todos.delete_one({'_id': ObjectId('6170b2376bf9e6e1b1a09d39')}
#  delete_many, {} for deleting all

#  Update operation
result = todos.update_one({'tags': 'python'}, {'$set': {'status': 'done'}})