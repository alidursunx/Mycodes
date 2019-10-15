#!/usr/bin/env python
# coding: utf-8

# In[2]:


def welcome():
    print('Welcome')
    print('Would you like play HANGMAN\nPress 1 to start Press 2 Exit ')
    start_choice=input('Your choice:')
    if start_choice == '2':
        return()
    else:
        user_name=input('What is Your Name')
        print(f'Welcome to the game {user_name} ')
        gost()
    


# In[3]:


def wordget():
    import random
    worden=['amsterdam','deeploi','mehmet','ali','nazmi','eindhoven','netherland','turkiye','babamsagolsun','asylum']
    num_word=len(worden)
    random.shuffle(worden)
    word_i=random.randint(0,num_word-1)
    choice=worden[word_i]
    return choice


# In[8]:


def gost():
    gu_num=0
    gus_true=0
    count_two=0
    count_three=0
    choice=wordget()
    print(choice)
    len_c=len(choice)
    print(len_c)
    word_current=list(len_c*'_')
    print(word_current)
       
    while gu_num < 7:
        guess_let=input('PRESS A LETTER')
        guess_let.lower()
        count_three=0
        while count_three < len_c:
            count_two=0
            if guess_let == choice[count_three]:
                word_current[count_three]=guess_let
                gus_true+=1
                count_two+=1
                count_three+=1
            else:
                count_three+=1
        print(word_current)
        if gus_true == len_c:
            break
        if count_two == 0:
            gu_num+=1
                
    if gus_true == len_c:           
        
        print('PERFECT')
        print('CONGRAGULATIONS')
        
    else:
        print('LOST')
    
    rpt=input('Would like to play again Press 9')
    if rpt == '9':
        hangman()
    else:
        return()
           
    
        
    


# In[6]:


def hangman():
    welcome()
    
    
    
    


# In[ ]:


hangman()


# In[ ]:




