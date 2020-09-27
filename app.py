from flask import Flask, render_template, request
import csv, urllib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')  # render a template

@app.route('/search', methods=('POST',))
def search():
    
    countryName = request.form['countryName']

    url = 'http://winterolympicsmedals.com/medals.csv'
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()] 
    reader = csv.reader(lines)
    results = filter(lambda x: countryName in x, reader)

    return render_template('data-return.html', data=results, type="Olympics")


# # start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)