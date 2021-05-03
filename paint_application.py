from tkinter import *
from tkinter import ttk, colorchooser
from PIL import ImageGrab, ImageTk, Image



class PaintApplication:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'white'
        self.color_bg = 'black'
        self.old_x = None
        self.old_y = None
        self.penwidth = 4
        self.drawWidgets()
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def paint(self, e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth,
                               fill=self.color_fg, capstyle=ROUND, smooth=True)
        self.old_x = e.x
        self.old_y = e.y

    def reset(self, e):
        self.old_x = None
        self.old_y = None

    def changew(self, e):
        self.penwidth = e

    def clear(self):
        self.c.delete(ALL)
        self.c.create_image(0, 0, image=self.gif1, anchor=NW)

    def change_fg(self):
        self.color_fg = colorchooser.askcolor(color=self.color_fg)[1]

    def eraser(self):
        if (self.var1.get() == 1):
            self.color_fg = 'black'
        else:
            self.color_fg = 'white'

#    def change_bg(self):
#        self.color_bg = colorchooser.askcolor(color=self.color_bg)[1]

    def saveImage(self):
        x1 = self.c.winfo_rootx()
        y1 = self.c.winfo_rooty()
        x2 = x1 + self.c.winfo_width()
        y2 = y1 + self.c.winfo_height()
        ImageGrab.grab().crop((x1, y1, x2, y2)).save("mitochondria.tif") #j.save("C:/Users/User/Desktop/mesh_trans",".bmp"), így kell kimenteni egy adott helyre

    def drawWidgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        Label(self.controls, text="Penwidth", font=('arial 16')).grid(row=0, column=0)
        self.var1 = IntVar()
        self.cb = Checkbutton(self.controls, text='Erase', font=('arial 16'), variable=self.var1, onvalue=1, offvalue=0,
                              command=self.eraser).grid(row=5, column=0)
        self.slider = ttk.Scale(self.controls, from_=4, to=15, command=self.changew, orient=HORIZONTAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0, column=1, ipadx=30)
        self.controls.pack(side=LEFT)



        self.gif1 = ImageTk.PhotoImage(Image.open('testing_groundtruth-0001.tif')) # a CurrentPrediction kell


        self.c = Canvas(self.master, width=self.gif1.width(), height=self.gif1.height(), bg=self.color_bg, ) #itt fontos, hogy a height és a width a képhez legyen igazítva
        self.c.pack(fill=BOTH, expand=True)

        self.c.create_image(0, 0, image=self.gif1, anchor = NW) #itt töltöm be az image-et a háttérre

        menu = Menu(self.master)
        self.master.config(menu=menu)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Options', menu=optionmenu)
        optionmenu.add_command(label='Clear Canvas', command=self.clear)
        optionmenu.add_command(label='Save Image', command=self.saveImage)


if __name__ == '__main__':
    root = Tk()
    PaintApplication(root)
    root.title('Paint Application')
    root.mainloop()
