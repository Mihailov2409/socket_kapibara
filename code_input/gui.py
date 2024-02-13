import customtkinter
import clinet_enter

root = customtkinter.CTk()
root.title("Code input")
root.geometry("450x450")
root.grid_columnconfigure(0, weight=1)

def click():
    code = entry.get()
    langi = lang.get()
    clinet_enter.start(code, langi)

entry = customtkinter.CTkEntry(root, placeholder_text="Code", font=(None, 18), height=50)
entry.grid(padx=10, pady=20, sticky="ew")

lang = customtkinter.CTkEntry(root, placeholder_text="Language", font=(None, 18), height=50)
lang.grid(padx=10, pady=20, sticky="ew")

button = customtkinter.CTkButton(root, text="entry", command=click)
button.grid(padx=10, pady=10, sticky="ew")

root.mainloop()