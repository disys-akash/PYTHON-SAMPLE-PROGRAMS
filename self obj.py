class creditcard:
    cardlimit = 5000
    def basicdetails(self):
        self.cardno = 5545
        self.name = "ram"
    def reccard(self):
        print(self.cardno , self.name)
ram = creditcard()
ram.basicdetails()
ram.reccard()

class appearancedetails:
    def healthdetails(self):
        self.nmae= "raja"
        self.Weight = 55
        self.Hight = 5.8
        self.Eyecolour = "brown"
        Gender = "male"
        Homeaddress = "#6/96,rajampet,kadapa."
        self.Homephone = 975545445
        self.mobile = 8553577745
        self.State = "andhrapradesh"
        self.county = "india"
    def execution(self):
        print(self.nmae,self.mobile)
raja = appearancedetails()
raja.healthdetails()
raja.execution()

import pack

class software(pack.camera):
    def __init__(self ,processor,os:list):
        print("launched 12")
        if(os is not list):
           raise TypeError("invalid datatype")
        super().__init__("12px","4k","a14",["IOS 11","IOS 12" , "IOS 13" , "IOS 14"])
        self.chip = processor
        self.system = os
Akash = software("a14","IOS")


    
    
    
    
    
        
