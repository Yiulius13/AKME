from Core.Controller import Controller
from Models.Temp import Temp

class SearchController(Controller):
    def __init__(self):
        self.searchView=self.loadView("search")
        self.tempModel=Temp()
        self.searchText=self.tempModel._getNext("search")

    def _getLinks(self):
        from youtubesearchpython import VideosSearch
        search=VideosSearch(self.searchText,limit=10)
        results=search.result()
        results=results["result"]
        links=[]
        for result in results:
            links.append(result["link"])
        return links

    def _getInfo(self,link):
        from hurry.filesize import size
        import datetime
        from pytube import YouTube
        yt=YouTube(link)
        
        lengt=str(datetime.timedelta(seconds=yt.length)).split(":")
        if lengt[0]=="0":
            lengt=lengt[1]+":"+lengt[2]
        else:
            lengt=str().join(lengt)
        
        title=yt.title
        if len(title)>>30:
            title=title[:30]
        
        
        info = {
            "title":title,
            "length":lengt,
            "author":yt.author,
            "link":link}
        info["button text"]="{}\n{}".format(info["title"],info["length"],info["author"])
        info["popup text"]="Title:    {}\nDuration: {}\nChannel:  {}".format(info["title"],info["length"],info["author"])
        yt=None
        return info

    def _sortEntry(self,text):
        if "https://www.youtube.com/watch" in text:
            return "LINK"
        else:
            return "SEARCH"
    def _validateEntry(self,text):
        if len(text)>>2:
            return True
        else:
            return False
    def _validateLink(self,link):
        from pytube import YouTube
        try:
            yt=YouTube(link)
            return True
        except:
            return False

    def _getButtonsInfo(self):
        info=[]
        for link in self._getLinks():
            info.append(self._getInfo(link))
        return info

    
    def clickBack(self):
        self.close("home")
    def clickConfirm(self,link):
        self.tempModel._putNext("link",link)
        self.close("download")
    def clickSearch(self):
        text=self.searchView.searchEntry.get()
        if self._validateEntry(text):
            if self._sortEntry(text)=="LINK":
                self.clickConfirm(text)
            else:
                self.tempModel._putNext("search",text)
                self.close("search")
        else:
            self.homeView._update_errorlog("Short entry!")
    def main(self):
        self.searchView.main()
    def close(self,next):
        self.tempModel._putNext("frame",next)
        self.searchView.close()
