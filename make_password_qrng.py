#!/usr/bin/env python3
import random
import string
import urllib.request

password_length = int(input("Enter the length of password:"))
def generatingPassword(quantum_seed):
    password = random.sample(quantum_seed, password_length)

    password += random.choice(string.printable)
 
    passwordList = list(password)
    random.shuffle(passwordList)
    password = "".join(passwordList)
     
    return password

req = urllib.request.Request('https://qrng.anu.edu.au/wp-content/plugins/colours-plugin/get_block_alpha.php')
with urllib.request.urlopen(req) as response:
   quantum_seed_block = response.read()
   print(f"Password of length {password_length}: {generatingPassword(quantum_seed_block.decode('ascii'))}")
