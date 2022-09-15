from Core.Core import Core
from Models.Temp import Temp
import os
from config import MP4_PATH,MP3_PATH
class Main:
    
    @staticmethod
    def run():
        if not os.path.exists(MP4_PATH):
            os.mkdir(MP4_PATH)
        if not os.path.exists(MP3_PATH):
            os.mkdir(MP3_PATH)
        
        
        tempModel=Temp()
        try:
            app=Core.openController("home")
            app.main()
            while True:
                next=tempModel._getNext("frame")
                if next=="EXIT":
                    break
                else:
                    app=Core.openController(next)
                    app.main()
        except Exception as e:
            print(str(e))

if __name__=="__main__":
    Main.run()