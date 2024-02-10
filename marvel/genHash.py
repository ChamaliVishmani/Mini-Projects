import hashlib
import time


def generate_hash(ts, private_key, public_key):
    # Concatenate timestamp, private key, and public key
    data_to_hash = f"{ts}{private_key}{public_key}"

    # Use MD5 hash function
    hashed_data = hashlib.md5(data_to_hash.encode()).hexdigest()

    return hashed_data


# Example usage
public_key = "abcd"
private_key = "1234"
ts = str(int(time.time()))  # Current timestamp in seconds

hash_value = generate_hash(ts, private_key, public_key)
print(hash_value)
print(ts)
