# Ask Me

This is a simple Flask application that takes in user input consisting of a text and a question on that text and produces the answer using a pretrained BERT or DistilBert fine-tuned on the The Stanford Question Answering Dataset (SQuAD)

resources:

[Huggingface](https://huggingface.co/transformers/usage.html#extractive-question-answering)

[SQuAD](https://rajpurkar.github.io/SQuAD-explorer/)

## Installation
Using `PIP`:
```bash
$ python -m pip install -r requirements.txt
```

## Usage
Running the localhost server:
```bash
$ flask run
```

## Notes:
when in development, export the following environmental variable:
```bash
$ export FLASK_ENV=development
```
With this, you don't have to restart the server everytime you update your code.