n=int(input())
words=[""]*n
for i in range(n):
    words[i]=input()
for i in range(n-1,-1,-1):
    print(words[i])    