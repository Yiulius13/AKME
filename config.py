import os
from getpass import getuser
global APP_PATH
global MP4_PATH
global MP3_PATH

APP_PATH = os.path.dirname(os.path.realpath(__file__))

userName=getuser()

MP4_PATH = '''C:/Users/{}/Downloads/MP4'''.format(userName)
MP3_PATH = '''C:/Users/{}/Downloads/MP3'''.format(userName)