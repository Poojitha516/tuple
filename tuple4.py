'''
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
Sample Input:
3
10
20
30
Sample Output:
60
'''
def main():
    # Input the number of elements
    n = int(input("Enter the number of elements: "))
    
    # Initialize an empty list to store elements
    elements = []
    
    # Get n elements from the user
    print("Enter the elements:")
    for _ in range(n):
        elements.append(int(input()))
    
    # Convert the list to a tuple
    tup = tuple(elements)
    
    # Calculate the sum of the tuple elements using the sum() function
    total_sum = sum(tup)
    
    # Print the result
    print(total_sum)

# Run the program
if __name__ == "__main__":
    main()
