import os
import importlib
from config import APP_PATH
import abc


class Controller(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def main(self):
        return 
    def loadView(self,viewName):
        response=None
        viewName=viewName[0].upper()+viewName[1:]+"View"

        if os.path.exists(APP_PATH+"/Views/"+viewName+".py"):
            module=importlib.import_module("Views."+viewName)
            class_=getattr(module,viewName)
            response=class_(self)

        return response