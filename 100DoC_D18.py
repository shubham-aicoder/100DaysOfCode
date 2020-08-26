M=int(input())
s1=set(list(map(int,input().split(' '))))
N=int(input())
s2=set(list(map(int,input().split(' '))))

res=sorted(list(set.union(s1-s2,s2-s1)))
for i in res:
    print(i)
