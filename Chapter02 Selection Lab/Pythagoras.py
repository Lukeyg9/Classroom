print("Pythagoras’ Calculator \n 1. Find the length of A given B and C \n 2. Find the length of B given A and C \n 3. Find the length of C given A and B")

length = int(input("Enter 1, 2 or 3. 1 will calculate adjecent side, 2 will calculate Opposite side and 3 wil calculate Hypotenuse"))

if length == 1:
    B_length = float(input("Length of side B?"))
    C_length = float(input("Length of side C?"))
    print(f"The length of side A is {(C_length**2 - B_length**2)**0.5}")
if length == 2:
    A_length = float(input("Length of side A?"))
    C_length = float(input("Length of side C?"))
    print(f"The length of side B is {(C_length**2 - A_length**2)**0.5}")
if length == 3:
    A_length = float(input("Length of side A?"))
    B_length = float(input("Length of side B?"))
    print(f"The length of side C is {(A_length**2 + B_length**2)**0.5}")

print("Done!")
