name = "raja"
#2nd_type
class details:
    __num = 98841
    def __init__(self):
        self.__dob = "22/5/2001"
    def print(self):
        print(self.__dob)
raja = details()
raja.print()
#raja is a object class of details where details is a user defined class
#type_3
empdetails = ("raj","suresh","ramesh","rajesh","rakesh")
print(empdetails[1])
#empdetails_is_a clss of tuple where tuple is a inbuilt class
#type_4
routine = {"eat":"breakfast","watch":"movies","play":"cricket"}
print(routine["watch"])
#routine is a class of dictn where dict is a inbuilt class
#type_5

for i in empdetails:
    if i == "rakesh" :
        print(i)
for i in routine.keys():
    print(i)
for i in routine.values():
    print(i)
#keys and values are the objets that acess all the variabels and data in dict
#type_6
dbase = [{"name":"raja","dept":"cse","sec":"a","age":20},
         {"name":"babu","dept":"eee","sec":"b","age":20},
         {"name":"babu","dept":"eee","sec":"b","age":20}]
print(dbase[0],dbase[1],dbase[2])

for i in dbase:
    if i["name"] == "babu":
        print("babu")
for i in dbase:
    if i["sec"] == "b":
        print("in b clas")
        
#type_7

office = [{"intern":[{"name":"raja"},{"dept":"cse"},{"sec":"a"},{"age":20}]},
           {"emp":[{"name":"babu"},{"dept":"bca"},{"sec":"b"},{"age":22}]}
            ]
#print(office[0],["intern",[0]])
for i in office:
    for j in i.values():
        for k in j:
            
            print(j,k)
            
            
