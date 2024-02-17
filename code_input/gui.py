import customtkinter
import clinet_enter

root = customtkinter.CTk()
root.title("Code input")
root.geometry("450x450")
root.grid_columnconfigure(0, weight=1)

def click():
    code = entry.get()
    langi = lang.get()
    name = fedora.get()
    out = clinet_enter.start(code, langi, name)
    text_output.text = out

entry = customtkinter.CTkEntry(root, placeholder_text="Code", font=(None, 18), height=50)
entry.grid(padx=10, pady=20, sticky="ew")

lang = customtkinter.CTkEntry(root, placeholder_text="Language", font=(None, 18), height=50)
lang.grid(padx=10, pady=20, sticky="ew")

fedora = customtkinter.CTkEntry(root, placeholder_text="user name", font=(None, 18), height=50)
fedora.grid(padx=10, pady=10, sticky="ew")

text_output = customtkinter.CTkEntry(root, placeholder_text="output", font=(None, 18), height=50)
text_output.grid(padx=10, pady=10, sticky="ew")

button = customtkinter.CTkButton(root, text="entry", command=click)
button.grid(padx=10, pady=10, sticky="ew")

root.mainloop()
