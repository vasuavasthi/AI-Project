# from openai import OpenAI
# from flask import Flask, render_template, request



# app = Flask(__name__)

# client=OpenAI(api_key='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')


# # Define the default route to return the index.html file
# @app.route("/")

# def index():
#     return render_template("index.html")


# # Define the /api route to handle POST requests
# @app.route("/api", methods=["POST"])
# def api():
#     message = request.json.get('message')

#     completion = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#         {"role": "user", "content": message}
#     ]
#     )
#     return {'content': completion.choices[0].message.content}


# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        message = request.form['message']

        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=message,
            temperature=0.7,
            max_tokens=150
        )

        response = completion.choices[0].text.strip()
        return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
