class Oldboypeople:
    school = 'oldboy'
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
    def tell(self):
        print('我是学生',end='')
        print('我的名字是:%s我的性别是:%s我的年龄是:%s'%(self.name,self.sex,self.age))

class Student(Oldboypeople):
    def learn(self):
        print('%s is learning !' %self.name)

class Teacher(Oldboypeople):
    def teach(self):
        print('%s is teaching !' %self.name)
    def tell(self):
        print('我是老师',end='')
        print('子类的tell')

s1=Student('张铁蛋','男',18)
t1=Teacher('egon','男',38)
s1.tell()
t1.tell()