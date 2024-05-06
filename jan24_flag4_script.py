# MITM Project - New Flag4

# Author: Joseph Abel and Rennan Fernandes

# Email:  jabell9@gatech.edu, renanfernandes@gatech.edu

# Generate a unique hash (sha256) given a gitID and display on the screen.

import hashlib

#x = input("Enter your GITID : ")
#hash_object = hashlib.sha256(x.encode())
#hex_digest = hash_object.hexdigest()
#print("Combined hash: ", hex_digest)


x = input("Enter your GTID : ") 

hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
hash_object2 = hashlib.sha256(b"CS6035-Summ-Flag4N0w")
hex_dig22 = hash_object2.hexdigest()
print("Combined hash   :  ", hex_dig+hex_dig22)
