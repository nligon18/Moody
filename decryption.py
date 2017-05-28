from Crypto.Cipher import AES
# Text and Key must be in multiples of 16-Bit Strings
# Encryption
def encrypt(string):
	encryption_suite = AES.new('d7f9757819fd9922f0e93a992ea754f9', AES.MODE_CBC, 'This is an IV456')
	cipher_text = encryption_suite.encrypt("d5ca8e27b253d455d3466803b42f0a82")
	print cipher_text
# Decryption
def decrypt(key,hash):
	decryption_suite = AES.new('d7f9757819fd9922f0e93a992ea754f9', AES.MODE_CBC, 'This is an IV456')
	plain_text = decryption_suite.decrypt(cipher_text)
	print plain_text
def promptKey():
	password = input('Enter the decryption key: ')
promptKey()
def decryptCredentials():
	