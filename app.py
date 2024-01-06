from flask import Flask, render_template

app = Flask(__name__)

BREADS = [
  {
    'id': 1,
    'name': 'Beagle',
    'description':'3yrs old, playful,friendly',
    'location': 'New Delhi'
  },
  {
    'id': 2,
    'name': 'Splitz',
    'description':'2yrs old, cute,friendly',
    'location': 'New Delhi'
  },
  {
    'id': 3,
    'name': 'Labra',
    'description':'3yrs old, playful,friendly',
    'location': 'New Delhi'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           breads = BREADS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)