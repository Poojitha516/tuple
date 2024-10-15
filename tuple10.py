'''
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
'''
# Function to calculate the factorial of a number
def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Main function to take input and display output
def main():
    # Input the tuple elements in a single line
    values = input("Enter the tuple values separated by space: ")
    
    # Convert the input string into a tuple of integers
    tup = tuple(map(int, values.split()))
    
    # Input the value to count
    x = int(input("Enter the number to count: "))
    
    # Count the occurrences of x in the tuple
    count = tup.count(x)
    
    # Calculate the factorial of the count
    factorial_value = calculate_factorial(count)
    
    # Print the result
    print(factorial_value)

# Run the program
if __name__ == "__main__":
    main()
