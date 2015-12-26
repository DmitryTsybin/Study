class Test():
    testvar = 'testvar'
    print testvar

    def __init__(self, testvar):
        self.testvar = testvar

    def printTestVar(self):
        # print testvar
        print self.testvar

test = Test('not default test var')
test.printTestVar()
