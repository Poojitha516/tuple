'''
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
Sample Input:
3
20
10
30
Sample Output:
30
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
    
    # Find the maximum value in the tuple using the max() function
    max_value = max(tup)
    
    # Print the result
    print(max_value)

# Run the program
if __name__ == "__main__":
    main()
