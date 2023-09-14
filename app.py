from flask import Flask,render_template,jsonify

app=Flask(__name__)

app.debug = True

JOBS=[
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'New York City, USA',
      
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'San Francisco, USA',
        'salary': '$120,000'
    },
   {
        'id': 3,
        'title': 'Marketing Manager',
        'location': 'New York City, USA',
        'salary': '$90,000'
    },
    {
        'id': 4,
        'title': 'Graphic Designer',
        'location': 'London, UK',
        'salary': '£40,000'
    },
   {
        'id': 5,
        'title': 'Project Manager',
        'location': 'Toronto, Canada',
        'salary': 'CAD 90,000'
    }
]

@app.route('/')
def index():
    return render_template('home.html',jobs=JOBS)


@app.route('/api/jobs')
def list_jobs():
   return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)