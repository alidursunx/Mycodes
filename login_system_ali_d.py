#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def logous():
    print('Welcome')
    print('please don use space,special character or symbol in username and password')
    user1=users()
    mod=input('Sign Up for press 1\nSign In Press 2\nPress 3 to exit\n')
    if mod == "1":
        
        while True: 
            input1=input('Select a username')
            user1.check(input1)
            if user1.result == 0:
                while True:
                    input2=input('Please select a password')
                    input3=input('Please retype your pasword')
                    if input2 == input3:
                        user1.register(input1,input2)
                        print('Register process is completed')
                        welcome()
                        break
                    else:
                        print('They are not same')
                break        
                
            
            else:
                print(f'{input1} is being used please change another one')
                
    
    elif mod == "2":
        
        while True:
            input4=input('USERNAME:')
            input5=input('PASSWORD:')
            user1.gate(input4,input5)
            if user1.g_result == 1:
                welcome()
                break
            else:
                print('Username or Password is wrong')
                
        

    else:
        logous()

    
class users():
    def __init__(self,username="ali",password="1234"):
        #Default variables inclued
        self.username=username
        self.password=password
    def check(self,input1,result=1):
        f= open("users.txt","r+")
        for line in f:
            (us_check,us_pas) = line.split()
            if us_check == input1:
                self.result=1
                break
            else:
                self.result=0
        f.close()
            
    def register(self,user_name,pass_word):
        self.username=user_name
        self.password=pass_word
        f=open("users.txt","a+")
        f.write("\n%s %s" %(self.username,self.password))
        f.close()
        welcome()
    def gate(self,userg_name,userg_pass,g_result=1):
        f=open("users.txt","r")
        for line in f:
            (us_check,us_pass) = line.split()
            if us_check == userg_name:
                if us_pass == userg_pass: 
                    self.g_result=1
                    break
            else:
                self.g_result=0
        f.close()
        return

def welcome():
    print('WELCOME The Homepage')  
logous()

