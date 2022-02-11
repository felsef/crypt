"""
Cryptography implementation for Password Manager
"""

#Encryptor Class

class Encrypt:
    def __init__(self, target, key):
        #Task - Perform XOR operation on target & key
        #============================================
        #Step 1 - Convert target & key into ordinal
        ord_tar = [ord(x) for x in target]
        ord_key = [ord(x) for x in key]
        #Step 2 - Find the longer list
        target_is_greater = False
        if len(ord_tar) > len(ord_key): 
            target_is_greater = True
        else: 
            pass
        #Step 3 - Find the difference in length
        target_length, key_length = 0, 0
        for x in ord_tar:
            target_length += 1
        for y in ord_key:
            key_length += 1
        if target_is_greater: 
            diff = target_length - key_length
        else: 
            diff = key_length - target_length
        #Step 4 - Make both values the same length
        cluster = [216] * diff
        if target_is_greater: 
            ord_key = cluster + ord_key
        else: 
            ord_tar = cluster + ord_tar
        #Step 5 - Carry out XOR operation on both lists
        xor = []
        for o in range(max(target_length, key_length)):
            xor.append(ord_tar[o] ^ ord_key[o])
        #Step 6 - Convert all list items to a hexadecimal string format
        secret = ""
        for item in xor: 
            secret += hex(item).upper() + "&"
        sec = []
        for s in secret: 
            sec.append(s)
        sec.pop()
        encrypted = ""
        for it in sec: 
            encrypted += it
            
        self.secret = encrypted

    def __str__(self):
        return self.secret

#Decryptor Class

class Decrypt:
    def __init__(self, secret, key):
        #Task - Perform XOR operation on target & key
        #============================================
        #Step 1 - Convert hexadecimal string format to ordinal list
        ord_sec = secret.split("&")
        ord_sec = [x.lower() for x in ord_sec]
        ord_sec = [int(x, 16) for x in ord_sec]
        ord_key = [ord(x) for x in key]
        #Step 2 - Find the longer list
        secret_is_greater = False
        if len(ord_sec) > len(ord_key): 
            secret_is_greater = True
        else:
            pass
        #Step 3 - Find the difference in length
        if secret_is_greater: 
            diff = len(ord_sec) - len(ord_key)
        else: 
            diff = len(ord_key) - len(ord_sec)
        #Step 4 - Make both values the same length
        cluster = [216] * diff
        if secret_is_greater: 
            ord_key = cluster + ord_key
        else: 
            ord_sec = cluster + ord_sec
        #Step 5 - Carry out XOR operation on secret and key
        xor = []
        for o in range(len(ord_sec)): 
            xor.append(ord_sec[o] ^ ord_key[o])
        #Step 6 - Convert ordinal values to ASCII characters
        plaintext = ""
        for c in xor: 
            plaintext += chr(c)
        self.plaintext = plaintext

    def __str__(self):
        return self.plaintext