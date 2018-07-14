from Crypto.Cipher import AES
import binascii
import sys

key = b'\x01\x02\x03\x04\x05\x06' + 10 * b'\x00'
#plaintext = b'\x00' * 16
plaintext = key
key = b'\x84\x52\x4a\x3a\x53\xda\x2d\x06\xe3\x53\x3a\x42\xed\x3f\xfa\x38'

encryption = AES.new(key, AES.MODE_ECB)
ciphertext = encryption.encrypt(plaintext)
recovered_plaintext = encryption.decrypt(ciphertext)

# some examples of printouts

print(binascii.hexlify(key))
print(binascii.hexlify(ciphertext))
print(binascii.hexlify(recovered_plaintext))
