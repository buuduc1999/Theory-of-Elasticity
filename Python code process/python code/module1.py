import numpy as np
from sympy import solve
from sympy.abc import x, y, z
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def matrix(a,b,c,d,e,f,g,h,i):
    return np.array([[a,b,c],[d,e,f],[g,h,i]])
class ungsuat:
    def __init__(self,*args):
        if ( len(args)==1):
            self.a= args[0]
        else:
            bd=args[0]
            E=args[1]
            v=args[2]
            G=E/(2*(1+v))
            K=(1/E)*np.array([[1,-v,-v],[-v,1,-v],[-v,-v,1]])
            ax,ay,az=np.linalg.solve(K,[bd[0,0],bd[1,1],bd[2,2]])
            axy=bd[0,1]*2*G
            axz=bd[0,2]*2*G
            ayz=bd[1,2]*2*G
            self.a=np.array([[ax,axy,axz],[axy,ay,ayz],[axz,ayz,az]])
    def get_us(self):
        return self.a
    def invariant(self):
        t1= np.linalg.det(np.array([[self.a[0,0],self.a[0,1]],[self.a[1,0],self.a[1,1]]]))
        t2= np.linalg.det(np.array([[self.a[1,1],self.a[1,2]],[self.a[2,1],self.a[2,2]]]))
        t3= np.linalg.det(np.array([[self.a[0,0],self.a[0,2]],[self.a[2,0],self.a[2,2]]]))
        I1=self.a[1,1]+self.a[2,2]+self.a[0,0]
        I2=t1+t2+t3
        I3=np.linalg.det(self.a)
        return I1,I2,I3
    def uschinh(self):
        return np.sort(np.roots([1,-self.invariant()[0],+self.invariant()[1],-self.invariant()[2]]))[: : -1]
    def phuongchinh(self,i):
        i=i-1
        f=self.a-np.diag([self.uschinh()[i],self.uschinh()[i],self.uschinh()[i]])
        k=solve([f[0,0]*x+f[0,1]*y+f[0,2]*z,f[1,0]*x+f[1,1]*y+f[1,2]*z,x**2+y**2+z**2-1],dict=True)
        return k
    def usthuytinh(self):
        return self.invariant()[0]/3
    def uscau(self):
        k=self.usthuytinh()
        return np.diag([k,k,k])
    def uslech(self):
        return self.a-self.uscau()
    def mohr(self):
        a,b,c=self.uschinh()
        A=abs(a)
        C=abs(c)
        fig, ax = plt.subplots()
        ax.set_xlim((-(A+C),(A+C)))
        ax.set_ylim((-(A+C),(A+C)))
        ax.add_artist(Circle(((a+c)/2,0),(a-c)/2))
        ax.add_artist(Circle(((b+c)/2,0),(b-c)/2,color="Red"))
        ax.add_artist(Circle(((a+b)/2,0),(a-b)/2,color="Black"))
        plt.show()
    
class biendang:
    def __init__(self,*args):
        if ( len(args)==1):
            self.a= args[0]
        else:
            us=args[0]
            E=args[1]
            v=args[2]
            G=E/(2*(1+v))
            ax=1/E*(a[0,0]-v*(a[1,1]+a[2,2]))
            ay=1/E*(a[1,1]-v*(a[0,0]+a[2,2]))
            az=1/E*(a[2,2]-v*(a[0,0]+a[1,1]))
            axy=us[0,1]/(2*G)
            axz=us[0,2]/(2*G)
            ayz=us[1,2]/(2*G)
            self.a=np.array([[ax,axy,axz],[axy,ay,ayz],[axz,ayz,az]])
    def get_bd(self):
        return self.a
    def invariant(self):
        t1= np.linalg.det(np.array([[self.a[0,0],self.a[0,1]],[self.a[1,0],self.a[1,1]]]))
        t2= np.linalg.det(np.array([[self.a[1,1],self.a[1,2]],[self.a[2,1],self.a[2,2]]]))
        t3= np.linalg.det(np.array([[self.a[0,0],self.a[0,2]],[self.a[2,0],self.a[2,2]]]))
        I1=self.a[1,1]+self.a[2,2]+self.a[0,0]
        I2=t1+t2+t3
        I3=np.linalg.det(self.a)
        return I1,I2,I3
    def bdchinh(self):
        return np.sort(np.roots([1,-self.invariant()[0],+self.invariant()[1],-self.invariant()[2]]))[: : -1]
    def phuongchinh(self,i):
        i=i-1
        f=self.a-np.diag([self.bdchinh()[i],self.bdchinh()[i],self.bdchinh()[i]])
        k=solve([f[0,0]*x+f[0,1]*y+f[0,2]*z,f[1,0]*x+f[1,1]*y+f[1,2]*z,x**2+y**2+z**2-1],dict=True)
        return k
    def bdthuytinh(self):
        return self.invariant()[0]/3
    def bdcau(self):
        k=self.bdthuytinh()
        return np.diag([k,k,k])
    def bdlech(self):
        return self.a-self.bdcau()
    def mohr(self):
        a,b,c=self.bdchinh()
        A=abs(a)
        C=abs(c)
        fig, ax = plt.subplots()
        ax.set_xlim((-(A+C),(A+C)))
        ax.set_ylim((-(A+C),(A+C)))
        ax.add_artist(Circle(((a+c)/2,0),(a-c)/2))
        ax.add_artist(Circle(((b+c)/2,0),(b-c)/2,color="Red"))
        ax.add_artist(Circle(((a+b)/2,0),(a-b)/2,color="Black"))
        plt.show()

import tkinter as tk






































class GUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("BAI TAP LON LY THUYET DAN HOI")
        self.pack(fill="both", expand=True)
        self.Introduce()
       

        
    def matrix(self,a,b,c,d,e,f,g,h,i):
        return np.array([[float(a),float(b),float(c)],[float(d),float(e),float(f)],[float(g),float(h),float(i)]])
    def Introduce(self):
        self.showinstruct()
        self.first=tk.Frame(self,borderwidth=5)
        self.first.pack(fill="both")
        
        tk.Label(self.first, text="BÀI TẬP LỚN LÝ THUYẾT ĐÀN HỒI", width=50,fg="blue",font=100).grid()
        self.matrixinput("NHẬP MA TRẬN")
        self.importinput()
        self.nutOK1()

    def matrixinput(self,text):
        tk.Label(self.first, text=text,anchor="w").grid(row=1) #in dong chu text ra man hinh
        matran=tk.Frame(self.first)
        matran.grid(row=2)
        self.xx=tk.Entry(matran,font=30,width=3)
        self.xx.grid(row=0,padx=5,pady=5)
        self.xy=tk.Entry(matran,font=30,width=3)
        self.xy.grid(row=0,column=1,padx=5,pady=5)
        self.xz=tk.Entry(matran,font=30,width=3)
        self.xz.grid(row=0,column=2,padx=5,pady=5)
        self.yx=tk.Entry(matran,font=30,width=3)
        self.yx.grid(row=1,padx=5,pady=5)
        self.yy=tk.Entry(matran,font=30,width=3)
        self.yy.grid(row=1,column=1,padx=5,pady=5)
        self.yz=tk.Entry(matran,font=30,width=3)
        self.yz.grid(row=1,column=2,padx=5,pady=5)
        self.zx=tk.Entry(matran,font=30,width=3)
        self.zx.grid(row=2,padx=5,pady=5)
        self.zy=tk.Entry(matran,font=30,width=3)
        self.zy.grid(row=2,column=1,padx=5,pady=5)
        self.zz=tk.Entry(matran,font=30,width=3)
        self.zz.grid(row=2,column=2,padx=5,pady=5)
    def importinput(self):
        def tester(self):
            if check.get()==1:
                print(check.get())
                E1.grid(column=0,row=1,pady=3)
                E.grid(column=1,row=1,pady=3)
                v1.grid(column=0,row=2,pady=3)
                v.grid(column=1,row=2,pady=3)
            elif check.get()==0:
                print(check.get())

                E1.grid_remove()
                E.grid_remove()
                v.grid_remove()
                v1.grid_remove()
        check=tk.IntVar()
        ipip=tk.Frame(self.first)
        ipip.grid(row=2,column=1)
        a=tk.Checkbutton(ipip,text="các hằng số Hook",var=check,command=lambda: tester(self))
        a.grid(columnspan=2)
        self.check=check.get()
        E1=tk.Label(ipip,text="nhập E: ")
        E=tk.Entry(ipip,width=5)
        v1=tk.Label(ipip,text="nhập v: ")
        v=tk.Entry(ipip,width=5)
        self.v=v.get()
        self.E=E.get()
#        E1.grid(column=0,row=1)
#        E.grid(column=1,row=1)
#        v1.grid(column=0,row=2)
#        v.grid(column=1,row=2)
        
    def matrixoutput(self,text):
       
        if text=="ma trận ứng suất":
            j=self.US
            matran=tk.Frame(self.test)
            matran.grid()
        elif text=="ma trận biến dạng":
            j=self.BD
            matran=tk.Frame(self.test1)
            matran.grid()
        matrix=tk.Frame(matran,bg="blue")
        matrix.grid(row=0,column=1,pady=3)
        tk.Label(matran,text= str(self.E),font=20,fg="blue").grid(row=0,column=0,padx=10)
        tk.Button(matran,text="biểu đồ Mohr", command= lambda: self.showMohr(text)).grid(row=0,column=3,padx=10)
        for m in range(3):
            for n in range(3):
                tk.Label(matrix,text=str(round(j[m,n],3)),width=4,font=20).grid(row=m,column=n,padx=1,pady=1)  
        
    def showinstruct(self):
        self.instruct=tk.Frame(self)
        
        tk.Button(self.instruct,text="nhập số liệu",command=lambda:GG(self)).pack(side="left")
        self.ungsuat=tk.Button(self.instruct,text="Các số liệu ứng suất",command=lambda:WDUS(self))
        self.biendang=tk.Button(self.instruct,text="Các số liệu biến dạng",command=lambda:WDBD(self))
        def GG(self):
            self.output.forget()
            self.first.pack()
        def WDUS(self):
            self.first.forget()
            self.output.forget()
            self.checkevent("us")
        def WDBD(self):
            self.first.forget()
            self.output.forget()
            self.checkevent("bd")
        
        
        
    def showMohr(self,text):
        if text=="ma trận ứng suất":
            self.doituongus.mohr()
        elif text=="ma trận biến dạng":
            self.doituongbd.mohr()
        
    def nutOK1(self):
        nut=tk.Frame(self.first)
        self.WTF="us"
        nut.grid(row=6,column=0)
        a=tk.Button(nut,text="OK! bắt đầu tính toán ", command= lambda: self.checkevent(self.WTF,True))
        a.grid(columnspan = 2)
        
    def checkevent(self,WTF,A=False):
            # hien so lieu tren thanh instruct
            
            if self.WTF=="us" and self.check==0:
                self.ungsuat.pack(side="left")
            if self.WTF=="bd" and self.check==0:
                    self.biendang.pack(side="left")
            if self.check==1:
                 self.ungsuat.pack(side="left")
                 self.biendang.pack(side="left")
            self.instruct.pack()
            print(self.E)
            ##
            self.first.forget()
            self.output=tk.Frame(self)
            self.output.pack(fill="both")
            self.test=tk.Frame(self.output,borderwidth=5)
            self.test.grid(row=1,column=0)
            self.test1=tk.Frame(self.output,borderwidth=5)
            self.test1.grid(row=1,column=1)
            if self.WTF=="us":
                if A==True:
                    self.US=self.matrix(self.xx.get(),self.xy.get(),self.xz.get(),self.yx.get(),self.yy.get(),self.yz.get(),self.zx.get(),self.zy.get(),self.zz.get())
                self.ungsuatmain()
                if self.check==1:
                    self.BD=biendang(self.US,self.E,self.v)
            if self.WTF=="bd":
                if A==True:
                       self.BD=self.matrix(self.xx.get(),self.xy.get(),self.xz.get(),self.yx.get(),self.yy.get(),self.yz.get(),self.zx.get(),self.zy.get(),self.zz.get())
                self.biendangmain()
                if self.check==1:
                    self.US=ungsuat(self.US,U,V)

    def ungsuatmain(self):
            
        self.doituongus=ungsuat(self.US)
        self.matrixoutput("ma trận ứng suất")
        self.showinvariant_us()
        self.showuschinh()
        self.showphuongchinh_us()
        self.showusthuytinh()
        self.showuscau()
        self.showuslech()
    def showinvariant_us(self):
        invariant=tk.Frame(self.test)
        invariant.grid(row=7)

        b=self.doituongus.invariant()
        k=["I[1]","I[2]","I[3]"]
        tk.Label(invariant,text="Các bất biến [ I(1) I(2) I(3) ]: ",font=10).grid(columnspan=3)
        for i in range(3):
            txt =k[i]+": "+ str(round(b[i],3))
            tk.Label(invariant,text=txt,font=20,width=15).grid(row=8,column=i)
    def showuschinh(self):
        uschinh=tk.Frame(self.test)
        uschinh.grid(row=9)
        b=self.doituongus.uschinh()
        k=["σx","σy","σz"]
        tk.Label(uschinh,text="ứng suất chính [σx,σy,σz]: ",font=10).grid(columnspan=3)
        for i in range(3):
            txt =k[i]+": "+ str(round(b[i],3))
            tk.Label(uschinh,text=txt,font=20,width=15).grid(row=9,column=i)
    def showphuongchinh_us(self):
        phuongchinh=tk.Frame(self.test)
        phuongchinh.grid(row=10)
        k=["phương chính thứ 1","phương chính thứ 2","phương chính thứ 3"]
        tk.Label(phuongchinh,text="các phương chính: ",font=10).grid(columnspan=3)
        for i in range(3):
            M=tk.Frame(phuongchinh)
            M.grid(row=i,column=1)
            j=self.doituongus.phuongchinh(i+1)
            tk.Label(phuongchinh,text=k[i],font=20,width=20,height=2,anchor="w").grid(row=i,column=0,pady=10)
            for m in range(2):
                txt= "X= " +str(round(j[m][x],3)) + "   Y= "+ str(round(j[m][y],3))+ "   Z= " +str(round(j[m][z],3))
                tk.Label(M,text=txt,font=20).pack()
    def showusthuytinh(self):
        usthuytinh=tk.Frame(self.test)
        usthuytinh.grid(row=15);
        j=self.doituongus.usthuytinh()
        txt= "ứng suất thuỷ tĩnh: " + str(round(j,3))
        tk.Label(usthuytinh,text=txt,font=20).grid()
    def showuscau(self):
        usthuytinh=tk.Frame(self.test)
        usthuytinh.grid(row=16);
        j=self.doituongus.uscau()
        matrix=tk.Frame(usthuytinh,bg="red")
        matrix.grid(row=0,column=1)
        tk.Label(usthuytinh,text= "ứng suất cầu: ",font=20,fg="red").grid(row=0,column=0)
        for m in range(3):
            for n in range(3):
                tk.Label(matrix,text=str(round(j[m,n],3)),width=4,font=20).grid(row=m,column=n,padx=1,pady=1)
    def showuslech(self):
        usthuytinh=tk.Frame(self.test)
        usthuytinh.grid(row=17,pady=5);
        j=self.doituongus.uslech()
        matrix=tk.Frame(usthuytinh,bg="blue")
        matrix.grid(row=0,column=1,pady=3)
        tk.Label(usthuytinh,text= "ứng suất lệch: ",font=20,fg="blue").grid(row=0,column=0)
        for m in range(3):
            for n in range(3):
                tk.Label(matrix,text=str(round(j[m,n],3)),width=4,font=20).grid(row=m,column=n,padx=1,pady=1)
    
    
    
    
    
    
    def biendangmain(self):
        self.doituongbd=biendang(self.US)
        self.matrixoutput("ma trận biến dạng")
        self.showinvariant_bd()
        self.showbdchinh()
        self.showphuongchinh_bd()
        self.showbdthuytinh()
        self.showbdcau()
        self.showbdlech()
    def showinvariant_bd(self):
        invariant=tk.Frame(self.test1)
        invariant.grid(row=7)
        
        b=self.doituongbd.invariant()
        k=["I[1]","I[2]","I[3]"]
        tk.Label(invariant,text="Các bất biến [ I(1) I(2) I(3) ]: ",font=10).grid(columnspan=3)
        for i in range(3):
            txt =k[i]+": "+ str(round(b[i],3))
            tk.Label(invariant,text=txt,font=20,width=15).grid(row=8,column=i)
    def showbdchinh(self):
        bdchinh=tk.Frame(self.test1)
        bdchinh.grid(row=9)
        b=self.doituongbd.bdchinh()
        k=["σx","σy","σz"]
        tk.Label(bdchinh,text="biến dạng chính [σx,σy,σz]: ",font=10).grid(columnspan=3)
        for i in range(3):
            txt =k[i]+": "+ str(round(b[i],3))
            tk.Label(bdchinh,text=txt,font=20,width=15).grid(row=9,column=i)
    def showphuongchinh_bd(self):
        phuongchinh=tk.Frame(self.test1)
        phuongchinh.grid(row=10)
        k=["phương chính thứ 1","phương chính thứ 2","phương chính thứ 3"]
        tk.Label(phuongchinh,text="các phương chính: ",font=10).grid(columnspan=3)
        for i in range(3):
            M=tk.Frame(phuongchinh)
            M.grid(row=i,column=1)
            j=self.doituongbd.phuongchinh(i+1)
            tk.Label(phuongchinh,text=k[i],font=20,width=20,height=2,anchor="w").grid(row=i,column=0,pady=10)
            for m in range(2):
                txt= "X= " +str(round(j[m][x],3)) + "   Y= "+ str(round(j[m][y],3))+ "   Z= " +str(round(j[m][z],3))
                tk.Label(M,text=txt,font=20).pack()
    def showbdthuytinh(self):
        bdthuytinh=tk.Frame(self.test1)
        bdthuytinh.grid(row=15);
        j=self.doituongbd.bdthuytinh()
        txt= "biến dạng thuỷ tĩnh: " + str(round(j,3))
        tk.Label(bdthuytinh,text=txt,font=20).grid()
    def showbdcau(self):
        usthuytinh=tk.Frame(self.test1)
        usthuytinh.grid(row=16);
        j=self.doituongbd.bdcau()
        matrix=tk.Frame(usthuytinh,bg="red")
        matrix.grid(row=0,column=1)
        tk.Label(usthuytinh,text= "biến dạng cầu: ",font=20,fg="red").grid(row=0,column=0)
        for m in range(3):
            for n in range(3):
                tk.Label(matrix,text=str(round(j[m,n],3)),width=4,font=20).grid(row=m,column=n,padx=1,pady=1)
    def showbdlech(self):
        usthuytinh=tk.Frame(self.test1)
        usthuytinh.grid(row=17,pady=5)
        j=self.doituongbd.bdlech()
        matrix=tk.Frame(usthuytinh,bg="blue")
        matrix.grid(row=0,column=1,pady=3)
        tk.Label(usthuytinh,text= "biến dạng lệch: ",font=20,fg="blue").grid(row=0,column=0)
        for m in range(3):
            for n in range(3):
                tk.Label(matrix,text=str(round(j[m,n],3)),width=4,font=20).grid(row=m,column=n,padx=1,pady=1)
g=tk.Tk()
#g.geometry("600x800+300+300")
a=GUI(g)
a.mainloop()

#g=ungsuat(4,-2,1,-2,3,5,1,5,-1)
#print(g.invariant())
#print(g.uschinh())

#print(g.phuongchinh(1))
#j=g.phuongchinh(2)
#print(j[0][x])
#print(g.uslech())
#g.mohr()
#a=ungsuat(a,4,5)
#print(a.invariant())
#a.mohr()
#g=biendang(a,4,5)
#g.mohr()
#a=np.array([[4,-2,1],[-2,3,5],[1,5,-1]])
#
