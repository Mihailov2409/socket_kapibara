import customtkinter

root = customtkinter.CTk()
root.title("Code input")
root.geometry("450x450")
root.grid_columnconfigure(0, weight=1)

entry = customtkinter.CTkEntry(root, placeholder_text="Code", font=(None, 18), height=50)
entry.grid(padx=10, pady=20, sticky="ew")

button = customtkinter.CTkButton(root, text="entry")
button.grid(padx=10, pady=10, sticky="ew")

root.mainloop()