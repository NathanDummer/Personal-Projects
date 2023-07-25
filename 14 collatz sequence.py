import time
start = time.time()
mem = {1:1,2:2}

def addToMem(lst,num=0):
    for i in range(len(lst)-1,-1,-1):
        mem[lst[i]] = len(lst) - i + num
        
def getSeq(num):
    count = 0
    lst = []
    while num != 1:
        lst = lst + [num]

        if num in mem:
            count = mem[num]
            lst = lst[:len(lst)-1]
            break
        if num % 2 == 0:
            num = num // 2    
        else:
            num = num * 3 + 1

    addToMem(lst,count)
    
max=0
num = 0
for i in range(0,1000000,2):
    getSeq(i+1)
    if mem[i+1] > max:
        num = i+1
        max = mem[i+1]

print("Answer:", num)
end = time.time()
print("Time:", round(end-start,4),"s")


        
    


    
