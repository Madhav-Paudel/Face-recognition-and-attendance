import tkinter as tk
import cv2
from PIL import Image, ImageTk
import util
# defining a class
class App:
    # defining constructor
    def __init__(self):
        self.main_window = tk.Tk()
        # this define the window size
        self.main_window.geometry("1200x520+350+100")

        x_position = 750
        login_y = 300
        gap = 20

        # login button
        self.login_button_main_window = util.get_button(
            self.main_window, 'Login', 'green', self.login)
        self.login_button_main_window.place(x=x_position, y=login_y)

        # register button with gap below login button
        self.register_new_user_button_main_window = util.get_button(
            self.main_window, 'Register New User', 'gray', self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=x_position, y=login_y + self.login_button_main_window.winfo_reqheight() + gap)

        # update geometry to ensure buttons are drawn before measuring
        self.main_window.update_idletasks()
        # for webcam label 
        self.webcam_label=util.get_img_label(self.main_window)

        self.webcam_label.place(x=10,y=0,width=700,height=500)
            # for adding webcam
        self.add_webcam(self.webcam_label)
    
        def add_webcam(self, label):
            if 'cap'  not in self.__dict__:
              self.cap=cv2.VideoCapture(0)

            
            self._label=label
            self.process_webcam()

    def process_webcam(self):
        ret,frame=self.cap.read()
        self.most_recent_capture_arr=frame

        img_=cv2.cvtcolor(self.most_recent_capture_arr,cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil=Image.fromarray(img_)

        imgtk=ImageTk.PhotoImage(image=most_recent_capture_pil)
        



        


    def login(self):
        pass

    def register_new_user(self):
        pass

    def start(self):
        self.main_window.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
