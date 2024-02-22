import PIL.Image
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


genai.configure(api_key=GOOGLE_API_KEY)

# List all models
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)


model = genai.GenerativeModel('gemini-pro')

# text to text
# Generate content
# response = model.generate_content(
#     'write a text prompt for image generation to generate garment cloth design ')

# print(to_markdown(response.text))
# print(response.candidates)

#####
# image to text

img = PIL.Image.open('image.jpg')
img.show()

model = genai.GenerativeModel('gemini-pro-vision')

response = model.generate_content(img)
print(to_markdown(response.text))
print(response.candidates)

# text+image to text
response = model.generate_content(
    ["Write a short, engaging blog post based on this picture. It should include a description of the meal in the photo and talk about my journey meal prepping.", img], stream=True)
response.resolve()
print(to_markdown(response.text))
print(response.candidates)
