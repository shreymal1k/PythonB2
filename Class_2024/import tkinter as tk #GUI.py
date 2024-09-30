import tkinter as tk    #GUI

from file_organizer import organize_files

root=tk.Tk()
root.title("File  Organizer")
root.geometry("400x250")


def show_input():
    user_input=entry.get()
    print("User Input:",user_input)




label=tk.Label(root,text="Laber text content")
label.pack(pady=10)

entry=tk.Entry(root,width=70)
entry.pack(pady=5)

button=tk.Button(root,text="Submit")
button.pack(pady=10)

root.mainloop()

# Design a file organizer gui app