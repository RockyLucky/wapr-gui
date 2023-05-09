import os
import tkinter as tk
from tkinter import messagebox

class warp_cli():
    
    def connect(self):
        if self.status_check == True:
            os.popen('warp-cli disconnect')
            self.is_connected.set('Connect')
            self.is_connected2.set('Disconnected')
            self.status = os.popen('warp-cli status').read()
            self.status_check = 'Status update: Connected' in self.status
        else:
            os.popen('warp-cli connect')
            self.is_connected.set('Disconnect')
            self.is_connected2.set('Connected')
            self.status = os.popen('warp-cli status').read()
            self.status_check = 'Status update: Connected' in self.status
    def install(self):
        os.system('sudo apt install cloudflare-warp -y')
        os.system('sudo yum install cloudflare-warp -y')
        messagebox.showwarning('Warp Install', 'If the application is still not working, you will need to download WARP manually.')
    
    def quit(self, e):
        self.root.destroy()
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cloudflare Warp - Linux x64')
        self.root.geometry('300x125')
        self.root.resizable(False, False)
        self.root.bind('<Escape>', self.quit)
        self.is_connected = tk.StringVar()
        self.is_connected2 = tk.StringVar()
        self.is_connected.set('Connect')
        self.status = os.popen('warp-cli status').read()
        self.status_check = 'Status update: Connected' in self.status
        
        self.top_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)
        self.top_frame.pack(side='top', pady=2)
        self.bottom_frame.pack(side='bottom',pady=3)
        
        self.title_label = tk.Label(self.top_frame, text='Cloudflare Warp CLI Connection', font=('Comic Sans MS', 18))
        self.title_label.pack()
        self.info_label = tk.Label(self.top_frame, text='Double click the "Connect"/"Disconnect" button \nto change your connection', font=('Comic Sans MS', 10))
        self.info_label.pack()
        self.connection_label = tk.Label(self.top_frame, textvariable=self.is_connected2, font=('Comic Sans MS', 12))
        self.connection_label.pack()
        self.connect_button = tk.Button(self.bottom_frame, textvariable=self.is_connected, command=self.connect)
        self.connect_button.pack(side='left')
        self.install_button = tk.Button(self.bottom_frame, text='Install', command=self.install)
        self.install_button.pack(side='left')
        
        self.root.mainloop()
        

warp_cli()