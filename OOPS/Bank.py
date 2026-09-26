class Bank:
    BANK_NAME = 'HDFC'
    LOCATION = 'Bangalore'
    IFSC = 1234567890
    ROI = '0.7'
    def __init__(self,name,acc_no,ph_no,bal,pin):    #Constructor
        self.name= name
        self.acc_no =acc_no
        self.ph_no= ph_no
        self.bal= bal
        self.pin=pin
    @classmethod
    def Change_Loc(cls):    #Class method
        cls.LOCATION = 'Hogwarts'
    
    @staticmethod  #ENCAPSULATION
    def __Check_Password():   #Static Method(Private)
        __password = int(input('Enter the password : '))
        return __password
    
    
    def Check_Balance(self):    #Object/Instance Method
        count = 3
        while count>0:
            if self.__Check_Password() == self.pin :
                return f'Available balance is {self.bal}'
            else:
                count-=1
                print (f'Password Mismatch. \n Available attempt: {count}')
        else:
            return f'Attempts over \nTry after 24 - Hours'
            
        
    def Deposite(self):  #Object/Instance method
        count=3
        while count>3:
            print(f'Attempts left: {count}')
            if self.Check_Password() == self.pin:
                data = int(input('Enter account number: '))
                if self.acc_no == data:
                    amount=int(input('Enter ther amount: '))
                    if 500 <= amount <=10000 and amount % 100 ==0 :
                        self.bal += amount
                        return 'Deposited successfully:', self.bal
                    else:
                        print('Invalid amount.')
                else:
                    return 'Invalid Account Number.'
            else:
                print('Password Mismatch.')
                count-=1
        else: 
            return f'Attempts over \nTry after 24 - Hours'        
            
        
    def With_Drawn(self):   #Object/Instance method
        count = 3
        while count>0:
            print('Attempts left: {count}')
            if self.Check_Password() == self.pin:
                amount=int(input('Enter the amount: '))
                if 100 <= amount <=20000 and self.bal >= amount:
                    self.bal -= amount
                    print('With Drawn successfully:', self.bal)
                else:
                    return 'Insufficient Balance.'
            else:
                print('Password Mismatch.')
                count-=1
        else: 
            return f'Attempts over \nTry after 24 - Hours'
            
harry = Bank('Harry',1234567890,9876543210,500000,111)
ron = Bank('Ron',1234507891,9876543211,-465,222)
hermione = Bank('Hermione',1234507892,9876543212,800000,333)
#ginny = Bank('Ginny',1234507893,9876543213,100000,444)
#neville = Bank('Neville',1234507894,9876543214,200000,555)
#print(harry.Check_Balance())
#print(harry._Bank__Check_Password())#Acccessing private method outside the class