from tkinter import *
from tkinter import ttk
import random 
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management Application")
        self.root.geometry("1540x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()



        lable_title=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lable_title.pack(side=TOP,fill=X)

        """****************************Data Frame Main******************************"""        

        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)

        """****************************Data Frame Main left******************************""" 

        dataframe_left=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,text="Patient Information",bg="white",font=("times new roman",12,"bold"))
        dataframe_left.place(x=0,y=5,width=980,height=350)

        """****************************Data Frame Main Right******************************"""
        
        dataframe_right=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=10,text="Prescription",bg="white",font=("times new roman",12,"bold"))
        dataframe_right.place(x=990,y=5,width=500,height=350)

        """****************************Buttons Frame******************************"""
        button_frame=Frame(self.root,bd=20,relief=RIDGE)
        button_frame.place(x=0,y=530,width=1530,height=70)

        """****************************Details Frame******************************"""
        details_frame=Frame(self.root,bd=20,relief=RIDGE)
        details_frame.place(x=0,y=600,width=1530,height=180)

        """**********************Details Frame left in side******************************"""

        lable_name_table=Label(dataframe_left,text="Name Of Tablet",font=("times new roman",12,"bold"),padx=2,pady=6)
        lable_name_table.grid(row=0,column=0)

        combo_box_name_tabl=ttk.Combobox(dataframe_left,font=("times new roman",12,"bold"),textvariable=self.Nameoftablets, width=35)
        combo_box_name_tabl["values"]=("Aspirin", "Paracetamol", "Ibuprofen", "Amoxicillin", "Atorvastatin", "Metformin", "Omeprazole", "Losartan", "Amlodipine", "Lisinopril")
        combo_box_name_tabl.grid(row=0,column=1, sticky=W)

        lable_ref=Label(dataframe_left, font=("arial", 12, "bold"), bg="white",text="Refence No: ",padx=2)
        lable_ref.grid(row=1, column=0, sticky=W)
        txtref=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.ref, bg="white", width=35)
        txtref.grid(row=1, column=1)

        lable_Dose=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Dose", padx=2, pady=4)
        lable_Dose.grid(row=2, column=0, sticky=W)
        txtDose=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.Dose,bg="white", width=35)
        txtDose.grid(row=2, column=1)

        lable_NoOftablets=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="No Of Tablets", padx=2, pady=6)
        lable_NoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.NumberofTablets, bg="white",width=35)
        txtNoOftablets.grid(row=3, column=1)
        
        lable_Lot=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Lot", padx=2,pady=6)
        lable_Lot.grid(row=4, column=0, sticky=W)
        txtLot=Entry(dataframe_left, font=("arial", 13, "bold"),textvariable=self.Lot,bg="white", width=35)
        txtLot.grid(row=4, column=1)

        lable_lissueDate=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Issue Date",padx=2, pady=6)
        lable_lissueDate.grid(row=5, column=0, sticky=W)
        txtissueDate=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.Issuedate,bg="white", width=35)
        txtissueDate.grid(row=5, column=1)

        lable_ExpDate=Label (dataframe_left, font=("arial", 12, "bold"), bg="white",text="Exp Date", padx=2, pady=6)
        lable_ExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.ExpDate, bg="white",width=35)
        txtExpDate.grid(row=6, column=1)

        lable_DailyDose=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Daily Dose", padx=2,pady=4)
        lable_DailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.DailyDose,bg="white", width=35)
        txtDailyDose.grid(row=7, column=1)

        lable_Side_Effect=Label (dataframe_left, font=("arial", 12, "bold"), bg="white",text="Side Effect", padx=2, pady=6)
        lable_Side_Effect.grid(row=8, column=0, sticky=W)
        txtSide_Effect=Entry (dataframe_left, font=("arial", 13, "bold"),textvariable=self.sideEfect, bg="white",width=35)
        txtSide_Effect.grid(row=8, column=1)

        lable_Furtherinfo=Label (dataframe_left, font=("arial", 12, "bold"), bg="white",text="Further Information", padx=2)
        lable_Furtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo=Entry(dataframe_left, font=("arial", 12, "bold"),textvariable=self.FurtherInformation, bg="white",width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lable_Blood_Pressure=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Blood Pressure", padx=2, pady=6)
        lable_Blood_Pressure.grid(row=1, column=2, sticky=W)
        txtBlood_Pressure=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.DrivingUsingMachine,bg="white",width=35)
        txtBlood_Pressure.grid(row=1, column=3)

        lable_Storage=Label(dataframe_left, font=("arial", 12, "bold"), bg="white",text="Storage Advice", padx=2, pady=6)
        lable_Storage.grid(row=2, column=2, sticky=W)
        txtStorage=Entry(dataframe_left, font=("arial", 12, "bold"),textvariable=self.StorageAdvice, bg="white",width=35)
        txtStorage.grid(row=2, column=3)

        lable_Medicine=Label (dataframe_left, font=("arial", 12, "bold"),bg="white", text="Medication", padx=2, pady=6)
        lable_Medicine.grid(row=3, column=2, sticky=W)
        txtMedicine=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.HowToUseMedication, bg="white",width=35)
        txtMedicine.grid(row=3, column=3, sticky=W)

        lable_PatientId=Label(dataframe_left, font=("arial", 12, "bold"),bg="white", text="Patient Id", padx=2, pady=6)
        lable_PatientId.grid(row=4, column=2, sticky=W)
        txtPatientId=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.PatientId, bg="white",width=35)
        txtPatientId.grid(row=4, column=3)

        lable_Nhs_Number=Label (dataframe_left, font=("arial", 12, "bold"),bg="white", text="NHS Number", padx=2, pady=6)
        lable_Nhs_Number.grid(row=5, column=2, sticky=W)
        txtNhs_Number=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.nhsNumber,bg="white", width=35)
        txtNhs_Number.grid(row=5, column=3)

        lable_Patientname=Label (dataframe_left, font=("arial", 12, "bold"), bg="white",text="Patient Name", padx=2, pady=6)
        lable_Patientname.grid(row=6, column=2, sticky=W)
        txtPatientname=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.PatientName,bg="white", width=35)
        txtPatientname.grid(row=6, column=3)

        lable_DateOfBirth=Label (dataframe_left, font=("arial", 12, "bold"),bg="white", text="Date Of Birth", padx=2, pady=6)
        lable_DateOfBirth.grid(row=7, column=2, sticky=W)
        txtDateOfBirth=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.DateOfBirth,bg="white", width=35)
        txtDateOfBirth.grid(row=7, column=3)

        lable_PatientAddress=Label(dataframe_left, font=("arial", 12, "bold"),bg="white",text="Patient Address", padx=2, pady=6)
        lable_PatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress=Entry (dataframe_left, font=("arial", 12, "bold"),textvariable=self.PatientAddress,bg="white", width=35)
        txtPatientAddress.grid(row=8, column=3)

        #****************Data frame right in side******************************************
        
        self.txtPrecription=Text(dataframe_right,font=("arial", 12, "bold"),bg="white", width=50,height=16,padx=2,pady=6)
        self.txtPrecription.grid(row=0,column=0)

        #****************Buttons ******************************************

        button_prescription=Button(button_frame,text="Prescription",font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_prescription.grid(row=0,column=0)

        button_prescription_data=Button(button_frame,text="Prescription Data",command=self.iprescriptiondata,font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_prescription_data.grid(row=0,column=1)

        button_update=Button(button_frame,text="Update",font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_update.grid(row=0,column=2)

        button_delete=Button(button_frame,text="Delete",font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_delete.grid(row=0,column=3)

        button_clear=Button(button_frame,text="Clear",font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_clear.grid(row=0,column=4)

        button_exit=Button(button_frame,text="Exit",font=("arial", 12, "bold"),bg="Green",fg="White", width=14,height=1,padx=0,pady=0)
        button_exit.grid(row=0,column=5)

        #****************Scrolls ******************************************

        scrol_x=ttk.Scrollbar(details_frame,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(details_frame,orient=VERTICAL)

        self.hospital_table=ttk.Treeview(details_frame,columns=("Name_of_tablet","Ref","dose", "nooftablets", "lot", "issuedate","expdate","dailydose", "storage", "nhsnumber", "pname", "dob", "address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)

        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x.config(command=self.hospital_table.xview)
        scrol_y.config(command=self.hospital_table.yview)

        scrol_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scrol_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("Name_of_tablet",text="Name Of Tablet")
        self.hospital_table.heading("Ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("Name_of_tablet",width=100)
        self.hospital_table.column("Ref", width=100)
        self.hospital_table.column("dose", width=100)
        self.hospital_table.column("nooftablets", width=100)
        self.hospital_table.column("lot", width=100)
        self.hospital_table.column("issuedate", width=100)
        self.hospital_table.column("expdate", width=100)
        self.hospital_table.column("dailydose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)
        self.hospital_table.pack(fill=BOTH,expand=1)

        # self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor())

        self.fetch_data()

        #******function ***************
    def iprescriptiondata(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="07042003",database="Patientdata")

            cursor=conn.cursor()

            query=("insert into patient (name_of_tablets, reference_no, dose, no_of_tablets, lot, issue_date, exp_date, daily_dose, storage, nhs_no, patient_name, date_of_birth, patient_address) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            values=(self.Nameoftablets.get(), self.ref.get(), self.Dose.get(), self.NumberofTablets.get(), self.Lot.get(), self.Issuedate.get(), self.ExpDate.get(), self.DailyDose.get(), self.StorageAdvice.get(), self.nhsNumber.get(), self.PatientName.get(), self.DateOfBirth.get(), self.PatientAddress.get())

            cursor.execute(query, values)
            self.fetch_data()
            conn.commit()
        conn.close()

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="07042003",database="Patientdata")


        cursor=conn.cursor()  

        query=("select * from patient")   
        cursor.execute(query)
        rows=cursor.fetchall()
        if rows:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for row in rows:
                values = [value for value in row]
                self.hospital_table.insert("", END, values=values)
            self.hospital_table.pack()
            conn.commit()
        conn.close()


        def get_cursor(self, event):
            cursor_row = self.hospital_table.focus()
            if cursor_row:
                content = self.hospital_table.item(cursor_row)  
                row = content["values"]
                self.Nameoftablets.set(row[0])
                self.ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberofTablets.set(row[3])
                self.Lot.set(row[4])
                self.Issuedate.set(row[5])
                self.ExpDate.set(row[6])
                self.DailyDose.set(row[7])
                self.StorageAdvice.set(row[8])
                self.nhsNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateOfBirth.set(row[11])
                self.PatientAddress.set(row[12])

    # def get_cursor(self,event=""):
    #     cursor_row=self.hospital_table.focus()
    #     content=self.hospital_table.item(cursor_row)  #return Dictionary

    #     row=content["values"]
    #     print(row)
    #     self.Nameoftablets.set(row[0])
    #     self.ref.set(row[1])
    #     self.Dose.set(row[2])
    #     self.NumberofTablets.set(row[3])
    #     self.Lot.set(row[4])
    #     self.Issuedate.set(row[5])
    #     self.ExpDate.set(row[6])
    #     self.DailyDose.set(row[7])
    #     self.StorageAdvice.set(row[8])
    #     self.nhsNumber.set(row[9])
    #     self.PatientName.set(row[10])
    #     self.DateOfBirth.set(row[11])
    #     self.PatientAddress.set(row[12])



       





root=Tk()
obj=Hospital(root)
root.mainloop()       

 # if (len(rows)!=0):
        #     self.hospital_table.delete(*self.hospital_table.get_children())
        #     for i in rows:
        #         self.hospital_table.insert("",END, values=list(i))
        #         conn.commit()
        