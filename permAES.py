from Crypto.Cipher import AES
import binascii
import sys

key = b'\x03\x06\x02\x00\x01\x00' + 10 * b'\x00'
#plaintext = b'\x18' + 15 * b'\x00'
plaintext = key
key = b'\x1f\xd3\x1d\x60\x70\x70\x9d\x50\xfd\xfb\x82\xac\xd0\x0c\x1a\x51'

encryption = AES.new(key, AES.MODE_ECB)
ciphertext = encryption.encrypt(plaintext)
recovered_plaintext = encryption.decrypt(ciphertext)

# some examples of printouts

print(binascii.hexlify(key))
print(binascii.hexlify(ciphertext))
print(binascii.hexlify(recovered_plaintext))
