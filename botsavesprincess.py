#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    for i in range(0,n):
        arr=list(grid[i])
        mp=n//2
        if ("p" in arr):
            pp=i;
            while(pp!=mp):
                if (i>n//2):
                    mp+=1
                    print("DOWN")
                elif(i<n//2):
                    mp-=1;
                    print("UP")
            
            mp=n//2
            for j in range(len(arr)):
                if (arr[j]=="p"):
                    pp=j
                    break
            while(mp!=j):
                if (mp>j):
                    mp-=1
                    print("LEFT")
                else:
                    mp+=1
                    print("RIGHT")
                
                
                
                
    


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
