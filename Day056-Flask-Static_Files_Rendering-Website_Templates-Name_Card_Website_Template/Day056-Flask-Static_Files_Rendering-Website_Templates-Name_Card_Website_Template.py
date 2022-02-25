# Rendering Static Files and Website Templates with Flask

from flask import Flask, render_template

app = Flask(__name__)


# Render an HTML template
# Put the templates inside a folder named "templates"
@app.route('/')
def home():
    return render_template('index.html')


# Other files and folders go inside a folder named "static"

# You can find website templates online and modify them to your need
# The fastest way to edit a template is to use the browser's console
# Type "document.body.contentEditable=true" to edit the content in the browser
# Save the page and copy the files to your project

# Day 56 Project - Name Card Website Template
@app.route('/')
def name_card():
    return render_template('name_card_index.html')


if __name__ == '__main__':
    app.run(debug=True)
