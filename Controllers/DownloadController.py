from Core.Controller import Controller
from Core.Core import Core
from Models.Temp import Temp
from pytube import YouTube


class DownloadController(Controller):
    def __init__(self):
        self.downloadView=self.loadView("download")
        self.tempModel=Temp()
        self.link=self.tempModel._getNext("link")
        self.yt=YouTube(self.link)
        self.stream=self.yt.streams.filter(mime_type="video/mp4")
        self.stream=self.stream[0]
    def clickConfirm(self):
        
        #self.downloadView._update_downloadFrame()
        self._download()
        #self.downloadView._update_convertFrame()
        self._convert()
        self.downloadView._update_finalFrame()
        
    def clickCancel(self):
        self.close("home")



    def _getInfo(self):
        from hurry.filesize import size
        import datetime
        return {
            "title":self.yt.title,
            "length":str(datetime.timedelta(seconds=self.yt.length)),
            "size":size(self.stream.filesize),
            "author":self.yt.author}
        
    def _download(self):
        from config import MP4_PATH
        import os
        video=YouTube(self.link)
        dirName=MP4_PATH+"/"+self.link.split("=")[-1]
        try:
            os.mkdir(dirName)
        except FileExistsError:
            pass
        stream=video.streams.filter(mime_type="video/mp4")
        stream=stream[0]
        audio=video.streams.get_by_itag(stream.itag)
        try:
            audio.download(dirName)
        except FileExistsError:
            pass
        self.tempModel._putNext("dirname",dirName)
    def _convert(self):
        import moviepy.editor as mp
        from os import listdir
        from config import MP3_PATH
        import shutil
        dirName=self.tempModel._getNext("dirname")
        videoName=listdir(dirName)[0]
        video=mp.VideoFileClip("{}/{}".format(dirName,videoName))
        try:
            video.audio.write_audiofile("{}/{}.mp3".format(MP3_PATH,videoName[:-4]))
        except FileExistsError:
            pass
        video.audio.close()
        video.close()
        shutil.rmtree(dirName)
    def main(self):
        self.downloadView.main()
    def close(self,next):
        self.tempModel._putNext("frame",next)
        self.downloadView.close()