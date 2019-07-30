#firebase stuff
import numpy as np
import requests
import json
from Item import Item
import pyrebase
import time

def login(email, password, firebase):
   auth = firebase.auth()
   user = auth.sign_in_with_email_and_password(email, password)
   return user

def createUser(email, password, firebase):
    auth = firebase.auth()
    user = auth.create_user_with_email_and_password(email, password)
    
    db = firebase.database()
    data = {
        "email" : email
    }
    db.child("Users").update({getUserId(user, firebase) : data}, user["idToken"])
    
    return login(email, password, firebase)

def getUserId(user, firebase):
    auth = firebase.auth()
    info = auth.get_account_info(user['idToken'])
    return info["users"][0]["localId"]

def buyItem(item, user, firebase):
   db = firebase.database()
   data = {
       item.name : {
           "name" : item.name,
           "description" : item.description,
           "cost" : item.cost,
           "prevCost" : item.prevCost,
           "reqSold" : item.reqSold,
           "totalSold" : item.totalSold,
           "shippingDate" : item.shippingDate,
           "tags" : {
               "tag0" : item.tags['tag0'],
               "tag1" : item.tags['tag1'],
               "tag2" : item.tags['tag2'],
               "tag3" : item.tags['tag3'],
               "tag4" : item.tags['tag4']
           }
       }
   }
   db.child("Users").child(getUserId(user, firebase)).child("boughtItems").update(data, user["idToken"])
   item.totalSold += 1
   db.child("Items").child(item.name).update({"totalSold" : item.totalSold},user["idToken"])

def refundItem(item, user, firebase):
    db = firebase.database()
    db.child("Users").child(getUserId(user, firebase)).child("boughtItems").child(item.name).remove()
    item.totalSold -= 1
    db.child("Items").child(item.name).update({"totalSold" : item.totalSold},user["idToken"])

def uploadPicture(storage, user, name):
    storage.child("images/"+name).put(name, user["idToken"])

def getItemList(firebase, user):
    db = firebase.database()
    resp = db.child("Items").get(user["idToken"])
    itemList = []
    for item in resp.each():
        val = item.val()
        itemList.append(Item(val["name"], val["description"], val["cost"], val["prevCost"], val["reqSold"], val["totalSold"], val["shippingDate"], val["tags"], firebase))
    return itemList

def sortByCostLowToHigh(itemList):
    itemList.sort(key=lambda x: x.cost)
    return itemList

def sortByCostHighToLow(itemList):
    itemList.sort(key=lambda x: x.cost, reverse=True)
    return itemList

def sortByNameLowToHigh(itemList):
    itemList.sort(key=lambda x: x.name)
    return itemList

def sortByNameHighToLow(itemList):
    itemList.sort(key=lambda x: x.name, reverse=True)
    return itemList

def getNamesInList(itemList):
    names = []
    for item in itemList:
        names.append(item.name)
    return names

def getCostInList(itemList):
    costs = []
    for item in itemList:
        costs.append(item.cost)
    return costs

def getSearchItemList(firebase, user, searchTerm):
    db = firebase.database()
    resp = db.child("Items").get(user["idToken"])
    itemList = []
    for item in resp.each():
        val = item.val()
        if searchTerm.casefold() in val["name"].casefold():
            itemList.append(Item(val["name"], val["description"], val["cost"], val["prevCost"], val["reqSold"], val["totalSold"], val["shippingDate"], val["tags"], firebase))
    return itemList
