"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7uv5269vf5qbbu350-a.oregon-postgres.render.com",
        database="todo_948q",
        user="root",
        password="psE2pljRfaL0vg0BybEUFckDLXOPZxJ9")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
