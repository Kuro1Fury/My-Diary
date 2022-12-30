# import datetime
# from flask import Flask, render_template, request
# from pymongo import MongoClient


# def create_app():
#     app = Flask(__name__)
#     client = MongoClient(
#         "mongodb+srv://Kuro1_Fury:skycoder135790@my-diary-application.tibejqh.mongodb.net/test")
#     app.db = client.MyDiary

#     @app.route("/", methods=["GET", "POST"])
#     def home():
#         if request.method == "POST":
#             entry_content = request.form.get("contentEntry")
#             formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
#             app.db.entries.insert_one(
#                 {"content": entry_content, "date": formatted_date})

#         entries_with_date = [
#             (entry["content"],
#              entry["date"],
#              datetime.datetime.strptime(
#                 entry["date"], "%Y-%m-%d").strftime("%b %d")
#              )
#             for entry in app.db.entries.find({})
#         ]
#         return render_template("home.html", entries=entries_with_date)

#     return app





# entries = []

# # def create_app():
# app = Flask(__name__)
# #     client = MongoClient(
# #         "mongodb+srv://Kuro1_Fury:skycoder135790@my-diary-application.tibejqh.mongodb.net/test")
# #     app.db = client.MyDiary


# @app.route("/", methods=["GET", "POST"])
# def home():
#     if request.method == "POST":
#         entry_content = request.form.get("contentEntry")
#         formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

#         entries.append((entry_content, formatted_date))
# #             app.db.entries.insert_one(
# #                 {"content": entry_content, "date": formatted_date})

#     entries_with_date = [
#         (entry[0],
#             entry[1],
#             datetime.datetime.strptime(
#             entry[1], "%Y-%m-%d").strftime("%b %d")
#          )
#         for entry in entries
#     ]
#     return render_template("home.html", entries=entries_with_date)
#     # return "Hello?"

# #     return app



import os
import datetime
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.environ.get("MONGODB_URI"))
    app.db = client.microblog

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            app.db.entries.insert({"content": entry_content, "date": formatted_date})
        
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
            )
            for entry in app.db.entries.find({})
        ]
        return render_template("home.html", entries=entries_with_date)
    
    return app
