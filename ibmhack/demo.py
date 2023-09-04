from flask import Flask, render_template, request
import os
os.add_dll_directory(r'C:\Users\haris\anaconda3\Lib\site-packages\clidriver\bin')
import ibm_db

app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=98538591-7217-4024-b027-8baa776ffad1.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=30875;UID=hlh20247;PWD=WwDIq5ImrO7lj72Y;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt", '', '')

print(conn)
connState = ibm_db.active(conn)
print(connState)

@app.route('/')
def index():
    return render_template('new.html')

@app.route('/print_value', methods=['POST'])
def print_value():
    name = request.form.get('name')
    age = request.form.get('age')
    subject = request.form.get('subject')
    date = request.form.get('date')
    time = request.form.get('time')

    # Insert the value into the database
    sql = "INSERT into REGISTER_HC (NAME, AGE, SUBJECT, DATE, TIME) VALUES (?, ?, ?, ?, ?)"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, name)
    ibm_db.bind_param(stmt, 2, age)
    ibm_db.bind_param(stmt, 3, subject)
    ibm_db.bind_param(stmt, 4, date)
    ibm_db.bind_param(stmt, 5, time)

    if ibm_db.execute(stmt):
        ibm_db.commit(conn)
        print(f"The Name submitted from the form is: {name}")
        print(f"The Age submitted from the form is: {age}")
        print(f"The Subject submitted from the form is: {subject}")
        print(f"The Date submitted from the form is: {date}")
        print(f"The Time submitted from the form is: {time}")
        return "Name printed in terminal and inserted into the database."
    else:
        return "Error inserting data into the database."

if __name__ == '__main__':
    app.run(debug=True)
