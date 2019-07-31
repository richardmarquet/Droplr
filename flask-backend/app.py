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
from collections import OrderedDict
from flask_cors import CORS
import tensorflow as tf
import sys



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


def getKNN(predicitionPoint, features, labels, k):
    val = tf.pow(tf.pow(tf.subtract(features, predicitionPoint), 2), 2)
    val_sum = tf.reduce_sum(val, 1)
    val_float = tf.to_float(val_sum)
    val_sqrt = tf.sqrt(val_sum)
    val_expand = tf.expand_dims(val_sqrt, 1);
    labels = tf.to_float(labels);

    print("val_expand", val_expand)
    val_concat = tf.concat([val_expand, labels], 1)
    # print("****!!!!!!!!!!!!!!!!val_concat: ",val_concat)
    val_unstack = tf.unstack(val_concat)
    print("****!!!!!!!!!!!!!!!!val_unstack: ",val_unstack)

    sess = tf.InteractiveSession()
    val_sort = sorted(val_unstack, key=lambda x:x.eval().tolist()[0])
    print("****!!!!!!!!!!!!!!!!val_sort: ",val_sort)

    val_slice = val_sort[0: k]

    return val_slice

def jsonArrayConverter(inarray):
  jsonObj = json.loads(inarray)
  features = []
  labels = []
  element = 0
  money = 0
  # print("ITEMMM TYPE: ", type(jsonObj))
  # print("ITEMMM: ", jsonObj)
  for item in jsonObj:
    print("ITEMMM: ", jsonObj[item])
    department = 0.0
    money = 0.0
    days = 0.0

    for key in jsonObj[item]:
        if key == ("department"):
            if jsonObj[item][key] == ("Appliances"):
              department = 0.25
            elif jsonObj[item][key] == ("Clothing"):
              department = 0.5
            elif jsonObj[item][key] == ("Outdoors"):
              department = 0.75
            elif jsonObj[item][key] == ("health"):
              department = 0.1
        elif key == ("cost"):
            money = jsonObj[item][key]/ 5000.0
        elif key == "shippingDate":
            days = jsonObj[item][key]/ 60.0
        elif (key == "name"):
            labels.append(jsonObj[item][key])
    features.append([department, money, days])
    money = 0
    days = 0
  return [features, labels]


@app.route('/getSuggestedItems')
def runTensor():
    allitems = fb.getItemList(firebase, user)
    results = jsonArrayConverter(allitems)
    playlist_features = results[0]
    labels = results[1]
    playlist_labels = [i for i in range(0, len(labels))]

    target_features= [.01,.1,.05]
    k = 5


    tffeatures = tf.constant(playlist_features);
    tflabels = tf.expand_dims(tf.constant(playlist_labels), 1);
    tfpred = tf.constant(target_features);

    arr = getKNN(tfpred, tffeatures, tflabels, k)
    item_names = []
    pos = 0
    for item in arr:
        item_names.append(labels[int(item.eval().tolist()[1])])
        print(labels[int(item.eval().tolist()[1])])
        pos += 1

    return jsonify({"closest_items": item_names})




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
