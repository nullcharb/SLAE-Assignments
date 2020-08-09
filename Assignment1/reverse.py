import sys
# str1 = "Hello World!"
if len(sys.argv) <= 1:
    print("Argument not found!")
    sys.exit()

str1 = sys.argv[1]

print(f"Length for string {str1} == {str(len(str1))}")

reverse_str1 = str1[::-1]
reverse_hex = str1[::-1].encode().hex()

print(f"Reverse hex is {reverse_hex}")


for i in range(0,len(reverse_hex)-1,8):
    print(f"{reverse_str1[(i//2):(i//2)+4]}:{reverse_hex[i:i+8]}")
