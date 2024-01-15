from openai import OpenAI
from flask import Flask, render_template, request



app = Flask(__name__)

client=OpenAI(api_key='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')


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


if __name__ == '__main__':
    app.run(debug=True)

# from openai import OpenAI
# from flask import Flask, render_template, request, jsonify
#
# app = Flask(__name__)
#
# # Replace 'YOUR_OPENAI_API_KEY' with your actual API key
# client = OpenAI(api_key='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')
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/get_chatbot_response", methods=["POST"])
# def get_chatbot_response():
#     try:
#         message = request.json.get('userInput')
#         if not message:
#             return jsonify({'error': 'Empty message received.'})
#
#         conversation = [
#             {"role": "user", "content": message}
#         ]
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=conversation
#         )
#
#         bot_response = completion.choices[0].message.content.strip()
#
#         return jsonify({'botResponse': bot_response})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# if __name__ == '__main__':
#     app.run(debug=True)


# from openai import OpenAI
# from flask import Flask, render_template, request, jsonify
#
# app = Flask(__name__)
#
# # Replace 'YOUR_OPENAI_API_KEY' with your actual API key
# client = OpenAI(api_key='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')
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/get_chatbot_response", methods=["POST"])
# def get_chatbot_response():
#     try:
#         message = request.json.get('userInput')
#         conversation = [
#             {"role": "user", "content": message}
#         ]
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=conversation
#         )
#
#         bot_response = completion.choices[0].message.content.strip()
#
#         return jsonify({'botResponse': bot_response})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
