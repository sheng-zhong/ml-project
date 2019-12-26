import hashlib

def create_btc_hash_value(message, nonce):
    # message: string
    # nonce: random value from randomness
    unsecure_message = message + nonce
    secure_message = hashlib.sha256()
    secure_message.update(unsecure_message)
    return secure_message.hexdigest()