# String indexing means accessing individual characters of a string using their position (index).
# string_name[start : end : step]

# str[i]  single character
# str[-i]  from end
# str[a:b]  slice
# str[a:b:c]  slice with step

cc_number = "1234-0987-45678-5678"

# print(cc_number[0])
# print(cc_number[0:4])
# print(cc_number[5:9])
# print(cc_number[5:])
# print(cc_number[-1])  # last digit
# print(cc_number[-4:]) # last 4 digit
# print(cc_number[-4:-1])

print(cc_number[: : 2])