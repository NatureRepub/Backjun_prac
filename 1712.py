problum = input()
x = []
x = problum.split(" ")

A = int(x[0])
B = int(x[1])
C = int(x[2])

if C > B:
    answer = A / (C - B) 
    print(int(answer)+1)   
elif C <= B:
    print(-1)
