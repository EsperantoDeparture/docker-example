import pymongo
from bson.objectid import ObjectId

# The methods are ordered by the operation type (CRUD) and the objects involved (node, node_type, water_body, data and datum)
class Database:
    _db_client = pymongo.MongoClient('mongodb://exampledb:27017/')
    _default_db = _db_client.db
    _instance = None

    def __init__(self):
        # Shortcuts to the db collections
        self.todos = Database._default_db.todos
    
    def __new__(cls):  # Basic singleton pattern
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def list(self):
        return [{ **todo, "_id": str(todo["_id"])} for todo in self.todos.find({})]
    
    def edit(self, todo, tid):
        self.todos.update_one({
            "_id": ObjectId(tid)
        },
        {
            "$set": {
                **todo
            }
        })
    
    def delete(self, tid):
        self.todos.delete_one({
            "tid": ObjectId(tid)
        })
    
    def add(self, todo):
        self.todos.insert_one(todo)