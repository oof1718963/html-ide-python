from tkinter import *
from PIL import ImageTk,Image
import os
from tkinter import filedialog
import webbrowser
root = Tk()
root.title("Notepad")
root.minsize(800, 800)
root.maxsize(800, 800)
root.configure(background="grey70")


open_img = ImageTk.PhotoImage(Image.open ("openIDE.png"))
close_img = ImageTk.PhotoImage(Image.open ("closeIDE.png"))
save_img = ImageTk.PhotoImage(Image.open ("saveIDE.png"))
play_img = ImageTk.PhotoImage(Image.open ("playIDE.png"))





label1 = Label(root, text = "File Name")
label1.configure(background="grey70", font =('Inter', 10))
label1.place(relx = 0.27,rely = 0.03,anchor = CENTER)


input_file_name = Entry(root)
input_file_name.configure(background="grey", font =('Inter', 7))
input_file_name.place(relx = 0.40,rely = 0.03, anchor = CENTER) 

my_text = Text(root, height=35, width=80)
my_text.configure(background="grey", font =('Inter', 10))
my_text.place(relx = 0.5,rely = 0.55,anchor = CENTER)

name = ""
name1 = ""
    
def play():
    global name1
    html_file = filedialog.askopenfilename(title=" Open Html File", filetypes=(("Html File", "*.html"),))
    path = os.path.basename(html_file)
    formated_html = os.path.abspath(html_file)
    last_html = formated_html
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(last_html)

def open_file():
    global name
    my_text.delete(1.0, END)
    input_file_name.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Html File", "*.html"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(text_file,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
def save_file():
    input_name = input_file_name.get()
    file = open(input_name + ".txt","w")
    data = my_text.get(1.0,END)
    print(data)
    file.write(data)
    input_file_name.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("update","success")

def close_file():
    root.destroy()
    
    
button_open = Button(root, image = open_img, text = "Open File", command = open_file, background="grey")
button_close = Button(root, image = close_img, text = "Close File",command = close_file, background="grey")
button_save = Button(root, image = save_img, text = "Save File", command = save_file, background="grey")
button_play = Button(root, image = play_img, text = "Play File", command = play, background="grey") 
button_play.place(relx = 0.20, rely = 0.03, anchor = CENTER )
button_open.place(relx = 0.05, rely = 0.03, anchor = CENTER )
button_save.place(relx = 0.10, rely = 0.03, anchor = CENTER )
button_close.place(relx = 0.15, rely = 0.03, anchor = CENTER )

root.mainloop()