from flask import Flask
#from flask import jsonify
#from flask import request
import algorithms as algo
import FirebaseFunctions as fb
import numpy as np
import requests
import json
from Item import Item
import pyrebase
import time
#from collections import OrderedDict
from flask_cors import CORS


app = Flask(__name__)
CORS(app, support_credentials=True)

# cors = CORS(app, resources={r"/foo": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
#

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

#fb.getSearchItemList(firebase, user, "Asus")
print(fb.getShippedCompanyItems(firebase, user, "Yeti"))

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

@app.route("/getSearchItemList", methods=["GET"])
def getSearchItemList():
   searchTerm = request.args.get("searchTerm")
   return fb.getSearchItemList(firebase, user, searchTerm)

@app.route("/getSearchItemListByCompany", methods=["GET"])
def getSearchItemListByCompany():
   company = request.args.get("company")
   return fb.getSearchItemListByCompany(firebase, user, company)

@app.route("/getSearchItemListByDepartment", methods=["GET"])
def getSearchItemListByDepartment():
   department = request.args.get("department")
   return fb.getSearchItemListByDepartment(firebase, user, department)

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

@app.route("/enableOverflow", methods=["POST"])
def enableOverflow():
   itemName = request.args.get("itemName") 
   print("hey")   

@app.route("/disableOverflow", methods=["POST"])
def disableOverflow():
   itemName = request.args.get("itemName")
   print("hey")

@app.route("/getCompleteCompanyItems", methods=["GET"])
def getCompleteCompanyItems():
   company = request.args.get("company")
   return fb.getCompleteCompanyItems(firebase, user, company)

@app.route("/getIncompleteCompanyItems", methods=["GET"])
def getIncompleteCompanyItems():
   company = request.args.get("company")
   return fb.getIncompleteCompanyItems(firebase, user, company)

@app.route("/getShippedCompanyItems", methods=["GET"])
def getShippedCompanyItems():
   company = request.args.get("company")
   return fb.getShippedCompanyItems(firebase, user, company)

@app.route("/getPendingShipCompanyItems", methods=["GET"])
def getPendingShipCompanyItems():
   company = request.args.get("company")
   return fb.getPendingShipCompanyItems(firebase, user, company)








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
