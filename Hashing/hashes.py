import hashlib
from itertools import product
from string import ascii_lowercase
import time

HASH_TO_FIND = "aed629fdafd6813b2a27c4f52a375bc721b138c7f6d5609d45f31212a99054f6cabe9b1b007f2d74f75b634c6cfa98453c5154312bb95b692f05e99e3b13bc89"
keywords = [''.join(i) for i in product(ascii_lowercase, repeat=5)]
md5_lists = []
sha256_list = []
start_time = time.asctime(time.localtime(time.time()))
print(start_time)

# keywords = ['aaaaa']

for word in keywords:
    str2hash = word
    for i in range(100):
        for j in range(100):
            for k in range(100):
                str2hash = hashlib.md5(str2hash.encode())
                str2hash = str2hash.hexdigest()
            str2hash = hashlib.sha256(str2hash.encode())
            str2hash = str2hash.hexdigest()
        str2hash = hashlib.sha512(str2hash.encode())
        str2hash = str2hash.hexdigest()
    if str2hash == HASH_TO_FIND:
        print(word)
        print(HASH_TO_FIND)
        print(str2hash)
        break
    



end_time = time.asctime(time.localtime(time.time()))
print("finished", end_time)
