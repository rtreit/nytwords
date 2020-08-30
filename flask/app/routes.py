from flask import render_template, request
from app import app
import json

def GenerateWordKey(word):
    key = "".join(sorted(set(word)))
    return key

with open("unique_letter_word_dictionary.json") as f:
    word_dictionary = json.load(f)

@app.route('/')
@app.route('/index')
def index():
    if "word" in request.args:
        original_word = request.args.get("word").strip()
        word = original_word.lower()
        word_length_string = 0        
        if ''.join(sorted(set(word))) in word_dictionary.keys():
            render_string=""          
            words = word_dictionary[GenerateWordKey(word)]
            if len(words) == 1:
                word_length_string = f"{len(words)} English word"
            else:
                word_length_string = f"{len(words)} English words"
            intro_string = f"""
            <p>You entered <b>{original_word}</b> which consists of the letters <b>{''.join(sorted(set(word)))}</b></p>
            <p>The following {word_length_string} can be made from these letters:</p>
            """                            
            for word in words:
                render_string = f"""
                <li><i><a href="https://www.thefreedictionary.com/{word}">{word}</a></i></li>{render_string}"""
            return render_template("index.html" , content=f"{intro_string}{render_string}")
        else:
            intro_string = f"""
            <p>You entered <b>{original_word}</b> which consists of the letters <b>{''.join(sorted(set(word)))}</b></p>
            <p>There are no English words that can be made from these letters.</p>
            """                  
            return render_template("index.html", content=f"{intro_string}")
    else:
        return render_template("index.html")



