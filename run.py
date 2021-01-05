from tkinter import*
from path import WordPath
def main():
    
    root = Tk()
    app = Window(root)
    root.wm_title("Welcome")
    root.geometry("450x300")
    #show window
    root.mainloop()

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
       
        #widget can take all window
        self.pack(fill = BOTH, expand = "yes")
        
        l1 = Label(self, text = "Enter Dicionary:").grid(row = 0, column = 1)
        l2 = Label(self, text = "Enter Word 1:   ").grid(row = 1, column = 1)
        l3 = Label(self, text = "Enter Word 2:   ").grid(row = 2, column = 1)

        self.e1 = Entry(self, show = None, font=('Arial',14),bd=1)
        self.e1.grid(row = 0, column = 2)
        self.e2 = Entry(self, show = None, font=('Arial',14),bd=1)
        self.e2.grid(row = 1, column = 2)
        self.e3 = Entry(self, show = None, font=('Arial',14),bd=1)
        self.e3.grid(row = 2, column = 2)

        enterBttn = Button(self, text ="ADD", command=self.clickEnter).grid(row = 3, column = 2)
        exitButton = Button(self, text = "Exit", command = self.clickExitButton).grid(row=3, column=1)
    
    def clickExitButton(self):
        exit()

    def clickEnter(self):
        dicString= self.e1.get()
        word1 = self.e2.get()
        word2 = self.e3.get()

        wordPath = WordPath(dicString)
        path = wordPath.getStringPath(word1,word2)
        dictionary = wordPath.getDic()

        text =Text(self, width = 50,height = 10)
        text.insert(INSERT,"Dictionary:"+"\t"+str(dictionary)+"\n\nPath Found: "+path)
        text.insert(END,'')
        text.grid(row = 4, column =1,columnspan=2, padx =15, pady = 15)


    def clearAll(self):
        #clear label
        self.e1.delete(0,END)
        self.e2.delete(0,END)
        self.e3.delete(0,END)

main()
