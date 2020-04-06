# VCrypt

### Version : 0.1
### Author : Irfan Valerian

## ~ A Very Useful Module For CTF Players And Cryptography Lovers ~

### FEATURE:

* HEX
* BINARY
* CHARCODE
* BASE64
* BASE32
* BASE16
* BASE85
* ROT13
* MD5
* SHA1
* SHA224
* SHA256
* SHA512
* REVERSE TEXT
* RSA CIPHER
* AFFINE CIPHER
* RAILFENCE CIPHER
* CAESAR CIPHER
* VIGENERE CIPHER
* DNA CRYPTOGRAPHY
* SUBSTITUTION CIPHER

~ More Features Will Be On The Next Update ~

### USAGE:

* hex,bin,charcode,b64,b32,b16,b85
  ```
  {name}(text) to Encrypt -> ### Example : hex('Irfan')
  un{name}(text) to Decrypt -> ### Example : unhex('497266616e')
  ```

* rot13,sha1,sha224,sha246,sha512,reverse
  ```
  {name}(text) to Encrypt / Hash -> ### Example : rot13('Irfan')
  ```

* rsa
  ```
  Usage same as using the rsa module -> ### Example : rsa.newkeys(2048)
  ```

* caesar
  ```
  setkey(key) to set a new key -> ### Example : caesar.setkey('abcdef')
  encrypt(plain,n) to Encrypt -> ### Example : caesar.encrypt('Irfan',4)
  decrypt(cipher,n) to Decrypt -> ### Example : caesar.decrypt('Nagss',4)
  ```
* dna
  ```
  encrypt(plain) to Encrypt -> ### Example : dna.encrypt('Irfan')
  decrypt(cipher) to Decrypt -> ### Example : dna.decrypt('TAATGT')
  ```

* affine,railfence,vigenere,substitution
  ```
  encrypt(plain,key) to Encrypt -> ### Example : affine.encrypt('Irfan',[17,20])
  decrypt(cipher,key) to Decrypt -> ### Example : railfence.decrypt('Inraf',3)
  ```
