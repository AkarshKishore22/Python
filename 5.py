class Anime:
    def __init__(self,name,rating):
        self.name=name
        self.rating=rating
    def display(self):
        print("name:",self.name,"and rating is",self.rating)
    

obj = Anime("kiminonawa",5)
obj.display()
