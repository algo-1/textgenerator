from flask import Flask, render_template, request
from spotify import get_pic_url
from textgenerator import get_generated_text_list

app = Flask(__name__)

@app.route('/', methods= ['GET'])
def index():
    return render_template('home.html') 
    
@app.route('/text', methods= ['POST'])
def text():
    # get user input 
    artist_name = request.form['artist_name']
   
    # get pic url 
    pic = get_pic_url(artist_name)
    
    # get list of lyrics
    generated_text_list = get_generated_text_list(artist_name)
    
    # converts list such that each new list element is a line of generated text 
    processed_list = [" ".join(line) for line in generated_text_list]
    
    return render_template('index.html', sauce= pic, members= processed_list, artist_name= artist_name)    

app.run(port= 5000)
