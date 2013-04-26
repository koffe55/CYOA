import Tkinter

import tkMessageBox as mess
from StoryReader import *
#from PIL import ImageTk, Image
from ttk import Frame, Style


class cyoagui(Tkinter.Tk):

        #Class Objects
    reader = StoryReader(None)
    past = ['Your Recent Choices:']   #list of all choices made.

        #Preferences and Options
    color = 'lavender' #defined in \python27\tools\pynche\X\rgb.txt
    color2 = 'cornflower blue'    #past frame
    color3 = 'cornflower blue'    #choices frame
    color4 = 'black'    #text color
    debug = False

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.v = Tkinter.IntVar()#v is a global variable
        self.v.set(0)        #that holds the int corresponding to a radiobutton
        self.initialize()

    def initialize(self):       #GUI stuff.
        self.grid()

               #frame that contains the entire GUI
        self.frame = Tkinter.Frame(self, bg=self.color)
        self.frame.grid(sticky='NWSE')
        self.frame.rowconfigure('all', minsize = 200)
        self.frame.columnconfigure('all', minsize = 200)

                #entry variable. outdated, just has keybinding now
        self.entryVariable = Tkinter.StringVar()        #holds whats in the box
        self.entry = Tkinter.Entry(self, textvariable = self.entryVariable)
        self.entry.bind("<Return>", self.OnPressEnter)      #Bind <enter> key to an event

       

                #display past choices.
        self.pasttxt = Tkinter.StringVar()
        plabel = Tkinter.Label(self.frame, textvariable=self.pasttxt, anchor='w', fg=self.color4,
                              bg=self.color2, width=100, wraplength=600, justify='left', font=("Arial", 10))
        plabel.grid(column=0, row=10, columnspan=2, rowspan=3, sticky='NWSE')
        self.pasttxt.set(self.past)
       
            #Choices label
        self.choicetxt = Tkinter.StringVar()      
        self.clabel = Tkinter.Label(self.frame, textvariable = self.choicetxt,
                              anchor="w", fg=self.color4, bg=self.color3,
                               relief ='ridge', width=100, wraplength=600, font=("Arial", 12),
                               justify='left')
        self.clabel.grid(column=0, row=0, columnspan=2, rowspan=3, sticky='NWSE')
        self.choicetxt.set(u"Choices will be displayed below.\n")


                #configuartion
        for r in range(7):
            self.rowconfigure(r, weight=1)
        for c in range(4):
            self.columnconfigure(c, weight=1)

        #self.grid_columnconfigure(0, minsize=500, weight=1) 
        self.resizable(False,False)     #make the window resizable horizontally, vertically
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

            #quit button
        quitbutton=Tkinter.Button(self.frame,text=u"Quit", command=self.OnExit)
        quitbutton.grid(column=3,row=0,sticky='NWSE')

            #Restart button
        restartbut = Tkinter.Button(self.frame,text=u"Restart", command=self.OnRestart)
        restartbut.grid(column=3,row=1,sticky='NWSE')

            #Radio buttons
        self.CreateRadio(0)     #Find question zero for initialization.

            #'Next' buttons
        button = Tkinter.Button(self.frame, text=u"Next", command=self.OnNext)
        button.grid(column=3, row=3, sticky='NWSE')
        self.bind("<Return>", self.OnPressEnter)      #Bind <enter> key to an event
        
             #About
        aboutbutton = Tkinter.Button(self.frame, text=u"About", command =self.OnAbout)
        aboutbutton.grid(column=3, row=2, sticky='NWSE',)

    def PastList(self):
        cur = self.v.get()
        i=0
        for i in range(len(self.numbers)):      #find where it matches to get text.
            if (self.numbers[i] == cur):
                temp = [self.choices[i]]
        self.past=self.past + temp #record that choice(string)
        paststr = '\n'.join(self.past)
        self.pasttxt.set(paststr)     #update display
        
    def OnAbout(self):
        try:
            with open ("about.txt", "r") as myfile:
                AboutFile=myfile.read().replace('\xe2\x80\x99', '\'')
                if self.debug: print 'Successfully opened About statement.'
                about = mess.showinfo("About The Project", AboutFile)
        except:
            print("Couldn't find the about.txt file. Printing default message instead.")
            message =  "About us:\n This project was built by Kelsie Renehan and"\
                      " Jeffrey Dowell for their Capstone Project in College Park" \
                      " Scholars Arts. "
            about = mess.showinfo("About The Project", message)
        
    def OnRestart(self):
        ans = mess.askokcancel("Really restart?", "Are you sure you want to restart?")
        if ans == True:
            if self.debug: print 'Restarting from question 0'
            self.ClearRadio()
            self.past = []              #reset past choices list
            self.pasttxt.set(self.past)
            self.CreateRadio(0)
            prompt = self.reader.GetText(0)
            self.choicetxt.set(prompt)


    def OnExit(self):
        ans = mess.askokcancel("Really quit?","Are you sure you want to quit? All story progress will be lost.")
        if ans == True:
            self.destroy()

    def OnPressEnter(self,event):
        self.OnNext()   #Pressing enter is just like clicking next.
        
    def OnNext(self):
        if self.debug: print ("this is the value you chose... "+str(self.v.get()))
        question = self.v.get()
        self.PastList()         #record this choice.
        self.CreateRadio(question)
        prompt = self.reader.GetText(question)
        self.choicetxt.set(prompt)
    
    def ClearRadio(self):
        try:
            self.b
        except:
            if self.debug: print 'Tried to clear radio buttons, but there aren\'t any.'
            return
        for i in range(len(self.b)):
            self.b[i].destroy()


    def CreateRadio(self, question):
        self.ClearRadio()               #clear previous buttons
        data= self.reader.choices(question)
        if not data:
            print 'ERROR, Trying to create radiobuttons but cant get good data'
            exit
        else:
            self.cut(data)
            
    def cut(self, data):                     #unpack text and make buttons.
        self.numbers = data[1::2]
        self.choices = data[::2]
        self.num_buttons = len(self.numbers)     #how many buttons?
        self.b= range(len(self.numbers))         #declare buttons.
        for i in range(len(self.numbers)):
            self.b[i] = Tkinter.Radiobutton(self.frame, text=self.choices[i], background=self.color,
                                       variable=self.v, value=self.numbers[i], wraplength=800, font=("Arial", 11))
            self.b[i].grid(column=0, row=(3+i), sticky='w')
        if self.debug: print "Done creating buttons"

if __name__ == "__main__":
    app = cyoagui(None)
    app.title('Choose Your Own Adventure!')
    app.mainloop() 
    

   

##            #Information Label
##        self.questiontxt = Tkinter.StringVar()        #label for the blue field thing
##        qlabel = Tkinter.Label(self, textvariable = self.questiontxt,
##                              anchor="w", fg="white", bg="blue",
##                               relief='ridge', width=100, wraplength=600,
##                               justify='left')
##        qlabel.grid(column=0, row=0, columnspan=2, rowspan=3, sticky='NW')
##        self.questiontxt.set(u"Ready to play?!\n\n")

            #choices label frame
        #labelframe = Tkinter.LabelFrame(self, text="Here are your options")
        #labelframe.grid(column=0, row=1, sticky='NW')
        #labelframe.pack(fill="both", expand="yes")






            #Image
##        path = "smile.jpg"
##        img = Image.open(path)
##        photo = ImageTk.PhotoImage(img)
##        #picture = Tkinter.PhotoImage(self, image = img)
##        #photo.grid(column=5, row=6, sticky='EW')
##        label7 = Tkinter.Label(image=photo)
##        label7.grid(column=5, row=6)


