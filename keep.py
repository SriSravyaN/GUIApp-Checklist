import tkinter as tk
from tkinter import END,ANCHOR
import sys, os
from tkinter import PhotoImage

#define window elements
root=tk.Tk()
root.title('To-do List Application')
root.geometry('500x500')
root.resizable(0,0)

#root.iconbitmap('check1.ico')
#root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='/checklist/check1.png')


#define fonts and colors

root_color='#6019bd'
button_color='#b543a8'
my_font=('Times New Roman',14)
root.config(bg=root_color)

#define functions 

def add_item():
    my_listbox.insert(END,input_item.get())
    input_item.delete(0,END)
    
def remove_item():
    my_listbox.delete(ANCHOR)   
    
def save_list():
    with open('checklist.txt','w') as f:
        list_tuple=my_listbox.get(0,END)
        for item in list_tuple:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item + "\n")
            
def open_list():
    try:
        with open('checklist.txt','r') as f:
            for line in f:
                   my_listbox.insert(0,line)
    except:
        return 
     
def clear_list():
    my_listbox.delete(0,END)    

#define layout:frames

input_frame=tk.Frame(root,bg=root_color)
output_frame=tk.Frame(root,bg=root_color)
button_frame=tk.Frame(root,bg=root_color)

input_frame.pack()
output_frame.pack()
button_frame.pack()

#Adding widgets on input frame

input_item=tk.Entry(input_frame,borderwidth=3,width=35,font=my_font)
input_button=tk.Button(input_frame,text="Add item",borderwidth=2,font=my_font,bg=button_color,command=add_item)
input_item.grid(row=0,column=0,padx=5,pady=5)
input_button.grid(row=0,column=1,padx=5,pady=5,ipadx=5)

#Adding widgets on output frame
scroll_bar=tk.Scrollbar(output_frame)
my_listbox=tk.Listbox(output_frame,width=45,height=17,font=my_font,borderwidth=3,yscrollcommand=scroll_bar.set)
#configuring scrollbar
scroll_bar.config(command=my_listbox.yview)
my_listbox.grid(row=0,column=0)
scroll_bar.grid(row=0,column=1,sticky='NS')

#Adding widgets on button frame

save_button=tk.Button(button_frame,bg=button_color,text='Save List',borderwidth=3,font=my_font,command=save_list)
clear_button=tk.Button(button_frame,bg=button_color,text='Clear List',borderwidth=3,font=my_font,command=clear_list)
remove_button=tk.Button(button_frame,text='remove item',borderwidth=3,font=my_font,bg=button_color,command=remove_item)
quit_button=tk.Button(button_frame,text='Quit',bg=button_color,font=my_font,borderwidth=3,command=root.destroy)

clear_button.grid(row=0,column=0,padx=2,pady=11,ipadx=10)
remove_button.grid(row=0,column=1,padx=2,pady=11)
save_button.grid(row=0,column=2,padx=2,pady=11,ipadx=10)
quit_button.grid(row=0,column=3,padx=2,pady=11,ipadx=25)

#opening previously saved list available

open_list()

#define mainloop for root
root.mainloop()
