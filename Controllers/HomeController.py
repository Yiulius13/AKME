from Core.Controller import Controller
from Core.Core import Core
from Models.Temp import Temp

class HomeController(Controller):
    def __init__(self):
        
        self.homeView=self.loadView("home")
        self.tempModel=Temp()
    def _validateEntry(self,text):
        if len(text)>>2:
            return True
        else:
            return False
    def _sortEntry(self,text):
        if "https://www.youtube.com/watch" in text:
            return "LINK"
        else:
            return "SEARCH"
    def _validateLink(self,link):
        from pytube import YouTube
        try:
            yt=YouTube(link)
            return True
        except:
            return False
    def _getLink(self,text):
        if self._sortEntry(text)=="SEARCH":
            from youtubesearchpython import VideosSearch
            search=VideosSearch(text,limit=1)
            result=search.result()
            result=result["result"]
            result=result[0]
            link = result["link"]
        else:
            link = text
        if self._validateLink(link):
            return link
        else:
            return False

    def clickSearch(self):
        text=self.homeView.searchEntry.get()
        if self._validateEntry(text):
            if self._sortEntry(text)=="LINK":
                self.clickDownload()
            else:
                self.tempModel._putNext("search",text)
                self.close("search")
        else:
            self.homeView._update_errorlog("Short entry!")


    def clickDownload(self):
        text=self.homeView.searchEntry.get()
        if self._validateEntry(text):
            if self._sortEntry(text)=="LINK":
                pass
            else:
                text=self._getLink(text)
            if self._validateLink(text):
                self.tempModel._putNext("link",text)
                self.close("download")
            else:
                self.homeView._update_errorlog("Link or search not valid!")
        else:
            self.homeView._update_errorlog("Short entry!")
    def main(self):
        self.homeView.main()
    def close(self,next):
        self.tempModel._putNext("frame",next)
        self.homeView.close()
        
        

