from flask import Flask, render_template, url_for, request, redirect 
import csv
app = Flask(__name__)
print(__name__)

@app.route('/<page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'Email: {email}\nSubject: {subject}\nMessage: {message}\n')

def write_to_csv(data):
    with open('database.csv', newline = '', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'

if __name__ = '__main__':
    app.run()