from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

app.run(port='8000')

"""...and when I navigate to 
    http://127.0.0.1:8000/ in 
    a web browser, I should 
    see a website that says 
    Hello, World!  """