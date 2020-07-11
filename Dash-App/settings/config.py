
import os


# App settings
name = "Minjusticia DS4A"

host = "127.0.0.1"

port = int(os.environ.get("PORT", 5000))

debug = False

contacts = ""

code = ""

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'


# File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"


# DB
