# Import the Firebase service
import firebase_admin
from firebase_admin import credentials, db

# Other Modules
import json

# Load appsettings JSON file
firebaseConfig = {
  "apiKey": "AIzaSyANQTcFR8VOPcbJVLvXuh2Le5xkSXoxxzU",
  "authDomain": "hirelinkx.firebaseapp.com",
  "databaseURL": "https://hirelinkx-default-rtdb.firebaseio.com",
  "projectId": "hirelinkx",
  "storageBucket": "hirelinkx.appspot.com",
  "messagingSenderId": "364671372495",
  "appId": "1:364671372495:web:4f73289bca230567ca3bba",
  "measurementId": "G-XF4MJCPEHR"
}

# Firebase-APIKey File
API_KEY_PATH = "appsetting.json"  # Add your API file path

# Initialize the default firebase app
certificate = credentials.Certificate(API_KEY_PATH)
firebaseApp = firebase_admin.initialize_app(certificate, {'databaseURL': firebaseConfig['databaseURL']})


class ToDoCollection():
    """Class to perform CRUD Operations with Firebase collection TODO"""

    def __init__(self,key,collection):
        """ Collection reference for ToDo """
        self.collection = db.reference(collection)
        self.key = key

    def __getSnapshot(self):
        """ Private method, It can access within class object
        To get snapshot of collection """
        return self.collection.get()

    def __findItem(self, id):
        """
            To find the item
            """
        snapshot = self.__getSnapshot()
        if snapshot == None:
            return False
        item = None
        for key, val in snapshot.items():
            if val[self.key] == id:
                item = key
                break
        if (item != None):
            node = self.collection.child(item)
            return node
        else:
            return False

    def addTodoItem(self, content,path):
        """ To push/add new todo items into collection """
        newcollection = self.collection.child(path)
        newcollection.push(content)


    def getTodoItems(self):
        """ To get the entire todo items list """
        snapshot = self.__getSnapshot()
        if snapshot == None:
            return []
        todos = []
        for key, val in snapshot.items():
            todos.append(val)
        return todos

    def getTodoItem(self, id):
        """ To get the todo item as dict which matches the id else return None """
        todoList = self.getTodoItems()
        todoItem = {}
        for item in todoList:
            for key,value in item.items():
                if key == id:
                    todoItem=item[id]
                else:
                    None
        # todoItem = next((item for item in todoList if item[id] == id), None)
        return todoItem

    def getTodoItemNew(self, key, value):
        """ To get the todo item based on provided key-value pair """
        todoList = self.getTodoItems()
        for item in todoList:
            if item.get(key) == value:
                return item
        return None
    
    def clearAllItems(self):
        """ To clear all nodes in the collection"""
        self.collection.delete()
        return True

    def updateTodoItem(self, id, content):
        """ To update existing todo item
            Return True
            If the key is not found then return false
         """
        newcollection = self.collection.child("Candidate").child(id)
        newcollection.update(content)

    def updateTodoItem2(self, id, content):
        """ To update existing todo item
            Return True
            If the key is not found then return false
         """
        newcollection = self.collection.child("Company").child(id)
        newcollection.update(content)

    def deleteTodoItem(self, id):
        """ To delete item from the list
            Return True
            If the key is not found then return false
         """
        itemMatchedNode = self.collection.child("add_new_oders").child(id)
        itemMatchedNode.delete()
        return True


