from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app= Flask(__name__)
translator = Translator()
langage = LANGUAGES

@app.route('/')
def index():
    return render_template('index.html', langages_disponible = langage)

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        traduction = request.form['traduction']
        if traduction == '':
            return render_template('index.html', message='Met un texte pd')
        return render_template('success.html', message = translator.translate(traduction).text)

if __name__ == '__main__':
    app.debug = True
    app.run()
