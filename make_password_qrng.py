#!/usr/bin/env python3
import random
import string
import ssl
import urllib.request

password_length = int(input("Enter the length of password:"))
def generatingPassword(quantum_seed_block):
    password = random.sample(quantum_seed_block, password_length)

    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
 
    passwordList = list(password)
    random.shuffle(passwordList)
    password = "".join(passwordList)
     
    return password

# Attain a quantum random character block seed
req = urllib.request.Request('https://qrng.anu.edu.au/wp-content/plugins/colours-plugin/get_block_alpha.php')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
with urllib.request.urlopen(req, context=ctx) as response:
   quantum_seed_block = response.read()
   #print(quantum_seed_block)
   print(f"Password of length {password_length}: {generatingPassword(quantum_seed_block.decode('ascii'))}")
