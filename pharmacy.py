
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime


def main():
    root=Tk()
    app=Window1(root)


class Window1:
    def __init__(self,master):
        self.master=master
        self.master.title("Pharmacy Management System")
        self.master.geometry("1350x750+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()

        self.username=StringVar()
        self.password=StringVar()
        

        


        self.LabelTitle=Label(self.frame,text="Pharmacy Management System",font=("arial",50,"bold"),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)
        



        self.Loginframe1=Frame(self.frame,width=1010,height=300,bd=20,relief="ridge")
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief="ridge")
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3=Frame(self.frame,width=1000,height=200,bd=20,relief="ridge")
        self.Loginframe3.grid(row=3,column=0,pady=2)

        #******************************************************************************************************************


        self.lblusername=Label(self.Loginframe1,text="Username",font=("arial",30,"bold"),bd=22)
        self.lblusername.grid(row=0,column=0)
        self.txtusername=Entry(self.Loginframe1,textvariable=self.username,font=("arial",30,"bold"),bd=22)
        self.txtusername.grid(row=0,column=1)

        
        self.lblpassword=Label(self.Loginframe1,text="Password",font=("arial",30,"bold"),bd=22)
        self.lblpassword.grid(row=1,column=0)
        self.txtpassword=Entry(self.Loginframe1,textvariable=self.password,show="*",font=("arial",30,"bold"),bd=22)
        self.txtpassword.grid(row=1,column=1,padx=85)
        

        #******************************************************************************************************************

        self.btnLogin=Button(self.Loginframe2,text="Login",width=17,font=("arial",20,"bold"),command=self.Login_System)
        self.btnLogin.grid(row=0,column=0)

        self.btnReset=Button(self.Loginframe2,text="Reset",width=17,font=("arial",20,"bold"),command=self.Reset)
        self.btnReset.grid(row=0,column=1)
        

        self.btnExit=Button(self.Loginframe2,text="Exit",width=17,font=("arial",20,"bold"),command=self.iExit)
        self.btnExit.grid(row=0,column=2)


        #********************************************************************************************************************

    
        self.btnRegistration=Button(self.Loginframe3,state=DISABLED,text="Patients Registration System",font=("arial",20,"bold"),command=self.Registration_window)
        self.btnRegistration.grid(row=0,column=0)

        self.btnHospital=Button(self.Loginframe3,state=DISABLED,text="Hospital Management System",font=("arial",20,"bold"),command=self.Hospital_window)
        self.btnHospital.grid(row=0,column=1,padx=37)
        #**********************************************************************************************************************








    def Login_System(self): 

        user = (self.username.get())
        pas  = (self.password.get())
       
        if (user ==str(1234)) and (pas ==str(2345)):

            
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
    
            
            
            tkinter.messagebox.askyesno("Pharmacy Management System","You have entered invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.username.set("")
            self.password.set("")
            self.txtusername.focus()
            
    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.username.set("")
        self.password.set("")
        self.txtusername.focus()



    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
        if self.iExit > 0:
            
            self.master.destroy()
            return
        
    

    
        #**********************************************************************************************************************

    





    def Registration_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window2(self.newWindow)
        

     
    def Hospital_window(self):
        self.newWindow=Toplevel(self.master)
        self.app=Window3(self.newWindow)




class Window2:
    def __init__(self,master):
        self.master=master
        self.master.title("Patients Registration System")
        self.master.geometry("1450x750+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()


   #***************************************************************************************************************************
        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        Postcode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()

        Membership=StringVar()
        Membership.set("0")
        #*****************************************Function Declared********************************************************
        def iExit():
            iExit=tkinter.messagebox.askyesno("Patients Registration System", "Confirm if you want to exit")
            if iExit > 0:
                #root.destroy()
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_of_Member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMembership.config(state=DISABLED)
            #self.btnParent.config(state=NORMAL)

        def iResetRecord():
            
             
            iResetRecord=tkinter.messagebox.askokcancel("Patients Registration Systems","Confirm if you want to addanew record")
            if iResetRecord>0:
                
                Reset()
            elif iResetRecord<=0:
                
                Reset()
                self.txtReceipt.delete("1.0",END)
                return





        def Ref_No():
            x=random.randint(10903,  600873)
            randomRef=str(x)
            Ref.set(randomRef)






        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,"\t"+Ref.get()+"\t\t"+Firstname.get()+"\t\t"+Surname.get()
                                   +"\t\t"+Address.get()+"\t\t"+DateofOrder.get()+"\t\t"+Telephone.get()
                                   +"\t\t"+Membership.get()+"\n")





        def Membership_Fees():
            if (var4.get()==1):
                self.txtMembership.config(state=NORMAL)
                Item1=float(50)
                Membership.set("$"+str(Item1))
            elif(var4.get()==0):
                self.txtMembership.config(state=DISABLED)
                Membership.set("0")
                

   #**************************************************FRAMES********************************************************************




        Mainframe=Frame(self.frame)
        Mainframe.grid()


        TitleFrame=Frame(Mainframe, bd=20, width=1350, padx=26 , relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame, font=("arial",59,"bold"),text="  Patients  Registration System  " , padx=2)
        self.lblTitle.grid()

        
   #***************************************************Lower Frames************************************************************


        MemberDetailsFrame=LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)






        FrameDetails=LabelFrame(MemberDetailsFrame,bd=10,width=880,height=400,relief=RIDGE)
        FrameDetails.pack(side=LEFT)





        MembersName_F=LabelFrame(FrameDetails,bd=10,width=350,height=400,font=("arial",12,"bold"),text="Customer Name",relief=RIDGE)
        MembersName_F.grid(row=0,column=0)





        Receipt_ButtonFrame=LabelFrame(MemberDetailsFrame,bd=10,width=1000,height=400,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
        
    #**********************************************************************************************************************

        self.lblReferenceNo=Label(MembersName_F, font=("arial",14,"bold"),text="Reference No" , bd=7)
        self.lblReferenceNo.grid(row=0,column=0,sticky=W)
        self.txtReferenceNo=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Ref,state=DISABLED,insertwidth=2)
        self.txtReferenceNo.grid(row=0,column=1)


        self.lblFirstname=Label(MembersName_F, font=("arial",14,"bold"),text="Firstname" , bd=7)
        self.lblFirstname.grid(row=1,column=0,sticky=W)
        self.txtFirstname=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Firstname,insertwidth=2)
        self.txtFirstname.grid(row=1,column=1)
        self.txtFirstname.focus()

        self.lblSurname=Label(MembersName_F, font=("arial",14,"bold"),text="Surname" , bd=7)
        self.lblSurname.grid(row=2,column=0,sticky=W)
        self.txtSurname=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Surname,insertwidth=2)
        self.txtSurname.grid(row=2,column=1)

        self.lblAddress=Label(MembersName_F, font=("arial",14,"bold"),text="Address" , bd=7)
        self.lblAddress.grid(row=3,column=0,sticky=W)
        self.txtAddress=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Address,insertwidth=2)
        self.txtAddress.grid(row=3,column=1)

        self.lblPostcode=Label(MembersName_F, font=("arial",14,"bold"),text="Postcode" , bd=7)
        self.lblPostcode.grid(row=4,column=0,sticky=W)
        self.txtPostcode=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Postcode,insertwidth=2)
        self.txtPostcode.grid(row=4,column=1)

        self.lblDate=Label(MembersName_F, font=("arial",14,"bold"),text="Date" , bd=7)
        self.lblDate.grid(row=5,column=0,sticky=W)
        self.txtDate=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=DateofOrder,insertwidth=2)
        self.txtDate.grid(row=5,column=1)


        self.lblTelephone=Label(MembersName_F, font=("arial",14,"bold"),text="Telephone" , bd=7)
        self.lblTelephone.grid(row=6,column=0,sticky=W)
        self.txtTelephone=Entry(MembersName_F, font=("arial",14,"bold"), bd=7,textvariable=Telephone,insertwidth=2)
        self.txtTelephone.grid(row=6,column=1)

        

 

    #**********************************************************************************************************************
        self.lblProve_of_ID=Label(MembersName_F
                                  ,font=("arial",14,"bold"),text="Prove of ID",bd=7)
        self.lblProve_of_ID.grid(row=7,column=0,sticky=W)


        self.cboProve_of_ID=ttk.Combobox(MembersName_F,font=("arial",14,"bold"),textvariable=var1,state="randonly",width=19)
        self.cboProve_of_ID["value"]=("","Pilot Licence","Driving Licence","Passport","Student ID")
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7,column=1)


        self.lblType_of_Member=Label(MembersName_F
                                  ,font=("arial",14,"bold"),text="Type of Member",bd=7)
        
        self.lblType_of_Member.grid(row=8,column=0,sticky=W)


        self.cboType_of_Member=ttk.Combobox(MembersName_F,font=("arial",14,"bold"),textvariable=var2,state="randonly",width=19)
        self.cboType_of_Member["value"]=("","Full Member","Annual Membership","Pay As You Go","Honorary Member")
        self.cboType_of_Member.current(0)
        self.cboType_of_Member.grid(row=8,column=1)



        self.lblMethod_of_Payment=Label(MembersName_F
                                  ,font=("arial",14,"bold"),text="Method of Payment",bd=7)
        self.lblMethod_of_Payment.grid(row=9,column=0,sticky=W)

        self.cboMethod_of_Payment=ttk.Combobox(MembersName_F,font=("arial",14,"bold"),textvariable=var3,state="randonly",width=19)
        self.cboMethod_of_Payment["value"]=("","Visa Card","Master Card","Debit Card","Cash")
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9,column=1)
    #******************************Check Button*******************************************************************************
        self.chkMembership=Checkbutton(MembersName_F,text="Membership Fees",variable=var4,onvalue=1,offvalue=0,
                                       font=("arial",16,"bold"),command=Membership_Fees).grid(row=10,column=0,sticky=W)
        self.txtMembership=Entry(MembersName_F,font=("arial",14,"bold"),textvariable=Membership,bd=7,
                                 insertwidth=2,state=DISABLED,justify=RIGHT)
        self.txtMembership.grid(row=10,column=1)


    #*****************************************Receipt****************************************************************
        self.lblLabel=Label(Receipt_ButtonFrame,font=("arial",10,"bold"),pady=10,
                            text="Member Ref\t Firstname\t Surname\t Address\t\t Date Reg.\t Telephone\tMember Paid",
                            bd=7)
        self.lblLabel.grid(row=0,column=0,columnspan=4)

        self.txtReceipt=Text(Receipt_ButtonFrame,width=112,height=22,font=("arial",10,"bold"))
        self.txtReceipt.grid(row=1,column=0,columnspan=4)

  #*******************************************************Button***************************************************
        self.btnReceipt=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),width=13,
                               text="Receipt",command= Receipt).grid(row=2,column=0)
        self.btnReset=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),width=13,
                               text="Reset",command=iResetRecord).grid(row=2,column=1)
        self.btnExit=Button(Receipt_ButtonFrame,padx=18,bd=7,font=("arial",16,"bold"),width=13,
                               text="Exit",command=iExit).grid(row=2,column=2)
        











    #*****************************************************************************************************************
class Window3:
    def __init__(self,master):
        self.master=master
        self.master.title("Hospital Management System")
        self.master.geometry("1450x750+0+0")
        self.frame=Frame(self.master)
        self.frame.pack()


        cmbNameTablets=StringVar()
        Ref=StringVar()
        Dose=StringVar()
        NumberTablets=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        DailyDose=StringVar()
        PossibleSideEffect=StringVar()
        FurtherInformation=StringVar()
        StorageAdvice=StringVar()
        DrivingUsingMachines=StringVar()
        HowToUseMedication=StringVar()
        PatientID=StringVar()
        PatientNHSNo=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientAddress=StringVar()
        Prescription=StringVar()
        #*********************************Function Declaration***************************************************************

        def iExit():
            iExit=tkinter.messagebox.askyesno("Hospital Management System","Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return
        def iPrescription():
            self.txtPrescription.insert(END,"Name Of Tablets: \t\t\t\t"+   cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,"Reference No: \t\t\t\t"+   Ref.get() + "\n")
            self.txtPrescription.insert(END,"Dose: \t\t\t\t"+   Dose.get() + "\n")
            self.txtPrescription.insert(END,"Number Of Tablets: \t\t\t\t"+   NumberTablets.get() + "\n")
            self.txtPrescription.insert(END,"Lot: \t\t\t\t"+   cmbNameTablets.get() + "\n")
            self.txtPrescription.insert(END,"Issued Date: \t\t\t\t"+   IssuedDate.get() + "\n")
            self.txtPrescription.insert(END,"Exp. Date: \t\t\t\t"+   ExpDate.get() + "\n")
            self.txtPrescription.insert(END,"Daily Dose: \t\t\t\t"+   DailyDose.get() + "\n")
            self.txtPrescription.insert(END,"Possible Side Effect: \t\t\t\t"+   PossibleSideEffect.get() + "\n")
            self.txtPrescription.insert(END,"Further Information: \t\t\t\t"+   FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END,"Storage Advice: \t\t\t\t"+   StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END,"Driving Or Using Machines: \t\t\t\t"+   DrivingUsingMachines.get() + "\n")
            self.txtPrescription.insert(END,"How To Use Medication: \t\t\t\t"+   HowToUseMedication.get() + "\n")
            self.txtPrescription.insert(END,"Patient ID: \t\t\t\t"+   PatientID.get() + "\n")
            self.txtPrescription.insert(END,"NHS Number: \t\t\t\t"+   PatientNHSNo.get() + "\n")
            self.txtPrescription.insert(END,"Patient Name: \t\t\t\t"+   PatientName.get() + "\n")
            self.txtPrescription.insert(END,"Date Of Birth: \t\t\t\t"+   DateOfBirth.get() + "\n")
            self.txtPrescription.insert(END,"Patient Address: \t\t\t\t"+   PatientAddress.get() + "\n")
            


            return
        def iPrescriptionData():
            self.txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t"+ Ref.get()+"\t"+ Dose.get()+"\t\t"+
            NumberTablets.get() + "\t"+ Lot.get()+ "\t"+ IssuedDate.get() +"\t\t"+ ExpDate.get()+"\t"+
            DailyDose.get() + "\t\t"+ StorageAdvice.get() + "\t"+ PatientNHSNo.get() + "\t\t"+ PatientName.get()
                                       + "\t"+ DateOfBirth.get() +"\t"+ PatientAddress.get() + "\n")


            return
        def iDelete():
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return
        def iReset():
            
            cmbNameTablets.set("")
            self.cboNameTablet.current(0)
            Ref.set("")
            Dose.set("")
            NumberTablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            DailyDose.set("")
            PossibleSideEffect.set("")
            FurtherInformation.set("")
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowToUseMedication.set("")
            PatientID.set("")
            PatientNHSNo.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return
        
                







        #*********************************Frame***************************************************************
        
        MainFrame=Frame(self.frame)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame,bd=20,width=1350,padx=20,relief=RIDGE)
        TitleFrame.pack(side=TOP)


        self.lbltitle=Label(TitleFrame,width=39,font=("arial",40,"bold"),text="\tHospital Management Systems\t",padx=8)
        self.lbltitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)


        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        
        DataFrame=Frame(MainFrame,bd=20,width=800,height=300,padx=20,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT=LabelFrame(DataFrame,bd=10,width=450,height=300,padx=20,font=("arial",12,"bold"),text="Patients Information",relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT=LabelFrame(DataFrame,bd=10,font=("arial",12,"bold"),text="Prescription",width=450,height=300,padx=20,relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)



       #*******************************************DataFrameLEFT************************************************** 




        self.lblNameTablet=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Name of Tablets:",padx=2)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state="randonly",
                                        font=("arial",12,"bold"),width=22)
        self.cboNameTablet["value"]=("","Ibuprofren","Co-codamol","Paracetamol","Amlodipine")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Further Information:",padx=2,pady=4)
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=FurtherInformation,width=25)
        self.txtFurtherInfo.grid(row=0,column=3)

        self.lblReferenceNo=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Reference No:",padx=2,pady=4)
        self.lblReferenceNo.grid(row=1,column=0,sticky=W)
        self.txtReferenceNo=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Ref,width=25)
        self.txtReferenceNo.grid(row=1,column=1)

        self.lblStorageAdvice=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=4)
        self.lblStorageAdvice.grid(row=1,column=2,sticky=W)
        self.txtStorageAdvice=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=StorageAdvice,width=25)
        self.txtStorageAdvice.grid(row=1,column=3)

        self.lblDose=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        self.lblDose.grid(row=2,column=0,sticky=W)
        self.txtDose=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Dose,width=25)
        self.txtDose.grid(row=2,column=1)

        self.lblDUseMachine=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Driving Machine:",padx=2,pady=4)
        self.lblDUseMachine.grid(row=2,column=2,sticky=W)
        self.txtDUseMachine=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=DrivingUsingMachines,width=25)
        self.txtDUseMachine.grid(row=2,column=3)

        self.lblNoOfTablets=Label(DataFrameLEFT,font=("arial",12,"bold"),text="No.Of Tablets:",padx=2,pady=4)
        self.lblNoOfTablets.grid(row=3,column=0,sticky=W)
        self.txtNoOfTablets=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=NumberTablets,width=25)
        self.txtNoOfTablets.grid(row=3,column=1)

        self.lblUseMedication=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Medication:",padx=2,pady=4)
        self.lblUseMedication.grid(row=3,column=2,sticky=W)
        self.txtUseMedication=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=HowToUseMedication,width=25)
        self.txtUseMedication.grid(row=3,column=3)

        self.lblLot=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Lot:",padx=2,pady=4)
        self.lblLot.grid(row=4,column=0,sticky=W)
        self.txtLot=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=Lot,width=25)
        self.txtLot.grid(row=4,column=1)

        self.lblPatientID=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Patient ID:",padx=2,pady=4)
        self.lblPatientID.grid(row=4,column=2,sticky=W)
        self.txtPatientID=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=PatientID,width=25)
        self.txtPatientID.grid(row=4,column=3)

        self.lblIssuedDate=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Issued Date:",padx=2,pady=4)
        self.lblIssuedDate.grid(row=5,column=0,sticky=W)
        self.txtIssuedDate=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=IssuedDate,width=25)
        self.txtIssuedDate.grid(row=5,column=1)

        self.lblNHSNumber=Label(DataFrameLEFT,font=("arial",12,"bold"),text="NHS Number:",padx=2,pady=4)
        self.lblNHSNumber.grid(row=5,column=2,sticky=W)
        self.txtNHSNumber=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=PatientNHSNo,width=25)
        self.txtNHSNumber.grid(row=5,column=3)

        self.lblExpDate=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=4)
        self.lblExpDate.grid(row=6,column=0,sticky=W)
        self.txtExpDate=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=ExpDate,width=25)
        self.txtExpDate.grid(row=6,column=1)

        self.lblPatientName=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=4)
        self.lblPatientName.grid(row=6,column=2,sticky=W)
        self.txtPatientName=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=PatientName,width=25)
        self.txtPatientName.grid(row=6,column=3)

        self.lblDailyDose=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=4)
        self.lblDailyDose.grid(row=7,column=0,sticky=W)
        self.txtDailyDose=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=DailyDose,width=25)
        self.txtDailyDose.grid(row=7,column=1)

        self.lblDateOfBirth=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Date Of Birth:",padx=2,pady=4)
        self.lblDateOfBirth.grid(row=7,column=2,sticky=W)
        self.txtDateOfBirth=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=DateOfBirth,width=25)
        self.txtDateOfBirth.grid(row=7,column=3)

        self.lblSideEffect=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=4)
        self.lblSideEffect.grid(row=8,column=0,sticky=W)
        self.txtSideEffect=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=PossibleSideEffect,width=25)
        self.txtSideEffect.grid(row=8,column=1)

        self.lblPatientAddress=Label(DataFrameLEFT,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=4)
        self.lblPatientAddress.grid(row=8,column=2,sticky=W)
        self.txtPatientAddress=Entry(DataFrameLEFT,font=("arial",12,"bold"),textvariable=PatientAddress,width=25)
        self.txtPatientAddress.grid(row=8,column=3)

    #***********************************************DataFrameright***********************************************************************

        self.txtPrescription=Text(DataFrameRIGHT,font=("arial",12,"bold"),width=43,height=14,padx=2,pady=4)
        self.txtPrescription.grid(row=0,column=0)

    #***********************************************ButtonFrame***********************************************************************
        self.btnPrescription=Button(ButtonFrame,text="Prescription",font=("arial",12,"bold"),width=24,bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        self.btnPrescriptionData=Button(ButtonFrame,text="PrescriptionData",font=("arial",12,"bold"),width=24,bd=4,command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame,text="Delete",font=("arial",12,"bold"),width=24,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame,text="Reset",font=("arial",12,"bold"),width=24,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame,text="Exit",font=("arial",12,"bold"),width=24,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=4)



    #***********************************************FrameDetail***********************************************************************
        self.lblLabel=Label(FrameDetail,font=("arial",10,"bold"),padx=8
        ,text="Name of Tablets\tReference No.\t Doseage\t No. of Tablets\t Lot\t Issued Date\t Exp. Date\
\tDaily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address",)
        self.lblLabel.grid(row=0,column=0)
        self.txtFrameDetail=Text(FrameDetail,font=("arial",12,"bold"),width=141,height=4,padx=2,pady=4)
        self.txtFrameDetail.grid(row=1,column=0)

        
if __name__=="__main__":
    main()
    

        
