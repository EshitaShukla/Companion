import tkinter as tk
from tkinter import ttk
from tkinter import*

from ttkthemes import themed_tk as tkt
from tkinter import Canvas
from tkinter.constants import *
from PIL import Image, ImageDraw, ImageTk

#Theme chooser
bg1="#8313a6"
bg2="#3056b3"
bg3="#0976b3"
fg3="snow"
fg4="dimgrey"

themel=["arc","black","blue","aquativo","kroc","radiance","keramik","clearlooks","classic","winxpblue","plastik"]
bg1l=["#dcdcdc","#808080","#87ceeb","#8313a6","#ffa500","#110000","#dcdcdc","#faf0e6","#696969","#ffa500","#c0c0c0"]
bg2l=["#c0c0c0","#696969","#191970","#3056b3","#8b4513","#d00001","#dcdcdc","#faf0e6","#dcdcdc","#ffa500","#c0c0c0"]
fg3l=["#696969","#696969","#191970","#0976b3","#8b4513","#d00001","#696969","#a52a2a", "#808080","#a52a2a","#000000"]

theme="blue"
z=2

"""
root_dir_path = os.path.dirname(os.path.realpath(__file__))
p=str(os.path.join(root_dir_path, "Templates"))

Px=p+"/hw"
P=str(os.path.join(root_dir_path, 'hwplastik.png'))

"""
root1=tkt.ThemedTk()
root1.get_themes()
root1.set_theme("aquativo")

basestring=str

def hex2rgb(str_rgb):
    try:
        rgb = str_rgb[1:]

        if len(rgb) == 6:
            r, g, b = rgb[0:2], rgb[2:4], rgb[4:6]
        elif len(rgb) == 3:
            r, g, b = rgb[0] * 2, rgb[1] * 2, rgb[2] * 2
        else:
            raise ValueError()
    except:
        raise ValueError("Invalid value %r provided for rgb color."% str_rgb)

    return tuple(int(v, 16) for v in (r, g, b))

class GradientFrame(Canvas):

    def __init__(self, master, from_color, to_color, width=None, height=None, orient=HORIZONTAL, steps=None, fill=None, **kwargs):
        Canvas.__init__(self, master,**kwargs)
        if steps is None:
            if orient == HORIZONTAL:
                steps = height
            else:
                steps = width

        if isinstance(from_color, basestring):
            from_color = hex2rgb(from_color)

        if isinstance(to_color, basestring):
            to_color = hex2rgb(to_color)

        r,g,b = from_color
        dr = float(to_color[0] - r)/steps
        dg = float(to_color[1] - g)/steps
        db = float(to_color[2] - b)/steps

        if orient == HORIZONTAL:
            if height is None:
                raise ValueError("height can not be None")

            self.configure(height=height, bd=0, highlightthickness=0, relief='ridge')

            if width is not None:
                self.configure(width=width)

            img_height = height
            img_width = self.winfo_screenwidth()

            image = Image.new("RGB", (img_width, img_height), "#FFFFFF")
            draw = ImageDraw.Draw(image)

            for i in range(steps):
                r,g,b = r+dr, g+dg, b+db
                y0 = int(float(img_height * i)/steps)
                y1 = int(float(img_height * (i+1))/steps)

                draw.rectangle((0, y0, img_width, y1), fill=(int(r),int(g),int(b)))
        else:
            if width is None:
                raise ValueError("width can not be None")
            self.configure(width=width)

            if height is not None:
                self.configure(height=height)

            img_height = self.winfo_screenheight()
            img_width = width

            image = Image.new("RGB", (img_width, img_height), "#FFFFFF")
            draw = ImageDraw.Draw(image)

            for i in range(steps):
                r,g,b = r+dr, g+dg, b+db
                x0 = int(float(img_width * i)/steps)
                x1 = int(float(img_width * (i+1))/steps)

                draw.rectangle((x0, 0, x1, img_height), fill=(int(r),int(g),int(b)))

        self._gradient_photoimage = ImageTk.PhotoImage(image)

        self.create_image(0, 0, anchor=NW, image=self._gradient_photoimage)


def g(z):
	root1.set_theme("black")
	global theme
	global bg1
	global bg2
	global bg3
	global fg3
	global fg4
	global P
	theme=themel[z]
	bg1=bg1l[z]
	bg2=bg2l[z]
	bg3="snow"
	fg3="dimgrey"
	fg4=fg3l[z]
	print ("fg4",fg4)
	root1.set_theme(theme)
	root1.config(bg=bg3)
	l1.config(fg=fg3,bg=bg3)
	print(theme)

l1=Label(root1,text="""Click on any of the following to choose a Theme. Then, quit the window.
		Please wait a little after clicking submit""")
l1.grid()

b1=ttk.Button(root1,text="       black      ", command=lambda: g(1))
b1.grid()
b1=ttk.Button(root1,text="        arc          ", command=lambda: g(0))
b1.grid()
b1=ttk.Button(text="   aquativo  ", command=lambda: g(3))
b1.grid()
b1=ttk.Button(text="        blue       ", command=lambda: g(2))
b1.grid()
b1=ttk.Button(text="         kroc      ", command=lambda: g(4))
b1.grid()
b1=ttk.Button(text=" clearlooks  ", command=lambda: g(7))
b1.grid()
b1=ttk.Button(text="   radiance   ", command=lambda: g(5))
b1.grid()
b1=ttk.Button(text="    keramik   ", command=lambda: g(6))
b1.grid()
b1=ttk.Button(text="     classic      ", command=lambda: g(8))
b1.grid()
b1=ttk.Button(text="  winxpblue ", command=lambda: g(9))
b1.grid()
b1=ttk.Button(text="      plastik     ", command=lambda: g(10))
b1.grid()
bp=Button(root1, text="Submit",command=lambda: root1.destroy())
bp.grid()

print(theme)

root1.mainloop()

bg3="snow"
fg3="grey"

class traj(tkt.ThemedTk,tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        
        tkt.ThemedTk.__init__(self)   ##
        self.get_themes()             ##
        self.set_theme(theme)      ##

        self.f=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
        self.f.place(height=50, width=0, x=0, y=0)
        self.f.pack(side="bottom",fill="both",expand=True)
        self.f.grid_rowconfigure(1)
        self.f.grid_columnconfigure(1)
        self.f.config(bg=bg1)

        self.f1=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
        self.f1.place(height=50, width=0, x=0, y=0)
        self.f1.pack(side="bottom",fill="both",expand=True)
        self.f1.grid_rowconfigure(1)
        self.f1.grid_columnconfigure(1)
        self.f1.config(bg=bg2)

        self.f2=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
        self.f2.place(height=50, width=0, x=0, y=0)
        self.f2.pack(side="bottom",fill="both",expand=True)


        self.f2.grid_rowconfigure(1)
        self.f2.grid_columnconfigure(1)
        self.f2.config(bg=bg2)


        self.x=GradientFrame(self.f, from_color=bg2, to_color=bg1, height=35,fill="both")
        self.x.pack(fill="both")

        self.y=GradientFrame(self.f2, from_color="#FFFFFF", to_color=bg2, height=35,fill="both")
        self.y.pack(fill="both")


        q=ttk.Button(self.f1,text="Quit",command=lambda:sys.exit())
        q.pack()

        self.menu=Menu(self,background=fg4,foreground=bg3)
        self.config(menu=self.menu)
        self.submenu=Menu(self.menu,foreground=bg3,background=fg4,activebackground="snow",activeforeground=fg3)

        def g(z,f,f1,f2):
	        f.pack_forget()
	        f1.pack_forget()
	        f2.pack_forget()
	        global theme
	        global bg1
	        global bg2
	        global bg3
	        global fg3
	        global P
	        theme=themel[z]
	        bg1=bg1l[z]
	        bg2=bg2l[z]
	        fg4=fg3l[z]
	        bg3="snow"
	        fg3="dimgrey"

	        f=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
	        f.place(height=50, width=0, x=0, y=0)
	        f.pack(side="bottom",fill="both",expand=True)
	        f.grid_rowconfigure(1)
	        f.grid_columnconfigure(1)
	        f.config(bg=bg1)
	        
	        f1=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
	        f1.place(height=50, width=0, x=0, y=0)
	        f1.pack(side="bottom",fill="both",expand=True)
	        f1.grid_rowconfigure(1)
	        f1.grid_columnconfigure(1)
	        f1.config(bg=bg2)
	        f2=Frame(width=500,height=30, bd=0, highlightthickness=0, relief='ridge')
	        f2.place(height=50, width=0, x=0, y=0)
	        f2.pack(side="bottom",fill="both",expand=True)
	        f2.grid_rowconfigure(1)
	        f2.grid_columnconfigure(1)
	        f2.config(bg=bg2)
	        
	        q=ttk.Button(f1,text="Quit",command=lambda:sys.exit())
	        q.pack()



	        print(theme)
	        self.set_theme(theme)
	        f.config(bg=bg1)
	        f1.config(bg=bg2)
	        self.menu.config(background=fg4,foreground="white")
	        global constant1
	        constant1=1
	        print (constant1)
	        self.submenu.config(foreground=bg3,background=fg4,activebackground="snow",activeforeground=fg3)
	        self.submenu2.config(foreground=bg3,background=fg4,activebackground="snow",activeforeground=fg3)
	        print("pack")

	        self.x=GradientFrame(f, from_color=bg2, to_color=bg1, height=35,fill="both").pack(fill="both")
	        self.y=GradientFrame(f2, from_color="#FFFfff", to_color=bg2, height=35,fill="both").pack(fill="both")
	        self.f=f
	        self.f1=f1
	        self.f2=f2

        #Menu
        self.menu=Menu(self,background=fg4,foreground=bg3)
        self.config(menu=self.menu)

            ##
        self.submenu=Menu(self.menu,foreground=bg3,background=fg4,activebackground="snow",activeforeground=fg3)
        self.menu.add_cascade(label="file",menu=self.submenu)


        a=self.submenu.add_command(label="developer info",command=lambda:self.show_frame(P01))
        b=self.submenu.add_command(label="contact us",command=lambda:self.show_frame(P02))

            ##
        self.submenu2=Menu(self.menu,foreground=bg3,background=fg4,activebackground="snow",activeforeground=fg3)
        self.menu.add_cascade(label="Choose Theme",menu=self.submenu2)


        b1=self.submenu2.add_command(label="     black     ", command=lambda: g(1,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="       arc     ", command=lambda: g(0,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="   aquativo  ", command=lambda: g(3,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="      blue     ", command=lambda: g(2,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="      kroc     ", command=lambda: g(4,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label=" clearlooks  ", command=lambda: g(7,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="   radiance ", command=lambda: g(5,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="   keramik  ", command=lambda: g(6,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="     classic    ", command=lambda: g(8,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label=" winxpblue ", command=lambda: g(9,self.f,self.f1,self.f2))
        b1=self.submenu2.add_command(label="    plastik    ", command=lambda: g(10,self.f,self.f1,self.f2))

        #
        F1=tk.Frame(self)

        F1.pack(side="top",fill="both",expand=True)

        F1.grid_rowconfigure(0,weight=1)
        F1.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (Start,LogIn):
            frame=F(F1,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
            frame.config(bg="snow")

        

        self.show_frame(Start)
    
    def show_frame(self,cont):

        frame=self.frames[cont]
        frame.tkraise()

class Start(tk.Frame):      # LogIn page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        L=Label(self,text="Companion",font="forte 25",fg=fg3,bg=bg3)
        L.grid(row=2,column=0,columnspan=3)

        L1=Label(self,text="    ",font="forte 25",fg=fg3,bg=bg3)
        L1.grid(row=1,column=1, columnspan=3)

        logIn=ttk.Button(self,text="Log In",command=lambda:controller.show_frame(LogIn))
        logIn.grid(sticky=NE,row=0,column=5)

        Front=ttk.Button(self,text="Front",command=lambda:controller.show_frame(P2))
        Front.grid(row=3,column=1)

        Left=ttk.Button(self,text="Left",command=lambda:controller.show_frame(P2))
        Left.grid(row=4,column=0)

        Right=ttk.Button(self,text="Right",command=lambda:controller.show_frame(P2))
        Right.grid(row=4,column=2)

        Back=ttk.Button(self,text="Back",command=lambda:controller.show_frame(P2))
        Back.grid(row=4,column=1)

        L2=Label(self,text="    ",font="forte 25",fg=fg3,bg=bg3)
        L2.grid(column=1)

        Ball=ttk.Button(self,text="Ball",command=lambda:controller.show_frame(P2))
        Ball.grid(column=1)

        Food=ttk.Button(self,text="Food",command=lambda:controller.show_frame(P2))
        Food.grid(column=1)

class LogIn(tk.Frame):      # LogIn page

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        L=Label(self,text="Login",font="forte 25",fg=fg3,bg=bg3)
        L.grid(row=0,column=1, columnspan=3)

        Username=StringVar()
        Password=StringVar()

        l=Label(self,text="                        ",font="forte",bg=bg3)
        l.grid(row=2,column=0)


        L2=Label(self,text="Username: ",font="forte",fg=fg3,bg=bg3)
        L2.grid(row=2,column=1)

        L3=Label(self,text="Password: ",font="forte",fg=fg3,bg=bg3)
        L3.grid(row=3,column=1)

        Us= Entry(self,bd=10,textvariable=Username)
        Us.grid(row=2,column=2)

        Ps= Entry(self,bd=10,textvariable=Password)
        Ps.grid(row=3,column=2)

        Submit=ttk.Button(self,text="User A",command=lambda:controller.show_frame(P2))
        Submit.grid()


    
class P2(tk.Frame):#calculate trajectory-2

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        L1=Label(self,text="P2",font="forte",fg=fg3,bg=bg3)
        L1.pack(pady=10,padx=10)

        Submit=ttk.Button(self,text="Submit",command=lambda:controller.show_frame(Start))
        Submit.pack()



    
root=traj()  

def exit_function():
    # Put any cleanup here.
    sys.exit()
    root.destroy()

root.protocol('WM_DELETE_WINDOW', exit_function)

root.mainloop()
