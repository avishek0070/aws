from flask import Flask,render_template

app = Flask(__name__)

#Using decorators to define which path provokes which function.
#These paths can be considered as different endpoints in the program.
#Since no method is passed in route we will treat as GET by default.

@app.route('/', endpoint="home")
def home():
    return render_template('home.html')

@app.route('/about/', endpoint="about")
def about():
    return render_template('about.html')

@app.route('/about/contact/', endpoint="about_contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
        app.run(host="0.0.0.0",port=int("5000"),debug=True)
    
    #In Case we have to load it using terminal:
    #export FLASK_APP=myapp1
    #export FLASK_ENV=development
    #flask run
