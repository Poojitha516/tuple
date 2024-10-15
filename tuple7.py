'''
Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
'''
# Main function to take input and display output
def main():
    # Input the tuple values in a single line
    values = input("Enter the tuple values separated by space: ")
    
    # Convert the input string into a tuple of integers
    tup = tuple(map(int, values.split()))
    
    # Input the value to count
    x = int(input("Enter the value to count: "))
    
    # Count the occurrences of x in the tuple
    count = tup.count(x)
    
    # Print the result
    print(count)

# Run the program
if __name__ == "__main__":
    main()
