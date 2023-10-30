import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

def pop():
    response= messagebox.askyesno("WARNING!","Do you really want to exit")
    if response == 1:
        root.quit()
    else:
        pass

def open_file():
    file_path=askopenfilename(
        filetypes=[("Text file", ".txt"),("Python file", ".py"),("All file", "*.*")]
    )
    if not file_path:
        return
    txt_edit.delete(1.0,tk.END)
    with open(file_path, mode="r") as input_file:
        txt = input_file.read()
        txt_edit.insert(1.0, txt)
    root.title(f"Simple Text Editor - {file_path}")

def save_file():
    file_path=asksaveasfilename(
        defaultextension=("Text file", ".txt"),
        filetypes=[("Text file", ".txt"),("Python file", ".py"),("All file", "*.*")]
    )
    if not file_path:
        return
    with open(file_path, mode="w") as output:
        txt = txt_edit.get(1.0, tk.END)
        output.write(txt)
    root.title(f"Simple Text Editor - {file_path}")

root = tk.Tk()
root.title("Simple Text Editor")
img_logo = tk.PhotoImage(file="image/logo.png")
root.iconphoto(False, img_logo)

root.rowconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

scroll_bar= tk.Scrollbar(root)
scroll_bar.grid(row=0, column=5, sticky="ns")

txt_edit= tk.Text(root, bg="white", fg="purple", font=("arial", 14), yscrollcommand=scroll_bar.set)

frm_buttons= tk.Frame(root, relief=tk.RAISED, bd=2, bg="purple")

btn_open= tk.Button(frm_buttons, text="OPEN", bg="purple", fg="white", command=open_file)
btn_save= tk.Button(frm_buttons, text="SAVE AS", bg="purple", fg="white", command=save_file)
btn_exit= tk.Button(frm_buttons, text="EXIT", bg="purple", fg="white", command= pop)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="sn")

txt_edit.grid(row=0, column=1, sticky="nwse")

scroll_bar.config(command=txt_edit.yview)

root.mainloop()