import hashlib

input_data = input()

encoded = input_data.encode()
result = hashlib.sha256(encoded).hexdigest()

print(result)
