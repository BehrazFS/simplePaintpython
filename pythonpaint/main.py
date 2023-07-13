import tkinter
from tkinter import colorchooser
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog

filename = ""
pensize = 1
pencolor = "yellow"
bgcolor = "black"
penshape = "circle"
img = Image.new("RGB", (1180, 680), bgcolor)
draw = ImageDraw.Draw(img)
try:
    win = tkinter.Tk()
    win.geometry("1200x700")
    win.resizable(False, False)
    menubar = tkinter.Menu(win)
    win.configure(menu=menubar)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    configmenu = tkinter.Menu(menubar, tearoff=1)


    def setSize():
        global pensize
        swin = tkinter.Toplevel(win)
        swin.geometry("100x40")
        swin.resizable(False, False)
        swin.attributes('-topmost', 'true')
        swin.grab_set()
        spin = tkinter.Spinbox(swin, from_=1, to=50, )

        def on_closing():
            global pensize
            pensize = int(spin.get())
            #print(pensize)
            swin.destroy()

        swin.protocol("WM_DELETE_WINDOW", on_closing)
        spin.configure(width=1000)
        spin.pack(fill="both", pady=10)
        swin.mainloop()


    configmenu.add_command(label="pen size", command=setSize)


    def setColor():
        global pencolor
        color_code = colorchooser.askcolor(title="pen color")
        pencolor = color_code[1]


    configmenu.add_command(label="pen color", command=setColor)


    def setBColor():
        global bgcolor
        global img
        global draw
        color_code = colorchooser.askcolor(title="pen color")
        bgcolor = color_code[1]
        canvas.configure(bg=str(bgcolor))
        canvas.delete("all")
        img = Image.new("RGB", (1180, 680), str(bgcolor))
        draw = ImageDraw.Draw(img)


    configmenu.add_command(label="page color", command=setBColor)


    def setShape():
        global pensize
        swin = tkinter.Toplevel(win)
        swin.geometry("100x40")
        swin.resizable(False, False)
        swin.attributes('-topmost', 'true')
        swin.grab_set()
        sh = ttk.Combobox(swin, values=("circle", "rectangle"), state="readonly")
        sh.current(0)

        def on_closing():
            global penshape
            penshape = str(sh.get())
            swin.destroy()

        swin.protocol("WM_DELETE_WINDOW", on_closing)
        sh.configure(width=1000)
        sh.pack(fill="both", pady=10)
        swin.mainloop()


    configmenu.add_command(label="pen shape", command=setShape)


    def saveAs():
        global filename
        swin = tkinter.Toplevel(win)
        swin.geometry("100x40")
        swin.resizable(False, False)
        swin.attributes('-topmost', 'true')
        swin.grab_set()
        sh = tkinter.Entry(swin)

        def on_closing():
            global filename
            filename = str(sh.get()) + ".jpg"
            if filename == "":
                filename = "nameless.jpg"
            img.save(filename)
            swin.destroy()

        swin.protocol("WM_DELETE_WINDOW", on_closing)
        sh.configure(width=1000)
        sh.pack(fill="both", pady=10)
        swin.mainloop()


    def save():
        global filename
        if filename == "":
            saveAs()
        else:
            img.save(filename)


    filemenu.add_command(label="save as", command=saveAs)
    filemenu.add_command(label="save", command=save)

    getimg = None


    def loadimg():
        global getimg
        file = filedialog.askopenfilename(
            filetypes=(("Image", "*.png *.jpg *.jpeg *.gif"), ("PNG", "*.png"), ("JPG", "*.jpg"), ("Any file", "*"),))
        if file:
            img2 = Image.open(file)
            img2.thumbnail((1200, 700))
            getimg = ImageTk.PhotoImage(img2)
            canvas.delete("all")
            img.paste(img2, (0, 0))
            canvas.create_image((0, 0), image=getimg, anchor='nw')



    filemenu.add_command(label="load image", command=loadimg)
    menubar.add_cascade(label="file", menu=filemenu)
    menubar.add_cascade(label="configure", menu=configmenu)
    canvas = tkinter.Canvas(win, bg=bgcolor, width=2000, height=2000)


    def drawCircle(event):
        global pensize
        global pencolor
        global penshape
        global draw
        if penshape == "circle":
            canvas.create_oval(event.x - pensize, event.y - pensize, event.x + pensize, event.y + pensize,
                               fill=pencolor,
                               outline=pencolor)
            draw.ellipse((event.x - pensize, event.y - pensize, event.x + pensize, event.y + pensize), fill=pencolor,
                         outline=pencolor)
        if penshape == "rectangle":
            canvas.create_rectangle(event.x - pensize, event.y - pensize, event.x + pensize, event.y + pensize,
                                    fill=pencolor,
                                    outline=pencolor)
            draw.rectangle((event.x - pensize, event.y - pensize, event.x + pensize, event.y + pensize), fill=pencolor,
                           outline=pencolor)


    canvas.bind('<B1-Motion>', drawCircle)
    canvas.bind('<Button-1>', drawCircle)
    canvas.pack(fill='both', padx=10, pady=10)

    win.mainloop()
finally:
    filename = "temp.jpg"
    img.save(filename)
