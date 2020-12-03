import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath=askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text=input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Encrypter - {filepath}")

def save_file():
    filepath=asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text=txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Encrypter - {filepath}")

def ceasarCypher(message,key,encrypt) -> str: #Remember to remove message
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output = ""
    message = message.upper()
    for symbol in message:
        if symbol in alphabet:
            num = alphabet.find(symbol) ## Retrieves number associated with the alphabet
            if encrypt == True:
                num = num + key
            else:
                num = num - key
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    return output

def vigenereCypher(message,phrase,encrypt) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 0
    output = ""
    message = message.upper()
    phrase =  phrase.upper()
    for symbol in message:
        if i == len(phrase):
            i = i - len(phrase)
        if symbol in alphabet:
            num = alphabet.find(symbol)
            shiftFactor = alphabet.find(phrase[i])
            if encrypt == True:
                num = num + shiftFactor
            else:
                num = num - shiftFactor
            ## Wrap-around protection
            if num >= len(alphabet):
                num = num - len(alphabet)
            elif num < 0:
                num = num + len(alphabet)
            i = i + 1
            ## Adding generated letter to translated array
            output = output + alphabet[num]
        else:
            output = output + symbol ## If symbol is not recognised as a letter, it is unaltered
    return output

def encrypt():
    cypher=mode.get()
    if cypher == "ceasar":
        key=int(ent_key.get())
        message=txt_edit.get("1.0", tk.END)
        translate=ceasarCypher(message,key,encrypt=True)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)
    if cypher == "vigenere":
        phrase=str(ent_phrase.get())
        message=txt_edit.get("1.0", tk.END)
        translate=vigenereCypher(message,phrase,encrypt=True)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)

def decrypt():
    cypher=mode.get()
    if cypher == "ceasar":
        key=int(ent_key.get())
        message=txt_edit.get("1.0", tk.END)
        translate=ceasarCypher(message,key,encrypt=False)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)
    if cypher == "vigenere":
        phrase=str(ent_phrase.get())
        message=txt_edit.get("1.0", tk.END)
        translate=vigenereCypher(message,phrase,encrypt=False)
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, translate)

window=tk.Tk()
window.title("Simple Text Encrypter")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#Establishing major window divisions
mainframe=tk.Frame(window)
txt_edit=tk.Text(window)
mainframe.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

#Setting up the save/load buttons and positions within their sub-frame
frm_topbuttons=tk.Frame(mainframe)
btn_open=tk.Button(frm_topbuttons, text="Open", command=open_file)
btn_save=tk.Button(frm_topbuttons, text="Save As...", command=save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=0, column=1, sticky="ew", padx=5)

#Setting up the "header" sub-frame
frm_divider=tk.Frame(mainframe)
lbl_divider=tk.Label(frm_divider, text="Cypher Options")
lbl_divider.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

#Main options sub-frame, with radiobutton selection
frm_encryption=tk.Frame(mainframe)
mode=tk.StringVar()
rad_ceasar=tk.Radiobutton(frm_encryption, text="Ceasar Cypher", variable=mode, value="ceasar")
rad_vigenere=tk.Radiobutton(frm_encryption, text="Vigenere Cypher", variable=mode, value="vigenere")
lbl_key=tk.Label(frm_encryption, text="Key:")
lbl_phrase=tk.Label(frm_encryption, text="Phrase:")
ent_key=tk.Entry(frm_encryption, width=10)
ent_phrase=tk.Entry(frm_encryption, width=10)

#Positioning for the above widgets within sub-frame
rad_ceasar.grid(row=0, column=0, sticky="ew")
rad_vigenere.grid(row=1, column=0, sticky="ew")
lbl_key.grid(row=0, column=1, sticky="ew")
lbl_phrase.grid(row=1, column=1, sticky="ew")
ent_key.grid(row=0, column=2, sticky="ew")
ent_phrase.grid(row=1, column=2, sticky="ew")

#Finally, the buttons that make it all run
frm_run=tk.Frame(mainframe)
btn_encrypt=tk.Button(frm_run, text="Encrypt", command=encrypt)
btn_decrypt=tk.Button(frm_run, text="Decrypt", command=decrypt)
btn_encrypt.grid(row=0, column=0, sticky="ew")
btn_decrypt.grid(row=0, column=1, sticky="ew")

#Placing sub-frames into the main-frame
frm_topbuttons.grid(row=0, column=0, sticky="ns")
frm_divider.grid(row=1, column=0, sticky="ns")
frm_encryption.grid(row=2, column=0, sticky="ns")
frm_run.grid(row=3, column=0, sticky="ns")

window.mainloop()