import tkinter as tk
from Views.View import View
from tkinter.messagebox import askquestion


class SearchView(tk.Tk,View):

    def __init__(self,controller):
        super().__init__()
        self.searchController=controller

    def _make_headFrame(self):
        self.headFrame=tk.Frame(self,background="#1A1A1A",height=80)
        title=tk.Label(self.headFrame,text="SEARCH",font=("Impact",50),justify=tk.CENTER,background="#1A1A1A")
        title.pack(pady=15)
        line=tk.Frame(self.headFrame,background="#FF1231",height=2)
        line.pack(fill="x")
        self.headFrame.pack(expand=True,fill="both")
    
    def _make_mainFrame(self):
        self.mainFrame=tk.Frame(self,background="#1A1A1A")
        self.mainFrame.columnconfigure(3)
        self.mainFrame.pack(expand=True)
        
        self.resultsFrame1=tk.Frame(self.mainFrame,bg="#1A1A1A",width=310,height=350)
        self.resultsFrame1.grid(padx=5,row=0,column=0,sticky="snw")

        self.optionsFrame=tk.Frame(self.mainFrame,bg="#1A1A1A",width=310,height=350)
        self.optionsFrame.grid(padx=2.5,row=0,column=1,sticky="sn")

        self.resultsFrame2=tk.Frame(self.mainFrame,bg="#1A1A1A",width=330,height=350)
        self.resultsFrame2.grid(padx=5,row=0,column=2,sticky="sne")
    
    def _make_resultsFrame1(self):
        buttonsInfo=self.searchController._getButtonsInfo()[:5]
        for video in buttonsInfo:
            b=tk.Button(self.resultsFrame1,bg="#FF1231",font=("Fixedsys",10),text=video["button text"],width=38,
                activebackground="#1CCA50",activeforeground="white",command=lambda e=video:self._popupFrame(e))
            b.pack(pady=10,padx=5)
    def _make_optionsFrame(self):
        
        self.searchEntry=tk.Entry(self.optionsFrame,justify=tk.LEFT,width=26,bg="#9E9E9A",fg="#1A1A1A",font=("Roboto",15))
        self.searchEntry.pack(pady=15,padx=5)
        self.searchEntry.focus()
        
        
        self.searchButton=tk.Button(self.optionsFrame,text="SEARCH",command=self.searchController.clickSearch,width=15,bg="#FF1231",font=("Fixedsys",10),activebackground="#1CCA50",activeforeground="white")
        self.searchButton.pack()
        
        lFrame=tk.Frame(self.optionsFrame)
        self.diamondLabel=tk.Label(lFrame,text="K⧫",fg="#A60006",bg="#0D0D0D",font=("Vani",40))
        self.diamondLabel.pack(pady=1,padx=1)
        lFrame.pack(pady=30)
        
        
        buttonsFrame=tk.Frame(self.optionsFrame,bg="#1A1A1A")
        buttonsFrame.pack(fill="x",side="bottom")
        
        self.backButton=tk.Button(buttonsFrame,text="BACK",command=lambda:self.searchController.clickBack(),activebackground="#1CCA50",activeforeground="white",
            width=12,bg="#FF1231",font=("Fixedsys",10))
        self.backButton.pack(side="left",padx=5)
        
        self.exitButton=tk.Button(buttonsFrame,text="EXIT",command=lambda:self.searchController.close("EXIT"),activebackground="#CF0707",activeforeground="white",
            width=12,bg="#FF1231",font=("Fixedsys",10))
        self.exitButton.pack(side="right",padx=5)
    def _make_resultsFrame2(self):
        buttonsInfo=self.searchController._getButtonsInfo()[5:]
        for video in buttonsInfo:
            b=tk.Button(self.resultsFrame2,bg="#FF1231",font=("Fixedsys",10),text=video["button text"],width=38,
                activebackground="#1CCA50",activeforeground="white",command=lambda e=video:self._popupFrame(e))
            b.pack(pady=10,padx=5)
    

    
    def _popupFrame(self,info):
        frame=askquestion(message=info["popup text"],title="Confirmar Descarga")
        if frame=="yes":
            self.searchController.clickConfirm(info["link"])
        elif frame=="no":
            pass
    def main(self):
        self.title="Search"
        self.geometry("1000x500")
        self.configure(bg="#1A1A1A")
        self._make_headFrame()
        self._make_mainFrame()
        self._make_optionsFrame()
        self._make_resultsFrame1()
        self._make_resultsFrame2()
        self.mainloop()
    def close(self):
        self.destroy()
        return