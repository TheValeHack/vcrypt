#!/usr/bin/env python

import base64
import rsa
import hashlib
import codecs
import string
import random
import itertools

# Cryptography Module For Anyone Who Likes Cryptography
# Made By @irfan_vrn
# For Python 3.x


class caesar:
    key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def setkey(self,key):
        self.key = key.upper()
    def encrypt(self,plain,n):
        result = ''
        for c in str(plain).upper():
           try:
             i = (self.key.index(c) + n) % len(self.key)
             result += self.key[i]
           except ValueError:
             result += c
        return result
    def decrypt(self,cipher,n):
        result = ''
        for p in str(cipher).upper():
           try:
             i = (self.key.index(p) - n) % len(self.key)
             result += self.key[i]
           except ValueError:
             result += p
        return result

class vigenere:
    def encrypt(self,plaintext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key.upper()]
        plaintext_int = [ord(i) for i in plaintext.upper()]
        ciphertext = ''
        for i in range(len(plaintext_int)):
           value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
           ciphertext += chr(value + 65)
        return ciphertext
    def decrypt(self,ciphertext, key):
        key_length = len(key)
        key_as_int = [ord(i) for i in key.upper()]
        ciphertext_int = [ord(i) for i in ciphertext.upper()]
        plaintext = ''
        for i in range(len(ciphertext_int)):
           value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
           plaintext += chr(value + 65)
        return plaintext

class dna:
    mapping = {
        "AAA":"a",
	"AAC":"b",
	"AAG":"c",
	"AAT":"d",
	"ACA":"e",
	"ACC":"f",
	"ACG":"g",
	"ACT":"h",
	"AGA":"i",
	"AGC":"j",
	"AGG":"k",
	"AGT":"l",
	"ATA":"m",
        "ATC":"n",
	"ATG":"o",
	"ATT":"p",
	"CAA":"q",
	"CAC":"r",
	"CAG":"s",
	"CAT":"t",
	"CCA":"u",
	"CCC":"v",
	"CCG":"w",
	"CCT":"x",
	"CGA":"y",
	"CGC":"z",
	"CGG":"A",
	"CGT":"B",
	"CTA":"C",
	"CTC":"D",
	"CTG":"E",
	"CTT":"F",
	"GAA":"G",
	"GAC":"H",
	"GAG":"I",
	"GAT":"J",
	"GCA":"K",
	"GCC":"L",
	"GCG":"M",
	"GCT":"N",
	"GGA":"O",
	"GGC":"P",
	"GGG":"Q",
	"GGT":"R",
	"GTA":"S",
	"GTC":"T",
	"GTG":"U",
	"GTT":"V",
	"TAA":"W",
	"TAC":"X",
	"TAG":"Y",
	"TAT":"Z",
	"TCA":"1",
	"TCC":"2",
	"TCG":"3",
	"TCT":"4",
	"TGA":"5",
	"TGC":"6",
	"TGG":"7",
	"TGT":"8",
	"TTA":"9",
	"TTC":"0",
	"TTG":" ",
	"TTT":"."
	}
    def encrypt(self,plain):
        mapping = {v:k for k,v in self.mapping.items()}
        result = ''
        for p in plain:
           try:
             result += mapping[p]
           except KeyError:
             result += p
        return result
    def decrypt(self,cipher):
        cipher = cipher.replace(' ','')
        cipher = list(map(lambda x: str(x),[cipher[i:i+3] for i in range(0,len(cipher),3)]))
        result = ''
        for dnas in cipher:
           try:
             result += self.mapping[dnas]
           except KeyError:
              result += dnas
        return result

class affine:
    def egcd(self,a, b):
       x,y, u,v = 0,1, 1,0
       while a != 0:
           q, r = b//a, b%a
           m, n = x-u*q, y-v*q
           b,a, x,y, u,v = a,r, u,v, m,n
       gcd = b
       return gcd, x, y
    def modinv(self,a, m):
       gcd, x, y = self.egcd(a, m)
       if gcd != 1:
           return None  # modular inverse does not exist
       else:
           return x % m
    def encrypt(self,text,key):
       return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) + ord('A')) for t in text.upper().replace(' ', '') ])
    def decrypt(self,cipher,key):
       return ''.join([ chr((( self.modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher ])

class substitution:
    defaultkey = ''.join(sorted(string.printable, key=lambda _:random.random()))
    def encrypt(self,plaintext, key = defaultkey):
        try:
           return ''.join(key[string.printable.index(char)] for char in plaintext)
        except:
           return 'Wrong Key Format'
    def decrypt(self,plaintext, key = defaultkey):
        try:
           return ''.join(string.printable[key.index(char)] for char in plaintext)
        except:
           return 'Wrong Key Format'

class railfence:
    def encrypt(self,text, key):
        rail = [['\n' for i in range(len(text))]
                      for j in range(key)]
        dir_down = False
        row, col = 0, 0
        for i in range(len(text)):
            if (row == 0) or (row == key - 1):
                dir_down = not dir_down
            rail[row][col] = text[i]
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return("" . join(result))
    def decrypt(self,cipher, key):
        rail = [['\n' for i in range(len(cipher))]
                      for j in range(key)]
        dir_down = None
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False
            rail[row][col] = '*'
            col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        index = 0
        for i in range(key):
            for j in range(len(cipher)):
                if ((rail[i][j] == '*') and
                   (index < len(cipher))):
                    rail[i][j] = cipher[index]
                    index += 1
        result = []
        row, col = 0, 0
        for i in range(len(cipher)):
            if row == 0:
                dir_down = True
            if row == key-1:
                dir_down = False
            if (rail[row][col] != '*'):
                result.append(rail[row][col])
                col += 1
            if dir_down:
                row += 1
            else:
                row -= 1
        return("".join(result))


rsa = rsa
caesar = caesar()
vigenere = vigenere()
dna = dna()
affine = affine()
substitution = substitution()
railfence = railfence()

def hex(teks):
    return ''.join(format(ord(i),'x') for i in str(teks))
def unhex(teks):
    return bytes.fromhex(str(teks))
def bin(teks):
    return ''.join(format(ord(i),'b') for i in str(teks))
def unbin(teks):
    teks = teks.replace(' ','')
    bin = list(map(lambda x: str(x),[teks[i:i+7] for i in range(0,len(teks),7)]))
    return ''.join(chr(int(i,2)) for i in bin)
def charcode(teks):
    return ','.join(map(str,[ord(i) for i in str(teks)]))
def uncharcode(teks):
    return ''.join(chr(int(i)) for i in str(teks).split(','))
def b64(teks):
    return base64.b64encode(str(teks).encode('utf-8'))
def unb64(teks):
    return base64.b64decode(teks)
def b32(teks):
    return base64.b32encode(str(teks).encode('utf-8'))
def unb32(teks):
    return base64.b32decode(teks)
def b16(teks):
    return base64.b16encode(str(teks).encode('utf-8'))
def unb16(teks):
    return base64.b16decode(teks)
def b85(teks):
    return base64.a85encode(str(teks).encode('utf-8'))
def unb85(teks):
    return base64.a85decode(teks)
def reverse(teks):
    teks = str(teks)
    return teks[len(teks)::-1]
def md5(teks):
    return hashlib.md5(teks.encode("utf-8")).hexdigest()
def sha256(teks):
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()
def sha512(teks):
    return hashlib.sha512(teks.encode("utf-8")).hexdigest()
def sha224(teks):
    return hashlib.sha224(teks.encode("utf-8")).hexdigest()
def sha1(teks):
    return hashlib.sha1(teks.encode("utf-8")).hexdigest()
def rot13(teks):
    return codecs.encode(teks,'rot_13')
