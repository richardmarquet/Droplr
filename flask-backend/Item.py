import pyrebase

class Item():
   def __init__(self, name, description, cost, prevCost, reqSold, totalSold, shippingDate, department, company, canOverflow, picture, firebase):
      self.name = name
      self.description = description
      self.cost = cost
      self.prevCost = prevCost
      self.reqSold = reqSold
      self.totalSold = totalSold
      self.shippingDate = shippingDate
      self.department = department
      self.company = company
      self.canOverflow = canOverflow
      self.picture = picture
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
         "department" : self.department,
         "canOverflow" : self.canOverflow,
         "picture" : self.picture,
         "company" : self.company
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
      db.child("Items").child(self.name).update(data)
      print(self.totalSold)

   def updateShippingDate(self, newShippingDate):
      self.shippingDate = newShippingDate
      db = self.firebase.database()
      data = { "shippingDate" : self.shippingDate }
      db.child("Items").child(self.name).update(data)

   def updateDescription(self, newDescription):
      self.description = newDescription
      db = self.firebase.database()
      data = { "description" : self.description }
      db.child("Items").child(self.name).update(data)
   
   def setComplete(self):
      if self.totalSold >= self.reqSold:
         return True
      return False

   def getDict(self):
      data = {
         "name" : self.name,
         "description" : self.description,
         "cost" : self.cost,
         "prevCost" : self.prevCost,
         "reqSold" : self.reqSold,
         "totalSold" : self.totalSold,
         "shippingDate" : self.shippingDate,
         "department" : self.department,
         "canOverflow" : self.canOverflow,
         "picture" : self.picture,
         "company" : self.company
      }
      return data


   def __str__(self):
      return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
