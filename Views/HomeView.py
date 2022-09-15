
import tkinter as tk
from tkinter import ttk
from Views.View import View


class HomeView(tk.Tk,View):
    
    PAD=10
    def __init__(self,controller):
        super().__init__()
        self.homeController=controller

    def _make_mainFrame(self):
        self.mainFrame=tk.Frame(self)
        self.mainFrame.config(bg="#1A1A1A")
        self.mainFrame.pack(expand=True,fill=tk.BOTH)

    def _make_title(self):
        title=ttk.Label(self.mainFrame,text="A K M E",font=("Impact",80),justify=tk.CENTER,background="#1A1A1A")
        title.pack(padx=self.PAD,pady=30)

    def _make_entry(self):
        self.searchEntry=tk.Entry(self.mainFrame,justify=tk.LEFT,width=70,bg="#9E9E9A",fg="#1A1A1A",font=("Roboto",15))
        self.searchEntry.pack(pady=5)
        self.searchEntry.focus()
    
    def _make_errorlog(self):
        self.logLabel=tk.Label(self.mainFrame,font=("Batang",10),bg="#1A1A1A",fg="#CF0707")
        self.logLabel.pack(pady=5)
        
    
    def _make_buttons(self):
        buttonsFrame=tk.Frame(self.mainFrame)
        buttonsFrame.config(bg="#1A1A1A")
        downloadButton=tk.Button(buttonsFrame,text="DOWNLOAD",command=self.homeController.clickDownload,width=30,bg="#FF1231",font=("Fixedsys",10),activebackground="#1CCA50",activeforeground="white")
        downloadButton.pack(side=tk.LEFT,padx=self.PAD)
        searchButton=tk.Button(buttonsFrame,text="SEARCH",command=self.homeController.clickSearch,width=30,bg="#FF1231",font=("Fixedsys",10),activebackground="#1CCA50",activeforeground="white")
        searchButton.pack(side=tk.RIGHT,padx=self.PAD)
        buttonsFrame.pack()

    def _make_exitButton(self):
        self.exitButton=tk.Button(self.mainFrame,text="EXIT",command=lambda:self.homeController.close("EXIT"),width=20,bg="#FF1231",font=("Fixedsys",10),activebackground="#CF0707",activeforeground="white")
        self.exitButton.pack(pady=40)
    


    def _update_errorlog(self,update):
        self.logLabel.config(text=update)
    def main(self):
        self.title("AKME")
        self.geometry("1000x500")
        self._make_mainFrame()
        self._make_title()
        self._make_entry()
        self._make_errorlog()
        self._make_buttons()
        self._make_exitButton()
        self.mainloop()
    def close(self):
        self.destroy()
        return
