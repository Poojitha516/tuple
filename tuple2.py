'''
Write a program to get the elements of tuple in a single line separated by space and print the tuple values.
Sample Input:
20 10 30
Sample Output:
20, 10, 30
'''
Ans 
a=map(int,input().split())
b=tuple(a)
print(b)
