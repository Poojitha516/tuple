'''
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
'''
# Main function to take input and display output
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
    
    # Find the minimum value in the tuple using the min() function
    min_value = min(tup)
    
    # Print the result
    print(min_value)

# Run the program
if __name__ == "__main__":
    main()
