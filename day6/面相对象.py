class Student:
    school='oldboy'
    count=0
    def __init__(self,name,sex,age):
        self.name=name
        self.age=age
        self.sex=sex
        Student.count+=1
        self.pcount=Student.count

    def learn(self,x,y):
        print('%s is learning ! '%self.name)
        print(x,y)

    def chiocecourse(self):
        print('is chioce course !')

stu1=Student('张铁蛋','男',18)
print(stu1.count)
stu2=Student('李铁柱','男',28)
print(stu2.count)
stu3=Student('张二狗','女',38)
print(stu3.count)

print(stu1.pcount)
print(stu2.pcount)
print(stu3.pcount)