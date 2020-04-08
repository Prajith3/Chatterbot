from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app=Flask(__name__) # __ indicates object ( constructor)
english_bot= ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter") #Storage adapter is the DB
trainer=ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")

@app.route("/")
def index():
    return render_template("index.html") #to send context to HTML file

@app.route("/get")
def get_bot_response():
    userText=request.args.get("msg") #get data from input wherethe JS is written to the HTML
    return str(english_bot.get_response(userText))

if __name__ == '__main__':  #to run it as a python file not as a module
    app.run(debug=True)
