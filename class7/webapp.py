import vidbot
from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    text = request.args.get("text", "")
    ts = str(time.time())
    outname = "static/" + ts + ".mp4"
    if text: 
        vidbot.compose(text, 1, outname)
        return '<video autoplay loop scr=' + outname + '></video>'
    else:
        return "Type text into the url"

if __name__ == "__main__":
    app.run(debug=True)
