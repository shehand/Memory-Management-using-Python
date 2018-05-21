#python version 3.3
#The main interface to eun the programme
from MemNode import *
from MemManage import *

begin = """

                ##################################################
                ##################################################
                ##               !!! WELCOME!!!                 ##
                ##                                              ##
                ##             First Fit Algorithm              ##
                ##################################################
                ##################################################



                INSTRUCTIONS :

                For Allocating ==              For Terminating ==

                    >>> A                          >>> T
                    >>> Process ID                 >>> Process ID            
                    >>> <Memory Size>                              

                For Snapshots ==               For Exit ==

                    >>> Show                       >>> Exit
"""

extra = """
For Allocating,
Use  'A'

For Terminating
Use 'T'

For Snapshots
Use 'Show'

For Exit
Use 'Exit'
"""
print(begin)

mem_os = int(input('Enter the OS Memory : '))
mem_total = int(input('Enter the Total Memory : '))
m = MemManage(mem_os,mem_total)
print('Main Memory has been crated !\n')

while True:
    com = input("Enter the Command : ")

    if com == 'A':
        p_id = input('Enter the Process ID to Allocate : ')
        val = input('Enter the Memory Size : ')
        m.allocating_memory(int(val),p_id)
    elif com == 'T':
        p_id = input('Enter the Process ID to Terminate : ')
        m.terminating_memory(p_id)
    elif com == 'Show':
        m.printMem()
    elif com == 'Exit':
        print('Bye !!!')
        break
    else:
        print('Invalid Command.Please read the instructions : \n',extra)



    

