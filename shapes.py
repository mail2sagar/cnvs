from tkinter import *
from tkinter import ttk 

window = Tk()

window.title("Working on canvas using functions")
window.geometry("600x600")




startx = Label(window,text="startx")

starty = Label(window,text="starty")

choose_color_label = Label(window,text="Choose a colour")

endx = Label(window,text="endx")

endy = Label(window,text="endy")


start_y = ttk.Combobox(window)

color = ttk.Combobox(window)

start_x = ttk.Combobox(window)

end_x = ttk.Combobox(window)

end_y = ttk.Combobox(window)

start_x.place(relx=0.2, rely=0.85,anchor=CENTER)

starty.place( relx=0.3, rely=0.85,anchor=CENTER)

start_y.place(relx=0.4, rely=0.85,anchor=CENTER)

color.place(relx=0.8,rely=0.9,anchor=CENTER)

choose_color_label.place(relx=0.6,rely = 0.9,anchor=CENTER)

startx.place(relx=0.1,rely = 0.85,anchor=CENTER)

endx.place(relx=0.5, rely=0.85,anchor=CENTER)

end_x.place(relx=0.6, rely=0.85,anchor=CENTER)

end_y.place(relx=0.8, rely=0.85,anchor=CENTER)

endy.place(relx=0.7, rely=0.85,anchor=CENTER)



canvas = Canvas(window,width=990,height=490,bg="white",highlightbackground="gray")
canvas.pack()

my_image = canvas.create_image(50,50)


shapes = ""

old_x = 50
old_y = 50

new_x = 50
new_y = 50

window.mainloop()