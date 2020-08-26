# def decrypt(string, shift):

#     cipher = ''
#     string = string.upper()
#     for char in string:
#         if char == ' ':
#             cipher = cipher + char
#         elif char:
#             cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)

#     return cipher


# for i in range(26):
#     text = 'DWLECEJAWYDDWJZXQPNAPQNJAZEJPDAARAJEJCPKWJANHAUPDANASWOWUKQJCHWZUKBSWHAOSDKYWQCDPWHWNCABEODSEPDKQPOY'
#     print("shift number: ", i)
#     print("A = " + decrypt("A", i))
#     print("original string: ", text)
#     print("after encryption: ", decrypt(text, i))
#     print()

from string import ascii_uppercase as alphabet
X = 22
print(alphabet[X])
