'''
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
'''
# Function to calculate the sum of elements in a tuple
def calculate_sum(tup):
    total = 0
    for element in tup:
        total += element
    return total

# Main function to take input and display output
def main():
    # Input the tuple elements in a single line
    values = input("Enter the tuple elements separated by space: ")
    
    # Convert the input string into a tuple of integers
    tup = tuple(map(int, values.split()))
    
    # Calculate the sum of the elements in the tuple
    total_sum = calculate_sum(tup)
    
    # Print the result
    print(total_sum)

# Run the program
if __name__ == "__main__":
    main()
