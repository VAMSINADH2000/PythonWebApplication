from flask import Flask,render_template,request
import random,string as st
import pyttsx3
import pyshorteners as ps
import qrcode
from translate import Translator

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home1():
    return render_template('home.html')
@app.route('/qrcode',methods=['POST','GET'])
def home():
    return render_template('qrcodehome.html')
@app.route('/download',methods=['POST','GET'])
def download():
    link = request.form['link']
    img = qrcode.make(link)
    img.show()
    return render_template("qrcodehome.html")
@app.route('/password',methods=['POST','GET'])
def passwordgen():
    alphabets = st.ascii_letters
    string = '0123456789' + '-+*%&$@!_' + alphabets
    pass_len = 9
    passw = random.sample(string, pass_len)
    passw = ''.join(passw)
    return render_template('password.html',password=passw)

@app.route('/texttospeech',methods=['POST','GET'])
def text_to_speech():
    return render_template('texttospeech.html')

@app.route('/convert',methods=['POST','GET'])
def convert():
    mod = pyttsx3.init()
    sentence = request.form['sentence']
    mod.say(sentence)
    mod.runAndWait()
    return render_template('texttospeech.html')

@app.route('/urlshortform',methods=['GET','POST'])
def takeurl():
    return render_template('urlform.html')
@app.route('/urlshow',methods=['GET','POST'])
def showurl():
    global url
    url = request.form['url']
    url = ps.Shortener().tinyurl.short(url)
    return render_template('urlshow.html',url=url)

@app.route('/taketext',methods=['POST','GET'])
def takepara():
    return render_template('paraform.html')

@app.route('/translate',methods=['GET','POST'])
def translate():
    try:
        global url
        text = request.form['sentence']
        fromtext = request.form['from']
        totext = request.form['to']
        s = Translator(from_lang=fromtext, to_lang=totext)
        res = s.translate(text)
    except:
        res = "Enter Data Correctly"
    return render_template('showtranslated.html',text = res)


if __name__ == '__main__':
    app.run(debug=True,port=9000)

