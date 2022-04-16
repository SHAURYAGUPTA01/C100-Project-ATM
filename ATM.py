class ATM(object):
    def __init__(self,CN,PN,Amount):
        self.CN=CN
        self.PN=PN
        self.Amount=Amount
    
    def CashWithdrawl(self,Amount):
        if(Amount>=100000):
            print("Amount Withdrawled")
        else:
            print("Amount is too high")
    
    def CashDeposit(self,Amount):
        if(Amount>=100000):
            print("Amount deposited")
        else:
            print("Amount is too high")
        

def main():
    CN = input("Enter Your Card Number :")
    PN = input("Enter Your Pin Number :")
    CWorCD = input("CashWithdrawl or CashDeposit :")
    Amount = input("Enter Your Amount :")
    if(CWorCD == "CashWithdrawl"):
        atm.CashWithdrawl()
    elif(CWorCD == "CashDeposit"):
        atm.CashDeposit()
        
if(__name__== "__main__"):
    main()
