import tkinter as tk
import hashlib


window = tk.Tk()
window.title("!so secure Password Manager")

website_label = tk.Label(window, text="Website name:")
website_label.pack()

username_label = tk.Label(window, text="Username:")
username_label.pack()

password_label = tk.Label(window, text="!secure password:")
password_label.pack()

website_entry = tk.Entry(window)
website_entry.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

def save_password():

  website = website_entry.get()
  username = username_entry.get()
  password = password_entry.get()

  hashed_password = hashlib.sha256(password.encode()).hexdigest()

  data = f"{website}|{username}|{hashed_password.encode()}"


  with open("notsecurepasswords.txt", "a") as password_file:
    password_file.write(data + "\n")

  website_entry.delete(0, tk.END)
  username_entry.delete(0, tk.END)
  password_entry.delete(0, tk.END)

  success_label = tk.Label(window, text="!so secure password saved successfully!")
  success_label.pack()
  success_label.after(2000, success_label.destroy)

submit_button = tk.Button(window, text="Submit", command=save_password)
submit_button.pack()

window.mainloop()
