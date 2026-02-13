"""
LeetCode 2043: Simple Bank System
=================================
Topic: Design / Simulation / Array / Hash Map
Difficulty: Medium
Company: Capital One (Highly Reported)

Problem:
You have been tasked with writing a program for a popular bank that will automate its banking operations.
All accounts are numbered from 1 to n. The initial balance of each account is given.

Implement the Bank class:
1. Bank(long[] balance): Initializes the object with the 0-indexed integer array balance.
2. boolean transfer(int account1, int account2, long money): Transfers money from account1 to account2.
3. boolean deposit(int account, long money): Deposits money to account.
4. boolean withdraw(int account, long money): Withdraws money from account.

Rules:
- Accounts are 1-indexed (input arrays are usually 0-indexed, so handle offset).
- Return true if the transaction is successful, false otherwise.
- A transaction is invalid if:
  - Account number is out of bounds.
  - Insufficient funds for withdrawal/transfer.

Ref: https://leetcode.com/problems/simple-bank-system/
"""

from typing import List

class Bank:
    def __init__(self, balance: List[int]):
        # The input 'balance' is 0-indexed (account 1 is at index 0).
        # We can store it directly. We'll handle the 1-based index conversion in methods.
        self.balance = balance
        self.n = len(balance)

    def _is_valid(self, account: int) -> bool:
        """Helper to check if account exists (1-based index)."""
        return 1 <= account <= self.n

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # Check both accounts exist
        if not (self._is_valid(account1) and self._is_valid(account2)):
            return False
        
        # Check sufficient funds (convert 1-based account to 0-based index)
        idx1, idx2 = account1 - 1, account2 - 1
        
        if self.balance[idx1] < money:
            return False
        
        # Perform Transfer
        self.balance[idx1] -= money
        self.balance[idx2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._is_valid(account):
            return False
        
        # Perform Deposit
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._is_valid(account):
            return False
        
        idx = account - 1
        if self.balance[idx] < money:
            return False
        
        # Perform Withdrawal
        self.balance[idx] -= money
        return True

# ==========================================
# TEST HARNESS
# ==========================================
if __name__ == "__main__":
    print("--- Testing Bank System ---")
    
    # Initialize Bank with balances for accounts 1, 2, 3, 4, 5
    # Account 1: 10, Account 2: 100, ...
    initial_balances = [10, 100, 20, 50, 30]
    bank = Bank(initial_balances)
    print(f"Initial Balances: {initial_balances}")

    # Case 1: Valid Withdraw
    # Withdraw 20 from Account 2 (Balance 100 -> 80)
    print(f"Withdraw(2, 20) -> {bank.withdraw(2, 20)} (Expected: True)")

    # Case 2: Insufficient Funds
    # Transfer 20 from Account 1 (Balance 10) to Account 3
    print(f"Transfer(1, 3, 20) -> {bank.transfer(1, 3, 20)} (Expected: False)")

    # Case 3: Valid Deposit
    # Deposit 20 to Account 5 (Balance 30 -> 50)
    print(f"Deposit(5, 20) -> {bank.deposit(5, 20)} (Expected: True)")

    # Case 4: Invalid Account
    # Withdraw from Account 99
    print(f"Withdraw(99, 10) -> {bank.withdraw(99, 10)} (Expected: False)")

    # Final State Check
    print(f"Final Balances: {bank.balance}")
    # Expected: [10, 80, 20, 50, 50]
    assert bank.balance == [10, 80, 20, 50, 50]
    print("✅ All Tests Passed!")
