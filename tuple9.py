'''
Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
'''
# Function to count even and odd numbers
def count_even_odd(values):
    even_count = 0
    odd_count = 0
    
    for value in values:
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
            
    return even_count, odd_count

# Main function to take input and display output
def main():
    # Input the values in a single line
    values = input("Enter the numbers separated by space: ")
    
    # Convert the input string into a list of integers
    numbers = list(map(int, values.split()))
    
    # Count even and odd numbers
    even_count, odd_count = count_even_odd(numbers)
    
    # Determine and print the result
    if even_count > odd_count:
        print("Even")
    elif odd_count > even_count:
        print("Odd")
    else:
        print("Equal")

# Run the program
if __name__ == "__main__":
    main()
