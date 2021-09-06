from flask import Flask
from flask import flash, request, redirect, url_for
from flask import render_template, jsonify

from modules.main import auto_qa, nlp_qa


app = Flask(__name__)

def predict_answer(text, question):
  answer = nlp_qa(text, question)
  return answer

@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def my_form_question():
  text = request.form['text']
  question = request.form['question']
  score, predicted_answer = predict_answer(text, question)
  result = {
    "asnwer": predicted_answer,
    "score": score
  }
  result = {str(key): value for key, value in result.items()}
  return jsonify(result=result)

if __name__ == '__main__':
  app.debug = True
  app.run()
