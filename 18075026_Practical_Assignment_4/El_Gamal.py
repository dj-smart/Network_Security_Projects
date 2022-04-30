# Python program to demonstrate El Gamal encryption

import random
from math import pow

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)

# Generating large random numbers
def gen_key(q):

    key = random.randint(pow(10, 10), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 10), q)

    return key

# Modular exponentiation
def mod_power(a, b, c):
    x = 1
    y = a

    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)

    return x % c

# Asymmetric encryption
def encrypt(msg, q, h, g):

    encr_msg = []

    k2 = gen_key(q)# Private key for sender
    s = mod_power(h, k2, q)
    p = mod_power(g, k2, q)
    
    for i in range(0, len(msg)):
        encr_msg.append(msg[i])
    
    print("Private Key For Sender (k2) :",k2)
    print("g^k2 used : ", p)
    print("g^k1k2 used : ", s)
    for i in range(0, len(encr_msg)):
        encr_msg[i] = s * ord(encr_msg[i])

    return encr_msg, p

def decrypt(encr_msg, p, key, q):

    dr_msg = []
    h = mod_power(p, key, q)
    for i in range(0, len(encr_msg)):
        dr_msg.append(chr(int(encr_msg[i]/h)))
        
    return dr_msg

# Main Code
def main():

    msg = 'Network Security'
    print("Original Message :", msg)

    q = random.randint(pow(10, 10), pow(10, 30))
    g = random.randint(2, q)

    k1 = gen_key(q) # Private key for receiver
    h = mod_power(g, k1, q)
    
    print("Private Key For Receiver (k1) :",k1)
    print("g used : ", g)
    print("g^k1 used : ", h)

    encr_msg, p = encrypt(msg, q, h, g)
    dr_msg = decrypt(encr_msg, p, k1, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg);


if __name__ == '__main__':
    main()
