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

def buyItemWithName(itemName, user, firebase):
    item = getItemByName(itemName, firebase, user)
    if item != None:
        buyItem(item)

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
           "department" : item.department,
           "canOverflow" : item.canOverflow,
           "company" : item.company
       }
   }
   db.child("Users").child(getUserId(user, firebase)).child("boughtItems").update(data, user["idToken"])
   item.totalSold += 1
   #COME BACK and add the bucket
   val = (item.reqSold - item.getRemainingNeeded()) / item.reqSold
   if val >= 90:
      db.child("bucketNearCompletion").child(item.name).set(item.getRemainingNeeded(), user["idToken"])
   db.child("Items").child(item.name).update({"totalSold" : item.totalSold},user["idToken"])

def refundItemWithName(itemName, user, firebase):
   item = getItemByName(itemName, firebase, user)
   if item != None:
      refundItem(item)

def refundItem(item, user, firebase):
    db = firebase.database()
    db.child("Users").child(getUserId(user, firebase)).child("boughtItems").child(item.name).remove()
    item.totalSold -= 1
    db.child("Items").child(item.name).update({"totalSold" : item.totalSold},user["idToken"])

def uploadPicture(storage, user, name):
    storage.child("images/"+name).put(name, user["idToken"])

def getItemListJSON(firebase, user):
    db = firebase.database()
    resp = db.child("Items").get(user["idToken"])
    print(resp)
    return resp

def getItemByName(itemName, firebase, user):
   arr = getItemList(firebase, user)
   for item in arr:
      if item.name == itemName:
         return item
   return None

def getItemList(firebase, user):
    db = firebase.database()
    resp = db.child("Items").get(user["idToken"])
    itemList = []
    dict = {}
    for item in resp.each():
        val = item.val()
        dict[item.key()] = val
    #itemList.append(Item(val["name"], val["description"], val["cost"], val["prevCost"], val["reqSold"], val["totalSold"], val["shippingDate"], val["department"], val["company"], val["canOverflow"], firebase))
    return json.dumps(dict)

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
    dict = {}
    for item in resp.each():
        val = item.val()
        if searchTerm.casefold() in val["name"].casefold():
            print(val)
            dict[item.key()] = val
            #itemList.append(Item(val["name"], val["description"], val["cost"], val["prevCost"], val["reqSold"], val["totalSold"], val["shippingDate"], val["department"], val["company"], val["canOverflow"], firebase))
                #return json.dumps({"ItemList" : dict})
    return json.dumps(dict)

def getSearchItemListByDepartment(firebase, user, department):
    db = firebase.database()
    resp = db.child("Items").get(user["idToken"])
    itemList = []
    dict = {}
    for item in resp.each():
        val = item.val()
        if val["department"] == item.department:
           dict[item.key()] = val
           #itemList.append(Item(val["name"], val["description"], val["cost"], val["prevCost"], val["reqSold"], val["totalSold"], val["shippingDate"], val["department"], val["company"], val["canOverflow"], firebase))
    return json.dumps(dict)

def pushToBucket(item, firebase, user):
   db = firebase.database()
   numSold = db.child("bucket").child(item.name).get(user["idToken"]).val()
   if(numSold == None):
      db.child("bucket").child(item.name).set(1,user["idToken"])
      return
   resp = db.child("Items").get(user["idToken"])
   for t in resp.each():
       val = t.val()
       if val["name"] == item.name:
          db.child("bucket").child(item.name).set(numSold+1,user["idToken"])
          break

def popFromBucket(item, firebase, user):
    db = firebase.database()
    numSold = db.child("bucket").child(item.name).get(user["idToken"]).val()
    if numSold == 0 or numSold - 1 == 0:
       db.child("bucket").child(item.name).remove(user["idToken"])
       return
    resp = db.child("Items").get(user["idToken"])
    for t in resp.each():
        val = t.val()
        if val["name"] == item.name:
            db.child("bucket").child(item.name).set(numSold-1,user["idToken"])
            break

def getBucketList(firebase, user):
    db = firebase.database()
    bucketList = []
    resp = db.child("bucket").get(user["idToken"])
    for item in resp.each():
        bucketList.append(BucketItem(item.key(), item.val()))
    return bucketList

def printBucketList(firebase, user):
   a = getBucketList(firebase, user)
   for item in a:
      print(item.name + " : " + str(item.count))

def getTrendingItems(firebase, user):
   bucketList = getBucketList(firebase, user)
   bucketList.sort(key=lambda x: x.count, reverse=True)
   dict = {}
   for item in bucketList[0:8]:
      dict[item.name] = item.count
   return json.dumps(dict)

def printTrendingList(firebase, user):
   trendingList = getTrendingItems(firebase, user)
   for item in trendingList:
      print(item.name + " : " + str(item.count))

#for other bucket
def getNearCompletionBucketList(firebase, user):
    db = firebase.database()
    bucketList = []
    dict = {}
    resp = db.child("bucketNearCompletion").get(user["idToken"])
    for item in resp.each():
        dict[item.key()] = item.val()
        bucketList.append(BucketItem(item.key(), item.val()))
    return json.dumps(dict)


def printNearCompletionBucketList(firebase, user):
    a = getNearCompletionBucketList(firebase, user)
    for item in a:
        print(item.name + " : " + str(item.count))

def getTrendingNearCompletionItems(firebase, user):
    bucketList = getNearCompletionBucketList(firebase, user)
    bucketList.sort(key=lambda x: x.count, reverse=True)
    return bucketList[0:8]

def printTrendingNearCompletionList(firebase, user):
    trendingList = getTrendingNearCompletionItems(firebase, user)
    for item in trendingList:
       print(item.name + " : " + str(item.count))

def getCompanyTrends(companyName, firebase, user):
   db = firebase.database()
   dict = {}
   ItemList = db.child("Companies").child(companyName).child("ItemList").get(user["idToken"])
   for item in ItemList.each():
       dict[item.key()] = item.val()
   return json.dumps(dict)

def itemListToDict(ItemList):
   dict = {}
   
   for item in ItemList:
     dict[item.name] = item.getDict()
   
   return dict


class BucketItem:
    def __init__(self, name, count):
       self.name = name
       self.count = count
