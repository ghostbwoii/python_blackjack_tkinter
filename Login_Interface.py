"""
creates form for login page upon app exec.
"""

import os
import re
from tkinter import *
from tkinter import messagebox


class Login():
    """
    handles the user login interface
    """

    node_list = []
    username = None
    password = None
    entry = None
    start_game = False
    root = None

    def create_scene(self):
        """
        sets up gui root
        """
        self.root = Tk()

        self.root.geometry("327x130+300+300")
        self.root.title("Login")
        self.root.resizable(False, False)
        self.root.configure(bg="grey25")
        self.entry = Entry(self.root)
        return self.root

    def create_nodes(self, root):
        """
        creates nodes
        """
        user_login = Label(root, text="USER LOGIN", font="courier 12 bold")
        self.node_list.append(user_login)
        username_lbl = Label(root, text="Username:", font="courier 8 bold")
        self.node_list.append(username_lbl)
        password_lbl = Label(root, text="Password:", font="courier 8 bold")
        self.node_list.append(password_lbl)
        error_lbl = Label(root, text="")
        self.node_list.append(error_lbl)
        username_txt = Text(root, width=20, height=1, wrap=WORD)
        self.node_list.append(username_txt)
        password_txt = Text(root, width=20, height=1, wrap=WORD)
        self.node_list.append(password_txt)
        register_btn = Button(root, text="REGISTER", bg="black",
                              fg="gold", command=self.set_username_password,
                              width="10", font="courier 9 bold")
        self.node_list.append(register_btn)
        login_btn = Button(root, text="LOGIN", bg="black",
                           fg="gold", command=self.log_username_password,
                           width="10", font="courier 9 bold")
        self.node_list.append(login_btn)
        clear_btn = Button(root, text="CLEAR", bg="black",
                           fg="gold", command=self.clear_fields, width="10", font="courier 9 bold")
        self.node_list.append(clear_btn)

        return root

    def set_grid(self, root):
        """
        arranges nodes and some initial node values
        """
        self.node_list[0].grid(row=0, column=2)
        self.node_list[0].configure(bg="gray25", fg="black")
        self.node_list[1].grid(row=1, column=1)
        self.node_list[1].configure(bg="gray25", fg="gold")
        self.node_list[2].grid(row=2, column=1)
        self.node_list[2].configure(bg="gray25", fg="gold")
        self.node_list[4].grid(row=1, column=2)
        self.node_list[5].grid(row=2, column=2)
        self.node_list[6].grid(row=4, column=1)
        self.node_list[7].grid(row=4, column=2)
        self.node_list[8].grid(row=4, column=3)
        self.node_list[4].focus()

        return root



    def create_user(self, username, password):
        """
        stores user/pass in .dat. uses to recursion to ensure file creation.
        as such is technically not pylint perfect.
        """
        user_data = None
        found = False
        if os.path.exists("login.dat"):
            with open("login.dat", "r+") as user_data:

                if user_data.readline() == username:
                    found = True
                    messagebox.showerror("Error", "Username Exists")
                if username and not found and re.findall("^[A-Za-z0-9_-]+$", username):
                    if re.findall("^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])"+
                                  "[a-zA-Z0-9!@#$%^&*]{8,12}", password):
                        data = username + password
                        user_data.write(data)
                        self.start_game = True
                        self.close_root()

                    else:
                        messagebox.showerror("Error", "Pwd Format: Abc123#$. Min 8.char")
                else:
                    messagebox.showerror("Error", "Invalid Username.")
        else:
            user_data = open("login.dat", "w+")

            return self.create_user(self.username, self.password)

    def login_user(self, username, password):
        """
        stores user/pass in .dat
        """
        user_data = None

        if os.path.exists("login.dat"):
            with open("login.dat", "r+") as user_data:
                user_found = False
                pass_found = False
                for line in user_data:
                    if line == username:
                        user_found = True
                    if line == password:
                        pass_found = True
                if not user_found:
                    messagebox.showerror("Error", "Username not found")
                if not pass_found:
                    messagebox.showerror("Error", "Incorrect Password")
                if user_found and pass_found:
                    self.start_game = True
                    self.close_root()

    def set_username_password(self):
        """
        grabs textfield data and runs it through account register method
        """
        self.username = self.node_list[4].get("1.0", END)
        self.password = self.node_list[5].get("1.0", END)
        self.node_list[4].delete("1.0", END)
        self.node_list[5].delete("1.0", END)
        self.node_list[4].focus()
        self.create_user(self.username, self.password)

    def log_username_password(self):
        """
        grabs textfield data and runs it thorugh log in method
        """
        self.username = self.node_list[4].get("1.0", END)
        self.password = self.node_list[5].get("1.0", END)
        self.node_list[4].delete("1.0", END)
        self.node_list[5].delete("1.0", END)
        self.node_list[4].focus()
        self.login_user(self.username, self.password)

    def clear_fields(self):
        """
        clears text field on button action
        """
        self.node_list[4].delete("1.0", END)
        self.node_list[5].delete("1.0", END)
        self.node_list[4].focus()

    def get_username(self):
        """
        get method for username
        """
        return self.username

    def get_password(self):
        """
        get method for password
        """
        return self.password
    def get_permission(self):
        """
        if login is successful this boolean controls game launch
        """
        return self.start_game
    def close_root(self):
        """
        closes login root
        """
        self.root.destroy()
