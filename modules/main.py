# resource: https://huggingface.co/transformers/usage.html#extractive-question-answering

import torch
from transformers import AutoModelForQuestionAnswering
from transformers import AutoTokenizer
from transformers import pipeline


nlp = pipeline("question-answering")

tokenizer = AutoTokenizer.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")
model = AutoModelForQuestionAnswering.from_pretrained("bert-large-uncased-whole-word-masking-finetuned-squad")


def auto_qa(question, text):
  inputs = tokenizer.encode_plus(question, text, add_special_tokens=True, return_tensors="pt")
  input_ids = inputs["input_ids"].tolist()[0]

  text_tokens = tokenizer.convert_ids_to_tokens(input_ids)
  answer_start_scores, answer_end_scores = model(**inputs)

  answer_start = torch.argmax(
      answer_start_scores
  )  # Get the most likely beginning of answer with the argmax of the score
  answer_end = torch.argmax(answer_end_scores) + 1  # Get the most likely end of answer with the argmax of the score

  answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

  return answer

def nlp_qa(question, text):
  result = nlp(question=question, context=text)
  return result["score"], result["answer"]
