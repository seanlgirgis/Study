from typing import List

class Bank:

    def __init__(self, _balance: List[int]):
        """  Initialize bank state  """
        self.balance =  _balance
        self.n = len(self.balance)
        pass
    
    def account_exist(self, account: int)->bool:
        """ account number has to be between 1 and self.n"""
        if account >= 1 and account <= self.n : return True
        return False
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.account_exist(account1 ) and self.account_exist(account2 ) and self.balance[account1 -  1] > money:
            self.balance[account1-1] -= money
            self.balance[account2-1] += money
        # TODO: Implement transfer logic
        # Remember: accounts are 1-indexed
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.account_exist(account):
            self.balance[account-1] > money:
            self.balance[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.account_exist(account) and self.balance[account - 1] > money:
            self.balance[account-1] -= money
            return True
        return False


# ------------------------------------------------------------------
# Test Harness
# ------------------------------------------------------------------
def run_tests():
    print("Running Bank System Tests...\n")
    
    # Example 1
    bank = Bank([10, 100, 20, 50, 30])
    
    # Test 1: valid withdraw
    # account 3 has 20. Withdraw 10 -> remaining 10. Expected True.
    res1 = bank.withdraw(3, 10)
    print(f"Test 1 (withdraw 10 from acc 3 [bal 20]): Expected True, Got {res1}")
    
    # Test 2: valid transfer
    # transfer 20 from acc 5 (bal 30) to acc 1 (bal 10). 
    # acc 5 becomes 10, acc 1 becomes 30. Expected True.
    res2 = bank.transfer(5, 1, 20)
    print(f"Test 2 (transfer 20 from acc 5 to acc 1): Expected True, Got {res2}")
    
    # Test 3: valid deposit
    # deposit 20 to acc 5 (now 10). Becomes 30. Expected True.
    res3 = bank.deposit(5, 20)
    print(f"Test 3 (deposit 20 to acc 5): Expected True, Got {res3}")
    
    # Test 4: invalid transfer (insufficient funds)
    # acc 3 has 10 (from Test 1). Try to transfer 15 to acc 4. Expected False.
    res4 = bank.transfer(3, 4, 15)
    print(f"Test 4 (transfer 15 from acc 3 [bal 10]): Expected False, Got {res4}")
    
    # Test 5: invalid withdraw (non-existent account)
    # acc 10 does not exist. Expected False.
    res5 = bank.withdraw(10, 50)
    print(f"Test 5 (withdraw from invalid acc 10): Expected False, Got {res5}")

    # Additional Edge Cases
    print("-" * 30)
    
    # Test 6: Deposit to invalid account
    res6 = bank.deposit(99, 100)
    print(f"Test 6 (deposit to invalid acc 99): Expected False, Got {res6}")
    
    # Test 7: Transfer to invalid account
    res7 = bank.transfer(1, 99, 5)
    print(f"Test 7 (transfer to invalid acc 99): Expected False, Got {res7}")
    
    # Test 8: Transfer FROM invalid account
    res8 = bank.transfer(99, 1, 5)
    print(f"Test 8 (transfer from invalid acc 99): Expected False, Got {res8}")

    print("-" * 30)
    print(f"Bank has to have no negative amounts {bank}")
    
run_tests()
