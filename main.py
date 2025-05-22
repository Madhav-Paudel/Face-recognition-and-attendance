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
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)
        # for adding webcam
        self.add_webcam(self.webcam_label)

        # showing the path for the directory 
        self.db.dir='./db'
        if not  os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
            

    
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)
            
        self._label = label
        self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        self.most_recent_capture_arr = frame

        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_)

        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)
        
        self._label.after(20, self.process_webcam)

    def login(self):
        pass

    def register_new_user(self):

        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+370+120")

        x_position = 750
        login_y = 300
        gap = 20

        self.accept_button_register_new_user_window = util.get_button(
        self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=x_position, y=login_y)

        self.start_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Start Again', 'red', self.start_again_register_new_user)
        self.start_again_button_register_new_user_window.place(x=x_position, y=login_y + self.accept_button_register_new_user_window.winfo_reqheight() + gap)
        

        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.enter_text_register_new_user=util.get_entry_text(self.register_new_user_window)
        self.enter_text_register_new_user.place(x=750,y=150)
        
        self.text_label_register_new_user = tk.Label(self.register_new_user_window, text="Enter Your UserName:", font=("Arial", 12), bg='white', fg='black')
        self.text_label_register_new_user.place(x=750, y=70)





    def add_img_to_label(self,label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)
        self.register_new_user_capture=self.most_recent_capture_arr.copy()
        
    def start_again_register_new_user(self):
        self.register_new_user_window.destroy()





    def accept_register_new_user(self):
        pass 
    

    def start(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = App()
    app.start()