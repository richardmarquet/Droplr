import numpy as np
import requests
import json
from Item import Item
import pyrebase
import time

def getNeededItemsSold(curPrice, priceToMake, goalProfits):
   totalCurProfit = curPrice - priceToMake
   requiredSold = goalProfits / totalCurProfit
   return np.ceil(requiredSold)

def getOptimizedBulkPrice(priceToMake, percentProfits):
   priceToSell = priceToMake * (1 + percentProfits)
   return priceToSell

def listItem(originalPrice, bulkPrice, neededSold):
   print("n/a")

#Searched items
def getAllSearchItems(search_item):
    url = "https://gateway-staging.ncrcloud.com/catalog/items"

    querystring = {"pageNumber":"0","pageSize":"200","longDescriptionPattern":("%2A " + search_item)}

    headers = {
        'nep-application-key': "8a00860b6641a0ae0166471356ba000f",
        'accept': "application/json",
        'content-type': "application/json",
        'Authorization': "Basic YWNjdDpqYW1AamFtc2VydmljZXVzZXI6MTIzNDU2Nzg=",
        'Cache-Control': "no-cache",
        'Postman-Token': "d25fe7bb-7340-45ef-ab07-76205c9097f8"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response_dict = json.loads(response.text)

    #make a list with all the items that fit the search result
    #return the list

    print(response_dict)

#Get every single item
def getAllItems():
   url = "https://gateway-staging.ncrcloud.com/catalog/items/snapshot"

   headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'nep-application-key': "8a00860b6641a0ae0166471356ba000f",
    'nep-organization': "ncr-market",
    'nep-service-version': "2.2.1:2",
    'Authorization': "Basic YWNjdDpqYW1AamFtc2VydmljZXVzZXI6MTIzNDU2Nzg=",
    'Cache-Control': "no-cache",
    'Postman-Token': "918d01ae-25a6-4b13-9ec1-83b1d86c6571"
    }

   response = requests.request("GET", url, headers=headers)

   ncr_items = json.loads(response.text)["snapshot"]
   test = ncr_items[0]["shortDescription"]["values"][0]["value"] 
  
   itemList = [] 
   for items in ncr_items:
      itemList.append(Item(items["shortDescription"]["values"][0]["value"],items["longDescription"]["values"][0]["value"], 100))
      
   for items in itemList:
      print(items)

def printItemList(itemList):
   for item in itemList:
      print(item)

def testCase():
   a = getOptimizedBulkPrice(20, .41)
   b = getNeededItemsSold(a, 20, 10000)
   print(a)
   print(b)
