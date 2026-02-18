import datetime


class User:
    def __init__(self,userid: int,name: str,email: str,phune_number: int,password: int,monthly_income: float):
        self.userid = userid
        self.name = name
        self.email = email
        self.phune_number = phune_number
        self._password = password
        self.monthly_income = monthly_income
        
    def addusertodatabase(self,DatabaseManeger):
           DatabaseManeger.create_user(self.userid,self.name,self.email,
                                       self.phune_number,self._password,self.monthly_income)
           return f'User {self.name} Successfuly Added'
    
class Wallet:
    def __init__(self,userid,wallet_id: int ,wallet_name: str, wallet_type: str,current_balance: float):
        self.userid = userid
        self.wallet_id = wallet_id
        self.wallet_name = wallet_name
        self.wallet_type = wallet_type
        self.current_balance = current_balance
        
    def addwallettodatabase(self,DatabaseManeger):
           DatabaseManeger.create_wallet(self.userid,self.wallet_id,self.wallet_name,self.wallet_type,
                                       self.current_balance)
           return f'Wallet {self.wallet_name} Successfuly Added'
       
    def update_balance(self,DatabaseManeger,new_balance,wallet_id):
        
        DatabaseManeger.update_wallet(new_balance,wallet_id)
        return f'Wallet Ballance Successfuly Updated'
    
class Transaction:
    def __init__(self,transaction_id: int ,transaction_name: str, transaction_date: int,
                           transaction_amount: float,transaction_type: str,transaction_category_id: int,
                           transaction_description: str = None):
        self.transaction_id = transaction_id
        self.transaction_name = transaction_name
        self.transaction_date = transaction_date
        self.transaction_amount = transaction_amount
        self.transaction_type = transaction_type
        self.transaction_description = transaction_description
        self.transaction_category_id = transaction_category_id
        
    def addTransaction(self,wallet_id,DatabaseManeger):
        DatabaseManeger.create_transaction(wallet_id = wallet_id,transaction_id=self.transaction_id,
                                           transaction_name=self.transaction_name,
                                           transaction_date = self.transaction_date,
                                           transaction_amount = self.transaction_amount,
                                           transaction_type = self.transaction_type,
                                           transaction_description = self.transaction_description,
                                           transaction_category_id = self.transaction_category_id)
        if self.transaction_type == 'Income':
            pass
        elif self.transaction_type == 'Expense':
            DatabaseManeger.update_budget(self.transaction_category_id,self.transaction_amount)
            DatabaseManeger.update_wallet(self.transaction_amount,wallet_id)
        
    
    def editTransaction(self):
        pass
    
    def deleteTransaction(self):
        pass

class Category:
    def __init__(self,category_id: int ,category_name: str,
                 category_type: str,
                 category_color: str = None,category_icon: str = None):
        self.category_id = category_id
        self.category_name = category_name
        self.category_type = category_type
        self.category_color = category_color
        self.category_icon = category_icon
        
    def addcategory(self,userid,DatabaseManeger):
        if DatabaseManeger.create_category(userid=userid,category_id=self.category_id,
                                        category_name=self.category_name,category_type = self.category_type,
                                        category_color = self.category_color,
                                        category_icon = self.category_icon):
            return True
        else:
            return False

class Budget:
    def __init__(self,budget_id: int , start_date: int,end_date: int,
                           limit_amount: float,remaining_amount: float):
        self.budget_id = budget_id
        self.start_date = start_date
        self.end_date = end_date
        self.limit_amount = limit_amount
        self.remaining_amount = remaining_amount
    
    def addbudget(self,category_id,DatabaseManeger):
        DatabaseManeger.create_budget(category_id = category_id,budget_id  = self.budget_id,
                                      start_date = self.start_date,end_date= self.end_date,
                                      limit_amount = self.limit_amount,
                                      remaining_amount = self.remaining_amount)
        return f'budget {self.budget_id} Successfuly Added'
        