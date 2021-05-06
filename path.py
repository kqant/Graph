from tkinter import *
from tkinter import filedialog

class Path_File:
    def Path(self):
        def get_file_path():
            global file_path
            # Open and return file path
            file_path = filedialog.askopenfilename(title="Select A File")

        def Open():
            window = Tk()
            window.title("Graph Application")
            window.geometry('400x250')
            lbl = Label(window, text="Please, attach your file", font=("Arial Bold", 14), fg="purple")
            lbl.grid(column=0, row=0)
            # Creating a button to search the file
            btn = Button(window, text="Open File", bg="black", fg="purple", command=get_file_path)
            btn.grid(column=1, row=0)
            window.mainloop()
            return file_path

        return Open()

x = Path_File()
print(x.Path())
