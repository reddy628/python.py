class mobile:
    battery = 7500
    headphone_jack = 4.5

    def __init__(self, camera, storage, battery, screen):
        self.camera = camera
        self.storage = storage
        self.battery = battery
        self.screen = screen

    def taking_photo(self):
        print("taking photo and saved")
        self.storage = 128
        print("current storage is", self.storage)

vivo = mobile(4, 128, 7500, "oled")
oppo = mobile(6, 256, 6000, "lcd")

vivo.taking_photo()
oppo.taking_photo() 


class account:
    def __init__(self,name,balance):
        self.name=name
        self._balance=balance
    def get_balance(self):
        return self._balance  
    def set_balance(self,balance):
        self.__balance=balance  

ashok=account("ashok",10000)
chinnu=account("chinnu",9000)
print(ashok._balance)
print(chinnu._balance)
ashok._balance=9000
print(ashok.get_balance())
chinnu._balance=5000
print(chinnu.get_balance())











class person:
    def __init__(self,name,role):
        self.name=name
        self.role=role

groom=person("virat","groom")
bride=person("anushka","bride")
bride_father=person("ashok","bride father")
groom_father=person("prem","groom father")
uncle=person("ramesh","uncle")
aunt=person("suresh","aunt")



class marriage:
    def __init__(self,bride,groom):
        self.bride=bride
        self.groom=groom
        self.__budget=500000
    def show__budget(self,role):
        allowed__people=["bride","groom","bride father","groom father"]
        if role in allowed__people:
            print("budget is",self.__budget)
        else:
            print("you are not allowed to see the budget")
virushka_marriage=marriage(bride,groom)
virushka_marriage.show__budget        












class father:
    def __init__(self,land,house):
        self.land=land
        self.house=house

class groom(father):
    def __init__(self,land,house,salary):
        super().__init__(land,house)
        self.salary=salary
virat=groom("10 acres","2bhk",5000000)
print(virat.land) 
print(virat.salary)  
print(virat.house)     




