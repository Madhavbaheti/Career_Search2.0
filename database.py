import mysql.connector
from flask import jsonify


db_config = {
    'user': 'root',
    'password': 'Madhav@123',
    'host': 'localhost',
    'database': 'career_search'
}

def load_jobs():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM jobs")
        jobs = cursor.fetchall()
        cursor.close()
        conn.close()
        return jobs
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []

def load_specific_job(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM jobs WHERE id = %s", (id,))
        job = cursor.fetchone()
        cursor.close()
        conn.close()
        return job if job else None

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def add_application_to_db(job_id, data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        check_query = "SELECT id FROM applications WHERE email = %(email)s LIMIT 1"
        cursor.execute(check_query, {'email': data['email']})
        existing_record = cursor.fetchone()

        if existing_record:
            response={'success': False, 'message':'email already present','status': 500}
            return response 

        insert_query = """
            INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)
            VALUES (%(job_id)s, %(full_name)s, %(email)s, %(linkedin_url)s, %(education)s, %(work_experience)s, %(resume_url)s)
        """

        cursor.execute(insert_query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['experience'],
            'resume_url': data['resume_url']
        })

        conn.commit()
        cursor.close()
        conn.close()

        response = {'success': True, 'message': 'Application added successfully'}
    
        return response

    except Exception as e:
        print(f"Error: {e}")
        response = {'success': False, 'message': 'An error occurred while processing the application'}
        return response


    except mysql.connector.Error as err:
        print(f"Error: {err}")
        response = {'success': False, 'error_message': str(err)}
        return response

