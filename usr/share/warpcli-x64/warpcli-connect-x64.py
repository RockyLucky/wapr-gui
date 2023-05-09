import os
import tkinter as tk
from tkinter import messagebox

class warp_cli():
    def connect(self):
        if self.is_connected_val == 1:
            os.system('warp-cli disconnect')
            self.is_connected.set('Connect')
            self.is_connected_val = 0
        else:
            os.system('warp-cli connect')
            self.is_connected.set('Disconnect')
            self.is_connected_val = 1
            
    def install(self):
        os.system('sudo apt install cloudflare-warp -y')
        os.system('sudo yum install cloudflare-warp -y')
        messagebox.showwarning('Warp Install', 'If there was an error, you need to manually install the package or the installation method is not supported on your system.')
    
    def quit(self, e):
        self.root.destroy()
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Cloudflare Warp - Linux x64')
        self.root.geometry('300x100')
        self.root.resizable(False, False)
        self.root.bind('<Escape>', self.quit)
        self.is_connected = tk.StringVar()
        self.is_connected.set('Connect')
        self.is_connected_val = 0
        
        self.top_frame = tk.Frame(self.root)
        self.bottom_frame = tk.Frame(self.root)
        self.top_frame.pack(side='top', pady=7)
        self.bottom_frame.pack(side='bottom',pady=3)
        
        self.is_connected_label = tk.Label(self.top_frame, text='Cloudflare Warp CLI Connection', font=('Comic Sans MS', 18))
        self.is_connected_label.pack()
        self.connect_button = tk.Button(self.bottom_frame, textvariable=self.is_connected, command=self.connect)
        self.connect_button.pack(side='left')
        self.install_button = tk.Button(self.bottom_frame, text='Install', command=self.install)
        self.install_button.pack(side='left')
        
        self.root.mainloop()
        

warp_cli()