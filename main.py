import smtplib
import tkinter
import customtkinter
import database as db
import CTkMessagebox



class AppNot(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.Frame1 = customtkinter.CTkFrame(self)
        self.geometry("600x500")
        self.title('Notification app')
        self.button = customtkinter.CTkButton(self.Frame1, text='Register', command=self.look_if_there_is_account)
        self.button.grid(row=4, column=2, padx=10, pady=5)
        self.e1 = customtkinter.CTkEntry(self.Frame1)
        self.e1.grid(row = 2, column = 2,padx=10, pady=5,sticky='ew')
        self.e2 = customtkinter.CTkEntry(self.Frame1)
        self.e2.grid(row=3, column=2 , padx=10, pady=5,sticky='ew')
        self.l1 = customtkinter.CTkLabel(self.Frame1 , text='Password')
        self.l1.grid(row=3 , column= 1,padx= 10, pady=5, sticky='ew')
        self.l2 = customtkinter.CTkLabel(self.Frame1, text='Email')
        self.l2.grid(row=2, column=1, padx= 10, pady=5, sticky='ew')
        self.Frame1.pack()


    def create_account(self):

        new_user = (self.e1.get(), self.e2.get())
        db.add_data(new_user)

    def look_if_there_is_account(self):
        data = db.get_data(self.e1.get())
        print(data)
        if data is not None:
            CTkMessagebox.CTkMessagebox(title='Warning',message='There is account with this email, try to log in')
            self.load_second_frame()
        else:
            self.create_account()


    def load_second_frame(self):
        self.Frame1.destroy()
        self.Frame2 = customtkinter.CTkFrame(self)
        button_2 = customtkinter.CTkButton(self.Frame2, text='Log in', command=self.log_in)
        button_2.grid(row=4, column=2, padx=10, pady=5)
        self.e1_2 = customtkinter.CTkEntry(self.Frame2)
        self.e1_2.grid(row=2, column=2, padx=10, pady=5, sticky='ew')
        self.e2_2 = customtkinter.CTkEntry(self.Frame2)
        self.e2_2.grid(row=3, column=2, padx=10, pady=5, sticky='ew')
        l1_2 = customtkinter.CTkLabel(self.Frame2, text='Password')
        l1_2.grid(row=3, column=1, padx=10, pady=5, sticky='ew')
        l2_2 = customtkinter.CTkLabel(self.Frame2, text='Email')
        l2_2.grid(row=2, column=1, padx=10, pady=5, sticky='ew')
        self.Frame2.pack()

    def log_in(self):
        data = db.get_data(self.e1_2.get())

        if data:
            if data[2] == self.e2_2.get():
                self.load_third_frame(self.e1_2.get())
            else:
                CTkMessagebox.CTkMessagebox(title='Warning', message='Incorrect password')

    def load_third_frame(self, email):
        self.Frame2.destroy()

        plans = db.get_all_planes_with_this_email(email)
        print(plans)
        self.Frame3 = customtkinter.CTkFrame(self)
        self.Frame3.pack()
        plans_m = []
        i = 1
        for p in plans:
            print(p[1])
            label = customtkinter.CTkLabel(self.Frame3,text=f'{p[1]}')
            label.pack()
            plans_m.append(label)
        # there can be a button near to label for delete plan

        self.e_p = customtkinter.CTkEntry(self.Frame3)
        self.e_p.pack()
        self.button_p = customtkinter.CTkButton(self.Frame3,text='Add plane', command=lambda:self.add_plan(email, self.e_p.get()))
        self.button_p.pack()

    def add_plan(self,email, plane):
        if plane != '':
            db.add_plan(email, plane)
            self.Frame3.destroy()
            self.load_third_frame(email)
        else:
            CTkMessagebox.CTkMessagebox(title='Warining', message='incorrect plane!')

    def delete_plane(self, plane:str):
        db.delete_plan(plane)


    def sending_emails(self):
        emails = db.get_all_planes_with_this_email()
        sender = "any_sender"
        smptObj = smtplib.SMTP('localhost')
        for e in emails:
            planes = db.get_all_planes_with_this_email(e[1])
            smptObj.sendmail(sender, e[1], f'You got planes to do! {planes}')










app = AppNot()



app.mainloop()
