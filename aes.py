from simple_aes_cipher import AESCipher, generate_secret_key


pass_phrase = "hacker"
secret_key = generate_secret_key(pass_phrase)
cipher = AESCipher(secret_key)


def encrypt(raw_text):
# generate cipher

    #raw_text = "abcdefg"
    encrypt_text = cipher.encrypt(raw_text)
    return(encrypt_text)
#assert raw_text != encrypt_text

def decrypt(encrypt_text):
    decrypt_text = cipher.decrypt(encrypt_text)
    #print("\n decryption is")
    return decrypt_text
#assert encrypt_text != decrypt_text
#assert decrypt_text == raw_text
#print(encrypt("hacker"))
#print(decrypt(encrypt("hacker")))
