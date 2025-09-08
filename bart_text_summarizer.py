from transformers import pipeline

# Load a summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

import ipywidgets as widgets
from IPython.display import display

text_area = widgets.Textarea(
    placeholder='Input text here:',
    layout=widgets.Layout(width='100%', height='200px'),
    description='Input:',
    disabled=False
)
display(text_area)

user_input = text_area.value

# Generate summary
summary = summarizer(user_input, max_length=100, min_length=30, do_sample=False)
print(summary[0]['summary_text'])