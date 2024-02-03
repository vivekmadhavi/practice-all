import tkinter as tk

def get_password():
    password = entry_password.get()
    print("Entered Password:", password)

# Create the main window
root = tk.Tk()
root.title("Password Entry Example")

# Create a Label
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)

# Create an Entry widget with show option for password
entry_password = tk.Entry(root, show="*")  # The show option sets the character to display (e.g., "*")
entry_password.pack(pady=10)

# Create a Button to retrieve the password
btn_submit = tk.Button(root, text="Submit", command=get_password)
btn_submit.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()