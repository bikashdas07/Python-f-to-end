def Deposite():
    amount=int(input('Enter ther amount: '))
    if 500 <= amount <=10000 and amount % 100 ==0 :
        bal += amount
        print('Deposited successfully:', bal)
    else:
        print('Invalid amount: ')    
    