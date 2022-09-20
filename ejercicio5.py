
from tkinter import *
import re
from tkinter.ttk import Treeview
import geocoder



class App():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('600x400')
        self.root.resizable(width=False,height=False)
        self.root.title('Geolocalizador IPs')
        label = Label(self.root,text="Geolocalizar IP")
        label.pack(side=TOP)


        self.text = Frame(self.root)
        self.text.pack(side=TOP)
        self.bottomFrame = Frame(self.root)
        self.bottomFrame.pack(side=BOTTOM)

        self.t1 = Entry(self.text,width=40)
        self.t1.grid(row=0,column=0,padx=10,pady=10)
       

        self.b1=Button(self.text,text='añandir',command=lambda:self.validate(1))
        self.b1.grid(row=0,column=1,padx=10,pady=10)
       

        self.l1=Label(self.text,text='...')
        self.l1.grid(row=0,column=2)
       

        self.btnExit=Button(self.bottomFrame,text="salir",command=self.root.destroy)
        self.btnExit.pack(side=LEFT)
        self.btnClean=Button(self.bottomFrame,text="limpiar",command=self.clean)
        self.btnClean.pack(side=LEFT)

        frm = Frame(self.root)
        frm.pack(side=LEFT,padx=20)


        self.tv = Treeview(frm,columns=(1,2,3),show="headings",height="5")
        self.tv.pack()

        self.tv.heading(1,text="Id")
        self.tv.heading(2,text="IP")
        self.tv.heading(3,text="Ciudad")
       

        self.ipInfo = []
        self.k = 0


        self.root.mainloop()


    def addElement(self,ip):
        self.k += 1
        #for i in range(0,self.k):
        ipG = geocoder.ip(ip)
        self.ipInfo.append((self.k,ip,ipG.city))
        
        
        self.tv.insert('','end',values=self.ipInfo[self.k-1])

        

    def clean(self):
        self.t1.delete(first=0,last='end')
        self.l1.config(fg='black',text='...')

    def validate(self,num):
        if(num==1):
            txtValidate=self.t1.get()
            x=re.search("[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",txtValidate)
            if(x):
                self.addElement(txtValidate)
                self.l1.config(fg="green",text="IPv4 valida")
            else:
                self.l1.config(fg="red",text="IPv4 invalida")
            self.t1.delete(first=0,last='end')
App()

