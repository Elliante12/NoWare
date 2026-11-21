from cryptography.fernet import Fernet, InvalidToken


def decrypt_file(filename):
    key = b"cYGEoL5KD3r8HpPx2T5Sqv8Jgmw5hEXerxr7PKR_cDM="
    f = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    try:
        decrypted = f.decrypt(data)
    except InvalidToken:
        return f"Decrypt failed (wrong key or double-encrypted): {filename}"

    with open(filename, "wb") as file:
        file.write(decrypted)

    return f"Decrypted: {filename}"
