from cryptography.fernet import Fernet

secret_key = b'HCSP-XM-YJ7L4Z_1HN7_Y86v75l0UZpejRBSq_CAv8A='
print(secret_key)

nombre = 'Arturo Emmanuel'
cipher_suite = Fernet(secret_key)
print(cipher_suite)

encrypted_nombre = cipher_suite.encrypt(nombre.encode())
print(encrypted_nombre)
encrypted_nombre = encrypted_nombre.decode()
print(encrypted_nombre)
print(len(encrypted_nombre))

print(cipher_suite)

decode = cipher_suite.decrypt(b'gAAAAABlOSTxcF-LTS3ap4rNUiuaHSwZ_YFWfs16Xoz6IU8QHVdXFcUHfqo2yOYFJq_UNX3Xk6kBprFEZpWQnEnp141ESX_hHA==')
print(decode)
print(decode.decode())

