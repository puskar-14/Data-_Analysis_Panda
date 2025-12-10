import numpy as np

# Function to take matrix input from user
def input_matrix(name):
    print(f"\nEnter number of rows for {name}: ", end="")
    rows = int(input())
    print(f"Enter number of columns for {name}: ", end="")
    cols = int(input())

    print(f"\nEnter elements row-wise for {name}:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"Please enter exactly {cols} elements!")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


# Display menu
def menu():
    print("\n========== MATRIX OPERATIONS TOOL ==========")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Transpose of Matrix")
    print("5. Determinant of Matrix")
    print("6. Exit")
    print("============================================")

# Main program
while True:
    menu()
    choice = input("Enter your choice: ")

    # Addition
    if choice == '1':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            print("\nResult of A + B:")
            print(A + B)
        else:
            print("\nError: Matrices must have same shape for addition.")

    # Subtraction
    elif choice == '2':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape == B.shape:
            print("\nResult of A - B:")
            print(A - B)
        else:
            print("\nError: Matrices must have same shape for subtraction.")

    # Multiplication
    elif choice == '3':
        A = input_matrix("Matrix A")
        B = input_matrix("Matrix B")
        if A.shape[1] == B.shape[0]:
            print("\nResult of A × B:")
            print(np.dot(A, B))
        else:
            print("\nError: Columns of A must equal rows of B for multiplication.")

    # Transpose
    elif choice == '4':
        A = input_matrix("Matrix")
        print("\nTranspose of Matrix:")
        print(A.T)

    # Determinant
    elif choice == '5':
        A = input_matrix("Matrix")
        if A.shape[0] == A.shape[1]:
            print("\nDeterminant of Matrix:")
            print(np.linalg.det(A))
        else:
            print("\nError: Determinant can only be calculated for square matrices.")

    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
