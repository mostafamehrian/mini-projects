from tinydb import TinyDB,Query


class DatabaseManeger:
    query = Query()
    def __init__(self):
        self.db = TinyDB('/home/mosi/projectbasedpython/projects/hesabdari/databse.json')
        
        self.user = self.db.table('User')
        self.wallet = self.db.table('wallet')
        self.category = self.db.table('category')
        self.transaction = self.db.table('transaction')
        self.budget = self.db.table('budget')

    def get_all(self, table):
        return table.all()
      
    def create_user(self,userid: int ,name: str, email: str,phune_number: int,password: int,monthly_income: float = None):
        self.user.insert({'userid':userid,'name':name,'email':email,
                          'phune_number':phune_number,
                          'password':password,
                          'monthly_income':monthly_income})
            
    def get_user(self):
        pass
        
    def update_user(self):
        pass
    
    def delete_user(self):
        pass
    
    
    def create_wallet(self,userid: int ,wallet_id: int ,wallet_name: str, wallet_type: str,current_balance: float):
        self.wallet.insert({'userid':userid, 'wallet_id':wallet_id,'wallet_name':wallet_name,
                          'wallet_type':wallet_type,
                          'current_balance':current_balance,})
        
    def get_wallet(self):
        pass
        
    def update_wallet(self,transaction_amount,wallet_id):
        walletexists = self.wallet.get(DatabaseManeger.query.wallet_id == wallet_id)
        current_balancefiled = 'current_balance'
        if walletexists:
            if current_balancefiled in walletexists:
                current_balance = walletexists[current_balancefiled] - transaction_amount
                data = {'current_balance':current_balance}
                self.wallet.update(data,DatabaseManeger.query.wallet_id == wallet_id)
        else:
            return False

        
    def delete_wallet(self):
        pass
    
    
    def create_category(self,userid: int,category_id: int ,category_name: str, category_type: str,category_color: str = None,category_icon: str = None):
        if self.category.insert({'userid':userid,'category_id':category_id,'category_name':category_name,
                          'category_type':category_type,
                          'category_color':category_color,
                          'category_icon':category_icon}):
            return True 
        
    def get_category(self):
        pass
        
    def update_category(self):
        pass
    
    def delete_category(self):
        pass
    
    
    def create_transaction(self,wallet_id: int,transaction_id: int ,transaction_name: str, transaction_date: int,
                           transaction_amount: float,transaction_type: str,transaction_category_id,
                           transaction_description: str = None):
        
                            self.transaction.insert({'wallet_id':wallet_id,'transaction_id':transaction_id,'transaction_name':transaction_name,
                                                'transaction_date':transaction_date,
                                                'transaction_amount':transaction_amount,
                                                'transaction_type':transaction_type,'transaction_category_id':transaction_category_id,
                                                'transaction_description':transaction_description})
        
    def get_transaction(self):
        pass
        
    def update_transaction(self):
        pass
    
    def delete_transaction(self):
        pass
    
    
    def create_budget(self,budget_id: int ,category_id: int, start_date: int,end_date: int,
                           limit_amount: float,remaining_amount: float):
        
                            self.budget.insert({'budget_id':budget_id,'category_id':category_id,
                                                'start_date':start_date,
                                                'end_date':end_date,
                                                'limit_amount':limit_amount,
                                                'remaining_amount':remaining_amount})
        
    def get_budget(self):
        pass
        
    def update_budget(self,category_id,transaction_amount):
        catexists = self.budget.get(DatabaseManeger.query.category_id == category_id)
        remaining_amountfiled = 'remaining_amount'
        if catexists:
            if remaining_amountfiled in catexists:
                remaining_amount = catexists[remaining_amountfiled] - transaction_amount
                data = {'remaining_amount':remaining_amount}
                self.budget.update(data,DatabaseManeger.query.category_id == category_id)
        else:
            return False
    
    def delete_budget(self):
        pass