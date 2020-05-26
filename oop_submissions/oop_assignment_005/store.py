import re
class Item:
    def __init__(self,name,price,category):
        self.name = name
        if price <=0:
            raise ValueError("Invalid value for price, got {}".format(price))
        else:
            self.price = price
        self.category = category
    
    
    def __str__(self):
        return ('{}@{}-{}'.format(self.name,self.price,self.category))
class Query:
    def __init__(self,field,operation,value):
        self.field = field
        self.value = value
        oper =["EQ","IN","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
        if operation in oper:
            self.operation = operation
        else:
            raise ValueError("Invalid value for operation, got {}".format(operation))
        
        
    def __str__(self):
        return(self.field+" "+str(self.operation)+" "+str(self.value))
        


class Store:
    
    def __init__(self):
        self.s = ""
        self.k = []
        
    def add_item(self,item):
        self.s = self.s+str(item)+"\n"
        self.k.append(item)
        
    def __str__(self):
        if len(self.s)>0:    
            #return self.s[:-1]
            return "\n".join(map(str,self.k))
        else:
            return "No items"
            
    def count(self):
        return len(self.k)
            
    def filter(self,query):
        result = Store()
        
        if query.operation == "IN":
            for i in self.k:
                if i.name in query.value or i.category in query.value or i.price in query.value :
                    result.add_item(i)
                    
        
        
            
        if query.operation == "EQ":   
            for i in self.k:
                if (query.field=='name' and i.name==query.value) or (query.field=='category' and i.category==query.value) or (query.field=='price' and i.price==query.value):
                    result.add_item(i)
                    
                    
        if query.operation == "GT":
            for i in self.k:
                if i.price>query.value:
                    result.add_item(i)
                  
           
            
            
        if query.operation == "GTE":
            for i in self.k:
                if i.price>=query.value:
                    result.add_item(i)
            
            
            
        if query.operation == "LT":
            for i in self.k:
                if i.price<query.value:
                    result.add_item(i)
            
        if query.operation == "LTE":
            for i in self.k:
                if i.price<=query.value:
                    result.add_item(i)
            
        
        if query.operation == "STARTS_WITH":
            for i in self.k:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                    result.add_item(i)
                
            
        if query.operation == "ENDS_WITH":
            for i in self.k:
                if i.name.endswith(query.value) or i.category.endswith(query.value):
                    result.add_item(i)
        
        if query.operation == "CONTAINS":# query.operation == "STARTS_WITH" or query.operation == "Ends_WITH":
            for i in self.k:
                if query.field=='name' and query.value in i.name or query.field=='category' and query.value in i.category:
                    result.add_item(i)
                
        return result
        
    def exclude(self,query):
        excluded_items=Store()
        included_items=self.filter(query)
        [excluded_items.add_item(i) for i in self.k if i not in included_items.k]        
        return excluded_items         

                 

        """
        if query.operation == "IN":
            for i in self.k:
                if i.name  in query.value or i.category  in query.value or i.price  in query.value :
                   pass
                else:
                    result1.add_item(i)
                    
        
        
            
        if query.operation == "EQ":   
            for i in self.k:
                if (query.field=='name' and i.name==query.value) or (query.field=='category' and i.category==query.value) or (query.field=='price' and i.price==query.value):
                    pass
                else:
                    result1.add_item(i)
                    
                    
        if query.operation == "GT":
            for i in self.k:
                if i.price<=query.value:
                    result1.add_item(i)
                  
           
            
            
        if query.operation == "GTE":
            for i in self.k:
                if i.price<query.value:
                    result1.add_item(i)
            
            
            
        if query.operation == "LT":
            for i in self.k:
                if i.price>=query.value:
                    result1.add_item(i)
            
        if query.operation == "LTE":
            for i in self.k:
                if i.price >query.value:
                    result1.add_item(i)
            
        
        if query.operation == "STARTS_WITH":
            for i in self.k:
                if i.name.startswith(query.value) or i.category.startswith(query.value):
                    pass    #  result.add_item(i)
                else:
                    result1.add_item(i)
            
        if query.operation == "ENDS_WITH":
            for i in self.k:
                if i.name.endswith(query.value) or i.category.endswith(query.value):
                    #result.add_item(i)
                    pass
                else:
                    result1.add_item(i)
                    
        if query.operation == "CONTAINS":
            for i in self.k:
                if query.field=='name' and query.value in i.name or query.field=='category' and query.value in i.category:
                        pass    #result.add_item(i)
                else:
                    result1.add_item(i)
                
        return result1
            
            
            
        """
"""          
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
  
query = Query(field="price", operation="LT", value=15)
print(query)


results = store.exclude(query)
print(results)
"""         
            
            
            
            
            
            

  