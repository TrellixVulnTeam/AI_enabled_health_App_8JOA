import sqlite3
import kivy
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.lang import Builder      # using this no need of having main class same as kivy
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class LoginWindow(Screen): # login screen class inheriting screen class
    username= ObjectProperty(None)
    password = ObjectProperty(None)


    def loginBtn(self):
        self.reset()
        sm.current = "mainW"

    def createBtn(self):
        self.reset()  # clears everything
        sm.current = "create"

    def reset(self): # resets the username and password section
        self.username = ""  
        self.password = ""
        

class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    confirm = ObjectProperty(None)

    def login(self):
        self.reset() # clears all
        sm.current = "login"

    def submit(self):
        
        # connecting to database
        conn = sqlite3.connect('login.db')
        
        # create a cursor
        c = conn.cursor()
        
        # taking user data
        if self.ids["username"].text and self.ids["password"].text and self.ids["confirm"] .text is not None:

            u = self.ids["username"].text
            p = self.ids["password"].text
            co = self.ids["confirm"].text

            if p==co:  # if password and confirm password are same then only push to database


                # add a record
                c.execute("INSERT INTO users VALUES (?,?)",(u,p))
            
                conn.commit()
                conn.close()
        
                sm.current = "login"
                
                
            
            else:
                popup = Popup(title='Invalid Password', content=Label(text='Password and Confirm-Password does not match.\nPlease try again'), size_hint = (0.5,0.5))
                popup.open()
        
        #else:
            #pop up giving fill required details

    def reset(self):   # resets everything to blank
        username = ""
        password = ""
        confirm =  ""

class MainWindow(Screen):
    
    def modelOn(self):
        pass # this will check in the model
    
    def modelOff(self):
        pass   # this will check out off the model
    
    def pauseNotif(self):  # logic to pause notification
        pass

    def unpauseNotif(self):  # logic to unpause notification
        pass

    def remindMe(self):   # logic to snooze the notifications for 5 minutes  # BUT HOW WILL ONE CAN STOP THE SNOOZE
        pass
    
    def scale(self):
        sm.current = "graph"

    def set(self):
        sm.current = "settingM"

class SettingMain(Screen):
    
    def notif(self):
        sm.current = "settingN"

    def prof(self):
        sm.current = "settingP"

    def login(self):
        sm.current = "login"

    def back(self):
        sm.current= "mainW"

class SettingProfile(Screen):
    
    n = ObjectProperty(None)
    age = ObjectProperty(None)
    #weight:ObjectProperty(None)
    #height:ObjectProperty(None)
    #job:ObjectProperty(None)
    #profile:ObjectProperty(None)

    def save(self):
        pass   # this function will save the data into the database
    
    def back(self):
        sm.current = "settingM"
    
    def reset(self):  # clear data
        n = ""
        age= ""
        #weight:""
        #height:""
        #job:""
        #profile:""
    
    


class SettingNotif(Screen):

    def back(self):
        sm.current = "settingM"

class Graph(Screen):
    
    def back(self):
        sm.current="mainW"

class WindowManager(ScreenManager): # inheriting screenmanager class properties to manage multiple screens
    pass


def invalidLogin():
    pass

def invalidForm():
    pass

kv = Builder.load_file("my.kv") # loading my.kv file

sm = WindowManager() # instance of class

# putting screens in widget; standard procedure
screens = [LoginWindow(name="login"),
            CreateAccountWindow(name="create"),
            MainWindow(name="mainW"), 
            SettingMain(name="settingM"), 
            SettingProfile(name="settingP"), 
            SettingNotif(name="settingN"),
            Graph(name="graph")]

for i in screens:
    sm.add_widget(i) 


sm.current = "login"  # default screen must be login


class MyMainApp(App): # inheriting the properties of App class from kivy library
    
    def build(self):

        return sm    # going to screenmanager



if __name__ == "__main__":
    MyMainApp().run()