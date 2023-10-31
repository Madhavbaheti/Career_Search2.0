from flask import Flask, render_template, jsonify,request,url_for,redirect
from database import load_jobs,load_specific_job,add_application_to_db

app = Flask(__name__)
app.debug = True

# Database connection configuration




@app.route('/')
def index():
    jobs = load_jobs()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs/')
def list_jobs():
    jobs = load_jobs()
    return jsonify(jobs)


@app.route("/jobs/<id>/apply", methods=["POST"])
def get_application(id):
    data = request.form
    job = load_specific_job(id)
    response = add_application_to_db(job['id'], data)

    if response['success']:
        
        return render_template('application_submitted.html', application=data, job=job,email_already_used = False)
    else:
        if response.get('status') == 500:
            return render_template('jobinfo.html',job=job,email_already_used=True)
      



@app.route('/jobs/<id>')
def show_job(id):
    job = load_specific_job(id)
    return render_template('jobinfo.html', job=job)


if __name__ == '__main__':
    app.run(debug=True)
