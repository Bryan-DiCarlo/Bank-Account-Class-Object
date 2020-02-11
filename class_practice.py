# -*- coding: utf-8 -*-
#"""
#Spyder Editor
#
#This is a temporary script file.
#"""

class BankAccount(object):
    """ Bank Account Class that will track deposits and withdrawals"""
    
    def __init__(self,balance=0.0):
        self.balance = balance
        
    def display_balance(self):
        print(f'Your balance is {self.balance}')
        
    def make_deposit(self):
        amount = float(input('How much would you like to deposit?:> '))
        self.balance += amount
        print(f'Balance is now {self.balance}')
    
    def make_withdrawal(self):
        amount = float(input('How much would you like to withdraw?:> '))
        if amount > self.balance:
            print(f'You have insufficient funds, your balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Successful, your new balance is {self.balance}')
            
            