import abc

class File(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def read(self):
        pass

    @abc.abstractclassmethod
    def wirte(self):
        pass

class Process(File):
    def read(self):
        print('read')

    def wirte(self):
        print('wirte')



s1=Process()

s1.wirte()