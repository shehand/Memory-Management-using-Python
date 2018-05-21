from MemNode import *

class MemManage:
    #create a linked list named as 'MemManage' and create two default nodes which are 'OS Node' & 'FREE Node' and link them together
    def __init__(self,mem_os,mem_total):
        
        osNode = MemNode()
        totalNode = MemNode()
        totalNode.setSize(mem_os,mem_total)
        osNode.setSize(0,(mem_os-1))
        osNode.setProcess('OS')
        self.head = osNode
        osNode.next = totalNode
        
    #defines the allocation theorys to the class
    def allocating_memory(self, value, pID):
        curMem = self.head.next
        preMem = self.head
        exNode = self.head
        
        #check whether the process is already in the memory
        while exNode != None:
            if exNode.processID == pID:
                print("This process is already existed !!!\n")
                return
            else:
                exNode = exNode.next
                
        #allocate the process where it is mainly suitable to be allocated
        while curMem != None:
            if (curMem.hole) == True and (curMem.printSize()) >= value:
                tempNode = MemNode()
                tempNode.setSize(curMem.startAddress,curMem.startAddress+value-1)
                tempNode.setProcess(pID)
                curMem.setSize(curMem.startAddress+value, curMem.endAddress)

                #if the remaining memory is null,we have to break the connection of that node with the linked list
                if curMem.printSize() == 0:
                    if curMem.next != None:
                        tempNode.next = curMem.next
                else:
                    tempNode.next = curMem
                preMem.next = tempNode

                print("Memory Allocated Succesfully !!!\n")
                return
            else:
                preMem = curMem
                curMem = curMem.next

        print("Not Enough Memory to be Allocated !!!\n")

    #defines the terminating theorys to the class
    def terminating_memory(self, pID):
        curMem = self.head.next
        preMem = self.head

        #check whether the process is existed or not and if exsist,terminate it
        while curMem != None:
            if curMem.processID == pID:
                curMem.freeMem()
                print("Process has been Terminated !!!\n")
                break
            else:
                preMem = curMem
                curMem = curMem.next
        #defines the way to connect neccessary nodes by removing unneccessary nodes
        if curMem != None:
            if curMem.next != None:
                if curMem.next.hole == True:
                    curMem.setSize(curMem.startAddress, curMem.next.endAddress)
                    curMem.next = curMem.next.next

                if preMem.hole == True:
                    preMem.setSize(preMem.startAddress, curMem.endAddress)
                    preMem.next = curMem.next
                    curMem = preMem.next
        else:
            print("There isn't any process called ",pID,'\n')
                
    #print a snapshot of the memory
    def printMem(self):
        find = self.head
        while find != None:
            if find.hole == True:
                a = "Free"
            if find.processID == None:
                print(a,' ',find.startAddress,'K',' ',find.endAddress,'K','\n')
            else:    
                print(find.processID,' ',find.startAddress,'K',' ',find.endAddress,'K','\n')
            find = find.next

                    

                
        
