#!/usr/bin/env python
# coding: utf-8

# In[ ]:



tasks={}
task_new={}
def tasking():
    choice=input('Add Item PRESS 1 \n Remove ITEM PRESS 2\n Report COMPLETED TASKS PRESS 3\n Report UNCOMPLETED TASKS PRESS 4\n EDIT TASKS PRESS 5\ SHOW CURRENT PRESS 6 ')
    if choice == '1':
        add_remove(1)
    elif choice == '2':
        add_remove(2)
    elif choice == '3':
        report(3)
    elif choice == 4:
        report(4)
    elif choice == 5:
        edit_tas()
    else:
        print('tasks')
    tasking()
        
def add_remove(desic):
    #Adding and removing items
    if desic == 1:
        key=input('Please task key')
        due=input('Set as a due date like this 10.12.2019 ')
        priority=input('Select priority in the range 0-5')
        situat=input('Task is complete Y or N')
        tasks[key]=[due,priority,situat]
        
    else:
        key_rem=input('Please enter the label of the task you want to delete')
        tasks.pop(key_rem)
    return

def edit_task():
    arbit1=input('Change Priority: PRESS 1\n Changeof the Situation PRESS 2')
    if arbit == '1':
        key_ar=input('Enter key label')
        new_priority=input('Enter new priority 0-5')
        tasks[key_ar][1]=new_priority
    else:
        key_ar=input('Enter key label')
        fin=input('is task finished Y/N')
        tasks[key_ar][2]=fin
    return
    
def report(mod):
    uncomp={}
    comp={}
    for key in tasks:
        if tasks[key][2] == 'N':
            uncom[key]=tasks[key]
        else:
            comp[key]=task[key]
    if mod == 3:
        print('Completed tasks')
        print(comp)
    else:
        print('Uncompleted tasks')
        print(uncom)
    return
tasking()             


# In[43]:


a={'ali':25,'omer': [45,45,34,'dene'],'taner':79}
a['deve']=456
a.pop('deve')
a


# In[38]:


b={}
b.append(a['omer'])

