#import testModule
#print(dir())
#print(dir(testModule))
##DOES NOT WORK
##testModule.testFunc.doThing()

#from testModule import testFunc
#print(dir())
#testFunc.doThing()
#
#import testModule.testFunc as blah
#print(dir())
#blah.doThing()

from testModule.testFunc import doThing
print(dir())
doThing()
