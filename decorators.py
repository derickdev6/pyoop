def calculus_presentation(calculus):
    def interior():
        print('We will do a calculation')
        calculus()
        print('That was all')
    return interior


@calculus_presentation
def sum():
    print(3+4)


@calculus_presentation
def sub():
    print(5-2)


sum()
sub()
