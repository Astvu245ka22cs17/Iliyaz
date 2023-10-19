class bank_account:
  def init(self):
    self.balance=0
    print("hello!!! welcome to deposit and withdrawal machine")
  def deposit(self):
    amount= float(input("Enter amount to deposit:"))
    self.balance+= amount
    print("Amount Deposited: ", amount)
  def withdrawal (self):
    amount= float(input("Enter amount to withdraw:"))
    if self.balance>= amount:
      self.balance-=amount
      print("You withdrew",amount)
    else:
      print("Insufficient balance ")
  def display(self):
     print("Net Available Balance= ",self.balance)
s= bank_account()
s.init()
s.deposit()
s.withdrawal()
s.display()

      
