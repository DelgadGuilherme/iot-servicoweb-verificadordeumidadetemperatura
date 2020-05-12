from flask import Flask
import os


app= Flask(__name__)


from application.controller import temperatura_controller
from application.controller import umidade_controller