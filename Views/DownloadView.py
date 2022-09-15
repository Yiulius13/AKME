import tkinter as tk
from Views.View import View

class DownloadView(tk.Tk,View):
    PAD=10
    BTN_CAPTION=[
        "CANCELAR",
        "CONTINUAR"
    ]
    def __init__(self,controller):
        super().__init__()
        self.downloadController=controller

    def _make_mainFrame(self):
        self.mainFrame=tk.Frame(self)
        self.mainFrame.config(bg="#1A1A1A")
        self.mainFrame.pack(expand=True,fill=tk.BOTH)
    
    def _make_title(self):
        title=tk.Label(self.mainFrame,text="DOWNLOAD",font=("Impact",50),justify=tk.CENTER,background="#1A1A1A")
        title.pack(pady=30)
        line=tk.Frame(self.mainFrame,background="#FF1231",height=2)
        line.pack(fill="x")

    def _make_infoFrame(self,info):
        borderFrame=tk.Frame(self.mainFrame)
        infoFrame=tk.Frame(borderFrame)
        infoFrame.config(bg="#1A1A1A")

        keys='''Title: \nDuration: \nSize: \nChannel'''
        keysLabel=tk.Label(infoFrame,text=keys,justify=tk.LEFT,background="#1A1A1A",fg="white",font=("Roboto",15))
        keysLabel.pack(side=tk.LEFT)
        
        values=f'''{info["title"]} \n{info["length"]} \n{info["size"]} \n{info["author"]}'''
        valuesLabel=tk.Label(infoFrame,text=values,justify=tk.RIGHT,background="#1A1A1A",fg="white",font=("Roboto",15))
        valuesLabel.pack(side=tk.RIGHT)
        
        infoFrame.pack(padx=1,pady=1)
        borderFrame.pack(pady=30,padx=1)
    

    def _make_buttonsFrame(self):
        self.buttonsFrame=tk.Frame(self.mainFrame)
        self.buttonsFrame.config(bg="#1A1A1A")
        self.confirmButton=tk.Button(self.buttonsFrame,text="CONFIRM",command=lambda:self.downloadController.clickConfirm(),width=30,bg="#FF1231",font=("Fixedsys",10),activebackground="#1CCA50",activeforeground="white")
        self.confirmButton.pack(side=tk.LEFT,padx=self.PAD)
        self.cancelButton=tk.Button(self.buttonsFrame,text="CANCEL",command=lambda:self.downloadController.clickCancel(),width=30,bg="#FF1231",font=("Fixedsys",10))
        self.cancelButton.pack(side=tk.RIGHT,padx=self.PAD)
        self.buttonsFrame.pack()

    def _make_finalFrame(self):
        self.finalFrame=tk.Frame(self.mainFrame)
        self.finalFrame.config(bg="#1A1A1A")
        self.successLabel=tk.Label(self.finalFrame,text="✓ Downloaded Succesfully ✓",background="#1A1A1A",fg="#1CCA50",font=("MS Serif",15))
        self.successLabel.pack(pady=self.PAD)
        self.doneButton=tk.Button(self.finalFrame,text="Done",command=lambda:self.downloadController.clickCancel(),width=30,bg="#FF1231",font=("Fixedsys",10))
        self.doneButton.pack(pady=10)
        self.finalFrame.pack()

    def _update_finalFrame(self):
        self.buttonsFrame.destroy()
        self._make_finalFrame()

    def main(self):
        self.title="Download"
        self.geometry("1000x500")
        self._make_mainFrame()
        self._make_title()
        self._make_infoFrame(self.downloadController._getInfo())
        self._make_buttonsFrame()
        self.mainloop()
    
    def close(self):
        self.destroy()