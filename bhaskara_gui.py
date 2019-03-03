from math import *
from tkinter import *
class app:
 x1,x2=0.0,0.0
 def __init__(self,toplevel):
  toplevel.title('TBhaskara')
  
  self.frm=Frame(toplevel)
  self.frm2=Frame(toplevel)
  self.frm.pack()
  self.frm2.pack()
  
  Label(self.frm,text='TBhaskara 0.1 por Lucas Nogueira').pack()
  
  Label(self.frm2,text='Coeficiente A:').pack()
  self.ae=Entry(self.frm2)
  self.ae.pack()

  Label(self.frm2,text='Coeficiente B:').pack()
  self.be=Entry(self.frm2)
  self.be.pack()  

  Label(self.frm2,text='Coeficiente C:').pack()
  self.ce=Entry(self.frm2)
  self.ce.pack()

  self.button=Button(self.frm2)
  self.button['text']='Calcula'
  self.button.bind('<Button-1>',self.calc)
  self.button.pack()

  self.raizes=Label(self.frm2)
  self.raizes['text']=''
  self.raizes.pack()

 def calc(self,event):
  a=float(self.ae.get())
  b=float(self.be.get())
  c=float(self.ce.get())

  delta=pow(b,2) - (4*a*c)
  if delta == 0:
   self.x1=-b/2*a
   self.x2=self.x1
   self.raizes['text']='X1 = %f  | X2 = %f' %(self.x1,self.x2)
   self.raizes.pack()
  elif delta > 0:
   self.x1=(-b + sqrt(delta)) / (2*a)
   self.x2=(-b - sqrt(delta)) / (2*a)
   self.raizes['text']='X1 = %f  | X2 = %f' %(self.x1,self.x2)
   self.raizes.pack()
  elif delta < 0:
      self.raizes['text']='raizes complexas'
      self.raizes.pack()
root=Tk()
app(root)
root.mainloop()
