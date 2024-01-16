from openai import OpenAI
from flask import Flask, render_template, request

app = Flask(__name__)

client=OpenAI(api_key='YOUR API KEY')

# Define the default route to return the index.html file
@app.route("/")

def index():
    return render_template("index.html")

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    message = request.json.get('message')

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "user", "content": message}
    ]
    )
    return {'content': completion.choices[0].message.content}
from app import app
if __name__=="__main__":
    app.run(debug=True)
