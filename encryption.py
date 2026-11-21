from cryptography.fernet import Fernet

def encrypt_file(path):
    if not path:
        return "No file provided"

    key = b"cYGEoL5KD3r8HpPx2T5Sqv8Jgmw5hEXerxr7PKR_cDM="
    f = Fernet(key)

    with open(path, "rb") as file:
        data = file.read()

    encrypted = f.encrypt(data)

    with open(path, "wb") as file:
        file.write(encrypted)

    return f"Encrypted {path}"