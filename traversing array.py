# Initializing a 2D array (list of lists)
two_dim_array = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Function to traversing and print the elements of a 2D array
def travers_2dim_array(array):
    print("Traversing the 2D array:")
    for r in range(len(array)): 
        for jt in range(len(array[r])):  
            print(array[r][jt], end=' ')
        print()  # New line after each row
# Call the function to traversing the 2D array

travers_2dim_array(two_dim_array)