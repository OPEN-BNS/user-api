import os, string, random, base64, hashlib
from Crypto.Cipher import AES
from Crypto import Random
from dotenv import dotenv_values

env = {
    **os.environ
}

ENCRYPTION_KEY = env["ENCRYPTION_KEY"]
PASSWORD_LENGTH = 20

#AES Parameters
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode("utf-8")))

def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))

def encryptPassword(password):
    return encrypt(password, ENCRYPTION_KEY)

def generateSecurePassword():
    s1 = list(string.ascii_lowercase)
    s2 = list(string.ascii_uppercase)
    s3 = list(string.digits)
    s4 = list(string.punctuation)

    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # calculate 30% & 20% of number of characters
    part1 = round(PASSWORD_LENGTH * (30/100))
    part2 = round(PASSWORD_LENGTH * (20/100))

    result = []

    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

    random.shuffle(result)

    password = "".join(result)

    password = encryptPassword(password)

    return password