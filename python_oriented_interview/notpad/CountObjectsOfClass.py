class ObjCount:
    count=0
    def __init__(self):
        ObjCount.count+=1
    
obj1=ObjCount()
obj2=ObjCount()
obj3=ObjCount()
obj4=ObjCount()
obj5=ObjCount()

print(ObjCount.count)