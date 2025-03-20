from customtkinter import *
import os
from tkinter import filedialog

#First time using classes in Python, though I did cheat on the file read/write segments.

START_OF_TEXT = 1.0 #Settle my confusion

class Top_Bar(CTkFrame):
    def __init__(self, master, notepad_textbox): #add notepad_textbox here so it can access notepad_textbox from Notes
        super().__init__(master)

        self.configure(height = 22, width = self.winfo_screenwidth())

        self.button_save = CTkButton(self, text="Save File", width=50, height=22, command=self.button_save_action)
        self.button_save.pack(side="left", anchor=CENTER)

        self.button_open = CTkButton(self, text="Open File", width=50, height=22, command=self.button_open_action)
        self.button_open.pack(side="left", anchor=CENTER)

        fonts = ["Helvetica", "Arial", "Times New Roman", "Verdana", "Tahoma", "Calibri"]
        self.button_font = CTkComboBox(self, width=75, height=22, values=fonts, command=self.button_font_action)
        self.button_font.pack(side="left", anchor=CENTER)

        colors = ["#ffffff", "#3df0cd", "#f03d3d", "#3df07b", "#3d7bf0", "#f03d66"]
        self.button_color = CTkComboBox(self, width=75, height=22, values=colors, command=self.button_color_action)
        self.button_color.pack(side="left", anchor=CENTER)

        self.notepad_textbox = notepad_textbox

    def button_save_action(self):

        text_to_save = self.notepad_textbox.get('1.0', END) #Mysterious Indian man says, '1.0' means from start, to 'END'. So start of the text to end.
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        #I really need to learn other libraries, I understand this but wouldn't be able to replicate without documentation.
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(text_to_save)
                print(f"File saved to {file_path}")  
            except ValueError:
                print(f"Error saving file..")
        
    def button_open_action(self):
        file_to_open = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_to_open: 
            try:
                with open(file_to_open, 'r') as file:
                    data = file.read()
                    self.notepad_textbox.delete(START_OF_TEXT, END)
                    self.notepad_textbox.insert(START_OF_TEXT, data) #Start to end of data
                    print(f"File opened: {file_to_open}") 
            except ValueError:
                print("Error opening file..")

    def button_font_action(self, choice):
        try:
            self.notepad_textbox.configure(font=(choice, 17))
        except ValueError:
            print("Error loading font..")

    def button_color_action(self, choice):
        try:
            self.notepad_textbox.configure(text_color=(choice))
        except ValueError:
            print("Error changing text color..")

class Notepad_Textbox(CTkTextbox):
    def __init__(self, master):
        super().__init__(master)



class Notes(CTk):
    def __init__(self):
        super().__init__()

        #Main Window

        self.title("Notepad")

        self.window_width = 1000
        self.window_height = 700

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (self.window_width / 2)
        y = (screen_height / 2) - (self.window_height / 2)

        self.geometry("{}x{}+{}+{}".format(self.window_width,self.window_height,int(x),int(y)))
    
        self.notepad_textbox = Notepad_Textbox(self) #set it here before top_bar otherwise top_bar won't find it
        self.topbar = Top_Bar(self, self.notepad_textbox)
        
        
        self.topbar.pack(side="top")
        self.notepad_textbox.pack(expand=True, fill="both")


if __name__ == "__main__":
    app = Notes()
    app.resizable(True,True,)
    app.mainloop()
