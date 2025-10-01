from transformers import T5Tokenizer, T5ForConditionalGeneration  # Abstractive fomat
model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")

text = """
This paper proposes a novel method for optimizing deep neural networks using a hybrid of genetic algorithms and backpropagation. Our experiments show significant improvements in convergence speed and model accuracy...
"""

input_text = "summarize: " + text
input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

summary_ids = model.generate(input_ids, max_length=100, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("Summary:", summary)

