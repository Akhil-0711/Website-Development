from flask import Flask, render_template

app = Flask(__name__)

BREADS = [
  {
    'id': 1,
    'name': 'Beagle',
    'description':'3yrs old, playful,friendly',
    'location': 'New Delhi',
    'image_path': 'static/beagle_id1.jpg'
  },
  {
    'id': 2,
    'name': 'Spitz',
    'description':'2yrs old, cute,friendly',
    'location': 'New Delhi',
    'image_path': 'static/spitz_id2.jpg'
  },
  {
    'id': 3,
    'name': 'Labrador',
    'description':'3yrs old, playful,friendly',
    'location': 'New Delhi',
    'image_path': 'static/labrador_id3.jpg'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html',
                           breads = BREADS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)