# NoWare

NoWare is a small Python file-encryption demonstration for Windows.

> [!WARNING]
> **The current script changes real files.** On launch, `NoWare.py` reads `*.jpg` files from `%USERPROFILE%\OneDrive\Desktop` and encrypts them in place. Entering the hard-coded password `1234` attempts to decrypt those files. This can make personal files unusable if the script is interrupted, the key or files are changed, or decryption fails. Do not run it on a computer or folder containing files you care about. The project should not be described or treated as harmless in its current form.

## Requirements

- Windows
- Python 3
- Tkinter (normally included with the standard Windows Python installer)
- `cryptography` Python package

Install the package with:

```powershell
py -m pip install cryptography
```

The project also requires the `encryption.py` and `decrypt.py` files to be in the same folder/directory as `NoWare.py`.

## Run

Only use a disposable test setup with files you can afford to lose. Before running, change the target directory in `NoWare.py` to a dedicated test folder and put copies of test `.jpg` files there. Then run:

```powershell
cd "Project_Path"
python NoWare.py
```

The current implementation uses `1234` as its demo password. The password is not used to derive the Fernet key; the encryption key is embedded in the source code.

## Current behavior and limitations

- Looks only for files matching `*.jpg` directly inside the configured OneDrive Desktop folder; it does not scan subdirectories.
- Encrypts matching files in place and writes the encrypted bytes back to each original file.
- Attempts to decrypt the same files after the password is accepted.
- Uses a fixed Fernet key embedded in `encryption.py` and `decrypt.py`; this is suitable only for a controlled demonstration, not real data protection.
- Disables the window's normal close action while it is running.
- Displays ransom-style text as part of the UI demonstration.

## Safety

This repository is an educational demonstration, not a secure backup or file-protection tool. A safer version should operate only on a temporary sample directory and preserve originals. Never test encryption behavior on personal, shared, synced, or production files.

## License

This project is licensed under the MIT License.
