from flask import Flask
import algorithms as algo
import FirebaseFunctions as fb
import numpy as np
import requests
import json
from Item import Item
import pyrebase
import time

app = Flask(__name__)
 
@app.route('/')
def index():
    return "Hello World!"

def setup():
    config = {
        "apiKey": "AIzaSyCXsfhpkG-zZ_PfS8q66TqATunM4_dqTQ4 ",
        "authDomain": "droplr.firebaseapp.com ",
        "databaseURL": "https://droplr.firebaseio.com/",
        "storageBucket": "droplr.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    storage = firebase.storage()
    db = firebase.database()

    user = fb.login("cooltest9@gmail.com", "test12345", firebase)
    #info = auth.get_account_info(user['idToken'])
    #print(info["users"][0]["localId"])
    #print(storage.child("images/hifimanhe400.jpg").get_url(user['idToken']))
    #uploadPicture(storage, user, 'avatar.png')
    # Pass the user's idToken to the push method
    #results = db.child("users").push(data, user['idToken'])

    a = fb.getItemList(firebase, user)
    # print(a[0])
    fb.buyItem(a[0], user, firebase)
    time.sleep(2)
    fb.refundItem(a[0], user, firebase)
    #a = fb.sortByCostLowToHigh(a)
    #a = fb.sortByCostHighToLow(a)
    #printItemList(a)
    #time.sleep(1)
    #b = fb.getCostInList(a)
    #algo.printItemList(b)

    #fb.createUser("cooltest10@gmail.com","test12345",firebase)
#tags = ["Technology", "Electronics", "Quality", "Audio", "Hifi"]
#   item = Item("-Ll-wiDoifpk82ektBJQ", "Axon 7","Asus notebook", 150, 250, 500, 231, "10/12/19", tags, firebase)
#   item.uploadItem()
    #time.sleep(1)
    #item.updateTotalSold()

setup()
