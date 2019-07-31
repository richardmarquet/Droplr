from flask import Flask
from flask import jsonify
from flask import request
import algorithms as algo
import FirebaseFunctions as fb
import numpy as np
import requests
import json
from Item import Item
import pyrebase
import time

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCXsfhpkG-zZ_PfS8q66TqATunM4_dqTQ4",
        "authDomain": "droplr.firebaseapp.com ",
        "databaseURL": "https://droplr.firebaseio.com/",
        "storageBucket": "droplr.appspot.com"
    }

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
storage = firebase.storage()
db = firebase.database()

user = fb.login("cooltest9@gmail.com", "test12345", firebase)

#item = Item("Dell XPS 13","Laptop", 700, 1200, 4000, 2391, "10/12/19", "Electronics", "Dell", "true", firebase)
#item.uploadItem()

#print(fb.getItemList(firebase, user))

@app.route('/')
def index():
   return "Hello World!"

@app.route("/buyItem", methods=["POST"])
def buyItem():
   itemName = request.args.get("itemName")
   fb.buyItemWithName(itemName, user, firebase)

#EXAMPLE request: localhost:5000/refundItem?itemName=name
@app.route("/refundItem", methods=["DELETE"])
def refundItem():
   itemName = request.args.get("itemName")
   fb.refundItemWithName(itemName, user, firebase)

@app.route("/getAllItems", methods=["GET"])
def getAllItems():
   items = fb.getItemList(firebase, user)
   return items

#EXAMPLE request: localhost:5000/refundItem?email=email&password=password
@app.route("/createUser", methods=["POST"])
def createUser():
   email = request.args.get("email")
   password = request.args.get("password")
   user = fb.createUser(email, password, firebase)

@app.route("/login", methods=["POST"])
def login():
   email = request.args.get("email")
   passsord = request.args.get("password")
   user = fb.login(email, password, firebase)

@app.route("/getTrending", methods=["GET"])
def getTrending():
   resp = fb.getTrendingItems()
   return resp

@app.route("/getNearCompletion", methods=["GET"])
def getNearCompletion():
   resp = fb.getNearCompletionBucketList(firebase, user)

@app.route("/enableOverflow")
def enableOverflow():
   itemName = request.args.get("itemName") 
   print("hey")   

@app.route("/disableOverflow")
def disableOverflow():
   itemName = request.args.get("itemName")
   print("hey")



















#info = auth.get_account_info(user['idToken'])
#print(info["users"][0]["localId"])
#print(storage.child("images/hifimanhe400.jpg").get_url(user['idToken']))
#uploadPicture(storage, user, 'avatar.png')
# Pass the user's idToken to the push method
#results = db.child("users").push(data, user['idToken'])


#fb.printBucketList(firebase, user)
#fb.getTrendingItems(firebase, user)
#fb.printTrendingList(firebase, user)
#fb.pushToBucket(a[3], firebase, user)
#fb.popFromBucket(a[0], firebase, user)
# print(a[0])
#fb.buyItem(a[0], user, firebase)
#time.sleep(2)
#fb.refundItem(a[0], user, firebase)
#a = fb.sortByCostLowToHigh(a)
#a = fb.sortByCostHighToLow(a)
#printItemList(a)
#time.sleep(1)
#b = fb.getCostInList(a)
#algo.printItemList(b)

#fb.createUser("cooltest10@gmail.com","test12345",firebase)
#   item = Item("GTX 1080Ti","Graphics card", 300, 500, 500, 109, "10/12/19", "Electronics", "Nvidia", firebase)
#item.uploadItem()
#time.sleep(1)
#item.updateTotalSold()

