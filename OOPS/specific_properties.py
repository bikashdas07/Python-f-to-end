class Bank:
    loc='Bhubaneswar'
    bank_name='AXIS'
    ifsc='12345'
    name = 'Facebook'
    def __init__(self,name='John Doe',acc_no,ph_no,bal):
        self.name=name
        self.acc_no=acc_no
        self.ph_no=ph_no
        self.bal=bal
ob1=Bank('Dhrumketu',1234567890,9876345210,100000)
ob2=Bank('Parshuram',1234507891,9876543211,200000)
#Accessing uncommon properties of a class using object reference.
print(ob1.name, ob1.acc_no, ob1.ph_no, ob1.bal)
ob2.name = 'Kalki'
print(ob2.name, ob2.acc_no, ob2.ph_no, ob2.bal)
print(ob2)
#Using class reference we can not access uncommon properties of a class.
Bank.name='Instagram'
print(Bank.name,ob2.name)