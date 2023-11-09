import numpy as np
import random
import string

def generate_dummy_data(size_MB):
    size_bytes = size_MB * 1024 * 1024
    current_size = 0
    data = []

    while current_size < size_bytes:
        name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
        address = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=20))
        email = ''.join(random.choices(string.ascii_lowercase, k=5)) + "@example.com"
        phone_number = ''.join(random.choices(string.digits, k=10))
        sentence = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + ' ', k=50))

        record = [name, address, email, phone_number, sentence]
        data.append(record)
        current_size += sum(len(str(field)) for field in record)

    return data

dummy_data = generate_dummy_data(101)

np.savetxt("dummy_dataset.txt", dummy_data, fmt="%s", delimiter=",")

print("Dummy dataset created successfully!")