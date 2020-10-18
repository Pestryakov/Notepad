from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.geometry('800x400+800+300')

main_menu = Menu(root)
root.config(menu=main_menu)


def about_program():
    messagebox.showinfo(title='About notepad', message='Program version 0.0.1')


def notepad_quit():
    answer = messagebox.askokcancel(title='Exit', message='Close the program')
    if answer:
        root.destroy()

def open_file():
    file_path = filedialog. askopenfilename(title='Select File', filetypes=(('Text documents','*.txt'), ('All files', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(title='Select File', filetypes=(('Text documents', '*.txt'), ('All files', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()



def change_theme(theme):
    text_field['bg'] = theme_colors[theme]['text_bg']
    text_field['fg'] = theme_colors[theme]['text_fg']
    text_field['insertbackground'] = theme_colors[theme]['cursor']
    text_field['selectbackground'] = theme_colors[theme]['select_bg']


# File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=notepad_quit)
main_menu.add_cascade(label='File', menu=file_menu)
# Theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Light Theme', command=lambda: change_theme('light'))
theme_menu_sub.add_command(label='Dark Theme', command=lambda: change_theme('dark'))
theme_menu.add_cascade(label='Decoration', menu=theme_menu_sub)
theme_menu.add_command(label='About the program', command=about_program)
main_menu.add_cascade(label='Various', menu=theme_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    'dark': {
        'text_bg': '#343D46', 'text_fg': '#C6DEC1', 'cursor': '#EDA756', 'select_bg': '#4E5A65'
    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000', 'cursor': '#8000FF', 'select_bg': '#777'
    }
}

text_field = Text(f_text, bg=theme_colors['dark']['text_bg'], fg=theme_colors['dark']['text_fg'], padx=10, pady=10,
                  wrap=WORD,
                  insertbackground=theme_colors['dark']['cursor'], selectbackground=theme_colors['dark']['select_bg'],
                  width=30,
                  spacing3=10, font=('Courier New', 10))
text_field.pack(fill=BOTH, expand=1, side=LEFT)

scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(fill=Y, side=LEFT)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()
