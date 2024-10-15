Write a program to get the tuple elements and print it.
Sample Input:
3
20
10
30
Sample Output:
(20, 10, 30)
Ans:

lst=[]
n=int(input())
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(tuple(lst))
