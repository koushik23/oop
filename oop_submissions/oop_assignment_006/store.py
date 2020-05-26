
class Item:
    def __init__(self,price,name,category):
        self.name=name
        self.price=price
        self.category=category
        if self.price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
    def __str__(self):
        return self.name+"@"+str(self.price)+"-"+self.category
class Query:
    def __init__(self,field,operation,value):
        compare=["EQ","IN","GT","GTE","LT","LTE","STARTS_WITH","ENDS_WITH","CONTAINS"]
        self.field=field
        self.operation=operation
        self.value=value
        if self.operation not in compare:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
    def __str__(self):
        return self.field+" "+self.operation+" "+str(self.value)    

class Store:
    def __init__(self):
        self.items=[]
        self.counter = 0
    def count(self):
        return len(self.items)
    
    def __str__(self):
        
        if len(self.items)>0:
            if self.counter>1:
                return "\n".join(map(str,self.counter))
            else:    
                return "\n".join(map(str,self.items))
        else:
            return "No items"
            
            
    def __add__(self,other):
        s = Store()
        for i in other.items:
            s.add_item(str(i))
        for i in self.items:
            s.add_item(str(i))
            
        return s
        
        
        
    def add_item(self,item_obj):
        self.items.append(item_obj)
    
    
    def filter(self,*argv):
        results=Store()
        for query_obj in argv:
            self.counter+=1
            if query_obj.operation == "IN" or query_obj.operation == "EQ":
                if not isinstance(query_obj.value,list):
                     query_obj.value=[query_obj.value]
                [results.add_item(item) for value in query_obj.value for item in self.items if value in item.__dict__.values()]
        
            elif query_obj.operation == "GT":     
                [results.add_item(item) for item in self.items if item.price>query_obj.value]
        
            elif query_obj.operation == "GTE":     
                [results.add_item(item) for item in self.items if item.price>=query_obj.value ]        
        
            elif query_obj.operation == "LT":
                [results.add_item(item) for item in self.items if item.price<query_obj.value]        
        
            elif query_obj.operation == "LTE":     
                [results.add_item(item) for item in self.items if item.price<=query_obj.value]        
        
            elif query_obj.operation == "STARTS_WITH" or query_obj.operation == "ENDS_WITH" or query_obj.operation == "CONTAINS":     
                    for item in self.items:
                        if (query_obj.field in item.__dict__.keys() and query_obj.value in str(item.__dict__[query_obj.field])):
                            results.add_item(item)   
            
            print(self.counter)
                        
        return results                

        
    def exclude(self,*argv):
        excluded_items=Store()
        for query_obj in argv:
            self.counter+=1
            included_items=self.filter(query_obj)
            [excluded_items.add_item(i) for i in self.items if i not in included_items.items]        
        return excluded_items         
    









store = Store()
item = Item(name="Oreo Biscuits", price=30, category="Food")
store.add_item(item)
item = Item(name="Boost Biscuits", price=20, category="Food")
store.add_item(item)
item = Item(name="ParleG Biscuits", price=10, category="Food")
store.add_item(item)
#print(store)
# Oreo Biscuits@30-Food
# Boost Biscuits@20-Food
# ParleG Biscuits@10-Food

query = Query(field="price", operation="GT", value=15)

query = Query(field="name", operation="CONTAINS", value="oo")
results = store.exclude(query, query) # should be able to give any number of Query objects as arguments
print(results)