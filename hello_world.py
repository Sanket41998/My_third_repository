a=20
b=10
c=a+b
print(c)

a=20
b=10
c=a-b
print(c)

class India:
    def capital(self):
        print("new delhi is capital of India")
    def language(self):
        print("hindi is spoken widely")
class USA:
    def capital(self):
        print("Washigton DC is the capital of USA")
    def language(self):
        print("English is spoken widely")
obj1=India()
obj2=USA()
for i in (obj1,obj2):
    i.capital()
    i.language()