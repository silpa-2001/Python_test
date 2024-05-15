class Inventory:
    def __init__(self):
        self.items={}
    
    def add_items(self,item_id,item_name,stock_count,price):
        if item_id not in self.items:
            self.items[item_id]={
                "item_name":item_name,
                "stock_count":stock_count,
                "price":price
            }
            print(f"Item {item_name} added successfully ")

    def update(self,item_id,**kwargs):
        if item_id in self.items:
            item=self.items[item_id]
            for key,value in kwargs.items():
                if key in item:
                    item[key]=value
            print(f"Item_id {item_id} details updated successfully ")
        else:
            print(f"Item_id {item_id} not found ")
    
    def chk(self,item_id):
        if item_id in self.items:
            print(f"Item id: {item_id}")
            for key,value in self.items[item_id].items():
                print(f"{key.capitalize()}:{value} ")
        else:
            print(f"Item_id {item_id} not found ")

obj=Inventory()
obj.add_items(1001,"bag",12,7000)
obj.chk(1001)
obj.update(1001,stock_count=190)
obj.chk(1001)

