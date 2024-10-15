'''
Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
'''
def count_tuple_elements(tup):
    return len(tup)

# Main function to take input and display output
def main():
    # Input the elements separated by spaces
    elements = input("Enter the elements separated by space: ")
    
    # Convert the input string into a tuple
    tup = tuple(map(int, elements.split()))
    
    # Count the number of elements in the tuple
    count = count_tuple_elements(tup)
    
    # Print the result
    print(count)

# Run the program
if __name__ == "__main__":
    main()
