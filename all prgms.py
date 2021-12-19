def sample():
    gotoshop = "vegetable"
    breakfast = "dosa"
    study = "morning"
    caring = "did u had tablet"
    print(gotoshop,breakfast,study,caring)
    return
    sample()


class busticket:
    name = " akash "
    Transportdetails = "Tamilnadu  State Transport Corporation Limited"
    BusDepoName = "Kanchipuram/01"
    TicketNumber = "00086655"
    Datetime = "06/11/2014  14:58:47"
    From = "Chennai"
    To = "pondichery"
    Qty  = 2
    cost = 33.00
    Total = 33.00
    BusNo = "TN 01 N 2454"
    print(Transportdetails , BusDepoName ,  TicketNumber , Datetime , From , To , Qty , cost , Total , BusNo)
akash = busticket()
print(akash.Transportdetails , akash.BusDepoName ,  akash.TicketNumber , akash.Datetime , akash.From , akash.To , akash.Qty , akash.cost , akash.Total , akash.BusNo)



class travellerdetails:
      Nameofpassenger = "sid"
      TransactionID = 100000380284535	
      PNRNo = 4115023549
      From = "KJM"
      To  = "TPTY"
      DateofBooking = "14-Dec-2015"
      DateofJourney = "04-Jan-2016"
 
      
class traveldetails(travellerdetails):
      DateOfBoarding = "04-Jan-2016"
      TrainNoName = "56213 / TIRUPATI PASSENGER"
      Class = "SLEEPERCLASS"
      Quota = "GENERAL"
      ReservationUpto  = "TPTY"
      ScheduledDeparture = "21:00 Hrs"
      ReservationUpto  = "TPTY"
      BoardingAt ="KJM"	
      ScheduledDeparture = "21:00 Hrs"
      sid=travellerdetails()
      print(sid.Nameofpassenger)

class busticket:
    name = " akash "
    Transportdetails = "Tamilnadu  State Transport Corporation Limited"
    BusDepoName = "Kanchipuram/01"
    TicketNumber = "00086655"
    Datetime = "06/11/2014  14:58:47"
    From = "Chennai"
    To = "pondichery"
    Qty  = 2
    cost = 33.00
    Total = 33.00
    BusNo = "TN 01 N 2454"
    print(Transportdetails , BusDepoName ,  TicketNumber , Datetime , From , To , Qty , cost , Total , BusNo)
akash = busticket()
print(akash.Transportdetails , akash.BusDepoName ,  akash.TicketNumber , akash.Datetime , akash.From , akash.To , akash.Qty , akash.cost , akash.Total , akash.BusNo)

def PersonalDetails(Name , Dob , TimeBirth , PlaceBirth , Nativity , MartialStatus , Religion ,  Community , Caste , SubSect , MotherTongue , Gothram , Star , Height , Complexion , Qualification , BloodGroup ,University):    
    print(Name , Dob , TimeBirth , PlaceBirth , Nativity , MartialStatus , Religion ,  Community , Caste , SubSect , MotherTongue , Gothram , Star , Height , Complexion , Qualification , BloodGroup ,University)
    return
PersonalDetails("Naga Lalitha Kumari Bezawada" , "18-02-1989" , "7.30-8PM" , "Samalkota" , "Rajahmundry." ,  " UnMarried" , "Hindu" , "Telugu" , "Balija" , "Krishna Balija" , "Telugu" ,  "Mathala" , "Pushyami 3,4P" , "5'1''"  , "Medium" , "B.Tech(CS)" , "KIET,Kakinada" , "B+ve" )

'''def recharge(num,plan):
    if len(num)< 10:
        raise ValueError("invalid number")
    elif (plan==149) or (plan==669):
        print("recharge succesful")

recharge("988418092",669)
    '''

def templedetails():
    TicketType  = "Special Entry Darshan"
    Date = "Dec 1st"
    Day = "Tuesday"
    Time = "3:30 Am" 
    PerSlotTickets = "2000"
    BookingNo       = "IS151110080016"
    NameofthePilgrim = "venkatesh"
    OrderNo         = "010600013554"
    Email            = "venkateshprofessional7@gmail.com"
    Amountinfigures = "220.00"
    ProofofID = "Aadhaar Card 733498928758"
    BookedDateTime = "11062015 11:36:46"
    NoofPersons =  1
    NameoftheSevaDarshan = "Archana"
    ReportingTime = "4:00 AM"
    PerformanceDateTime = "12012015 AM 4:30:00"
    PrivilegestotheSeva = "Two Small Laddu"
    BookedTime = "11:36:46"
    AccommodationType =  "Rs 500 Tirumala"
    Available  =            350
    Rate =   "50 to 2000"
    print( TicketType , Date ,Day , Time , PerSlotTickets , BookingNo , NameofthePilgrim , OrderNo , Email , Amountinfigures , ProofofID , BookedDateTime , NoofPersons,NameoftheSevaDarshan , ReportingTime , PrivilegestotheSeva , BookedTime , AccommodationType , Available , Rate)
    return
templedetails()

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

allpt=["hpp1","hpp2","hpp3",]
def hp(patientname,patientid):
  if(patientid in allpt):
    print(patientname,patientid)
    return
ret =hp("ram","hpp1")

import asyncio


def  broadband( ):
 AccountNo =1135497
 BroadbandUserID = 11128550
 IPAddress= "10.245.97.123"
 print( AccountNo,BroadbandUserID,IPAddress)
 return

broadband()


from asyncio import *

class education:
     college="srm"
     stream ="cse"

ram=education()

class job(education):
       company="disys"

abhiesk=job()

class marriage(job):
         wifename="xyz"

jv=marriage()

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

allpt=["hpp1","hpp2","hpp3",]
def hp(patientname,patientid):
  if(patientid in allpt):
    print(patientname,patientid)
    return
ret =hp("ram","hpp1")

import asyncio


def  broadband( ):
 AccountNo =1135497
 BroadbandUserID = 11128550
 IPAddress= "10.245.97.123"
 print( AccountNo,BroadbandUserID,IPAddress)
 return

broadband()


from asyncio import *

class education:
     college="srm"
     stream ="cse"

ram=education()

class job(education):
       company="disys"

abhiesk=job()

class marriage(job):
         wifename="xyz"

jv=marriage()


class food:
    meal ="south indian"
    dish="egg masala"

abhiesh=food()
venkatesh=food()
    

def  Mother( ):       
       gotoshop ="vegitables"    
       breakfast = "idly"       
       study ="morning"             
       caring="did u had tablet"  
       return 

Mother( ) 

def  pizza():
      quantity=6
      flavour="cheese"
      price=600
      return 

pizza()
    


'''import pack

class software(pack.camera):
    def __init__(self ,processor,os:list):
        print("launched 12")
        if(os is not list):
           raise TypeError("invalid datatype")
        super().__init__("12px","4k","a14",["IOS 11","IOS 12" , "IOS 13" , "IOS 14"])
        self.chip = processor
        self.system = os
Akash = software("a14","IOS")
'''

allpt =["pt12","pt13" ]

def hc( patientname , pateintid):
    if ( pateintid  in allpt):
       print( patientname , pateintid )
    return 0

ret=hc("ram", "pt12")  
hc("jv",1212)

def  healthcare( ):
      PatientName=" Sathish"
      PatientID= 10567890890
      Patientphone="044222738"
      Billno=56725
      Age=34
      DateofBirth ="15/05/1991"
      Gender="Male" 
      Fasting="Yes"
      print(  PatientName )
      return

class personaldata:
      Age=34
      DateofBirth ="15/05/1991"
      Gender="Male" 
      Fasting="Yes"

class patient(personaldata):
      PatientName=" Sathish"
      PatientID= 10567890890
      Patientphone="044222738"
      Billno=56725

jv=patient()

def  healthcare( ):
      PatientName=" Sathish"
      PatientID= 10567890890
      Patientphone="044222738"
      Billno=56725
      Age=34
      DateofBirth ="15/05/1991"
      Gender="Male" 
      Fasting="Yes"
      print(  PatientName )
      return

healthcare()


class  healthcare:
      PatientName=" Sathish"
      PatientID= 10567890890
      Patientphone="044222738"
      Billno=56725
      Age=34
      DateofBirth ="15/05/1991"
      Gender="Male" 
      Fasting="Yes"

sathish=healthcare()
print(healthcare.PatientName)

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

def  enrollment(course,technology):
          print(course,technology  )
def  demo():
          trainername = "venkatesh"
          fees = 14000
          duration = 36
          print("demo details",trainername ,fees,duration)
          return fees
def  receipt():
          print(" Paid fess : 14000 ")
venkatesh = enrollment("f","efrw")
venkatesh = demo()
venkatesh = receipt()

def office(cabinid):

       if cabinid == "DYS101":
          print(" Manager Sriram ")
       elif  cabinid == "DYS201":
        print("Manager Hari")


office("DYS201")
officeactivities = [ [ "emailing checking","meeting","work"] ,

[ "emailing checking","meeting","idle"]  ]


count =0

for i in officeactivities :

      if  i == "idle":

         count =count+1
print( count )

dailyact  = ["music","eating","working","calls","facebook","utube"  ]
for i in dailyact  :
      if i  == "music":
         print(" listening music")
         
class developer:
    def __init__(self,t):
        self.team=t
        print(t)
suresh = developer(1)
ramesh = developer(1)




    
    
    
    
    
        




               


    
    
    
    
    
        




                   

    


