#yeild keyword 
def joy(happy):
    if happy == "positive":
        print("smiling face")
    elif happy == "worried":
        print("unhappy face")
    yield"disys"
    print("live long life")

#getting n number of argumwnts using *arg and **args values and keys in dict
def running (**args):
    for i in args:
        print(i) 

#decorator is nothing but callin function using other function
#closure
'''def c():
    print("we are coder")
    def cpp():
        print("escaped")
    return cpp
ret = c()
ret.cpp'''
'''class hacker:
    def __init__(self,d):
        self.__website = "flipkart"
        self.__data = d
    def theft(self):
        print(self.__data)
    def __add__(self,j):
        pass
user = hacker([{"name":"Akash","acc no":"100"},{"name":"Ahmed","acc no":"800"}])
user.self.__
data()
user1 = hacker([{"name":"Akash","acc no":"100"},{"name":"Ahmed","acc no":"800"}])
user1+user
#using asyncio and coruitine managing threads'''
import asyncio
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")
asyncio.run(main())
#acessing class obj in function

class java:
    jvt =  "coder's"
    @staticmethod
    def freeclass():
        print("free java class",java.jvt)
java.freeclass()
#
class opera:
    def __init__(self)
        self.a=1
    def __add__(self,r)
        print("result")
        return self.a+r.a
    def __sub__(self,r)
        print("result")
        return self.a-r.a
a=opera()
b=opera()
c=a+b
        
        
