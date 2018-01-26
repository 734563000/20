class People:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        return self.weight / (self.height ** 2)

egon=People('egon',18,1.80,95)
print(type(egon.bmi))