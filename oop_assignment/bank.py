class BankAccount:
    def __init__(self,name,age,phone_number):
        acccountnumber = 3175710023
        self.name = name
        self.age  = age
        self.phone_number = Phone_number
        self.account_number = acccountnumber
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("insuffient balance")
        else:
            self.balance-=amount
    
    def __str__(self):
        return("{}\n{}\n{}\n{}\n",self.name,self.age,self.acccount_number,self.balance)
    









"""
class AccountHolder:
    def __init__(self,name,addres,mobile_no):
        self.name = name
        self.addres = addres
        self.mobile_no = mobile_no
        self.banck_accounts = []
        
    def associate_bank_account(self,account):
        self.bank_account.append(account)
        
class BankAccount:
    withdraw_limit = 1000
    def __init__(self,account_number):
        self.account_number = account_number
        self.__balance = 0
        self.__amount_withdraw = 0
    

a=AccountHolder('vineel','kottom clg \n chinnatekur','mobile_no')

print(a.name,a.addres,a.mobile_no,sep='\n')

b= BankAccount('8099914796')

'''
class a:
    def __init__(self,name):
        self.name = name
        self.addres = 'addres'
        
        
        
class b(a):
    pass


c=a('k')
#d=b('o')
d=b('k')


print(isinstance(d,b))
print(issubclass(a,b))
"""
