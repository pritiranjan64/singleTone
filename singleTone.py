def singleTon(arg):
    d={}
    def inner():
        if arg not in d:
            multiplexobject=arg()
            d[arg]=multiplexobject
        return d[arg]
    return inner
@singleTon
class Multiplex:
    def __init__(self):
        self.ticlets=300

    def booking(self,n):
        if self.ticlets>=n:
            self.ticlets-=n
            print(f'booking of {n} tickets is done')
            print('remaining tickets are',self.ticlets)
        else:
            print('in sufficent tickets')
harshad=Multiplex()
harshad.booking(100)
print(harshad)

kanha=Multiplex()
kanha.booking(100)
print(kanha)

happy=Multiplex()
happy.booking(102)
print(happy)       

