'''print("Program Started!")
char = input("Please enter a standard character ")
if len(char) == 1:
    val = ord(char)
    print(f"The ASCII value of the character {char} is {val}")
else:
    print("Error: wrong length")
print("Program Ended!")
'''

val = input("Please enter an ASCII code: ")
val = abs(int(val))
if val in range(32, 126):
    char = chr(val)
    print(f"The character represented by the ASCII code {val} is {char}")
