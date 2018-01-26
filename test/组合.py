class OldboyPeople:
    school = 'Oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def tell_info(self):
        print('<名字:%s 年龄:%s 性别:%s>' % (self.name, self.age, self.sex))


class OldboyStudent(OldboyPeople):
    def __init__(self, name, age, sex, course, stu_id,):
        OldboyPeople.__init__(self, name, age, sex)
        self.course = course
        self.stu_id = stu_id

    def learn(self):
        print('%s is learning' % self.name)

    def tell_info(self):
        print('我是学生：', end='')
        # self.tell_info() #stu1.tell_info()
        OldboyPeople.tell_info(self)

class OldboyTeacher(OldboyPeople):
    def __init__(self, name, age, sex, level, salary):
        OldboyPeople.__init__(self, name, age, sex)
        self.level = level
        self.salary = salary

    def teach(self):
        print('%s is teaching' % self.name)

    def tell_info(self):
        print('我是老师：', end='')
        OldboyPeople.tell_info(self)

class Date:
    def __init__(self,year,mon,day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell_birth(self):
        print('出生日期是:<%s-%s-%s>' % (self.year, self.mon, self.day))

stu1 = OldboyStudent('牛榴弹', 18, 'male', 'Python', 1,)
date_obj1=Date(1983, 3, 11)
stu1.birth=date_obj1


teacher1 = OldboyTeacher('啊狗', 18, 'female', 10, 4000)
date_obj2=Date( 1990, 2, 17)
teacher1.birth=date_obj2


# print(stu1.birth)
# print(teacher1.birth)

stu1.birth.tell_birth() #date_obj1.tell_birth()
teacher1.birth.tell_birth()