class person:
    def __init__(self, name='anonymous'):
        self.name = name
    def report(self):
        #print(list(attr for attr in dir(self) if not attr.startswith('__')))
        print(type(self), self.__dict__)

class girl(person):
    def __init__(self, name='anonymous', measurements='0-0-0'):
        super().__init__(name)
        self.measurements=measurements

class hottie(girl):
    def __init__(self, name, bestFeature):
        super().__init__(name)
        self.bestFeature = bestFeature

girl0 = person(name='random')
girlA = girl(name='ann', measurements='40-34-40')
girlB = girl(name='betty', measurements='36-24-36')
girlC = girl(name='candace')
girlD = hottie(name='darice', bestFeature='face')

girl0.report()
girlA.report()
girlB.report()
girlC.report()
girlD.report()

import sys
print(sys.maxsize, type(1/99), type(31474836471323456789432), type(4147483647))