import pyrebase

class Item():
   def __init__(self, name, description, cost, prevCost, reqSold, totalSold, shippingDate, tags, firebase):
      self.name = name
      self.description = description
      self.cost = cost
      self.prevCost = prevCost
      self.reqSold = reqSold
      self.totalSold = totalSold
      self.shippingDate = shippingDate
      self.tags = tags
      self.firebase = firebase
 
   def uploadItem(self):
      db = self.firebase.database()
      data = {
	 "name" : self.name,
	 "description" : self.description,
	 "cost" : self.cost,
	 "prevCost" : self.prevCost,
 	 "reqSold" : self.reqSold,
	 "totalSold" : self.totalSold,
	 "shippingDate" : self.shippingDate,
         "tags" : {
            "tag0" : self.tags[0],
            "tag1" : self.tags[1],
	    "tag2" : self.tags[2],
 	    "tag3" : self.tags[3],
	    "tag4" : self.tags[4] 
         }
      }
      db.child("Items").child(self.name).set(data)

   def getRemainingNeeded(self):
      return self.reqSold - self.totalSold
   
   def getCostDif(self):
      return self.prevCost - self.cost

   def updateTotalSold(self):
      self.totalSold += 1
      db = self.firebase.database()
      data = { "totalSold" : self.totalSold }
      db.child("Items").child(self.key).update(data)
      print(self.totalSold)

   def updateShippingDate(self):
      #connect to database
      db = self.firebase.database()
      
      return 1

   def updateDescription(self):
      #connect to database
      return 1

   def __str__(self):
      return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
