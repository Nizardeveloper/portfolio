from flask import *
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def dbfile(data):
    with open('database.txt',mode='a')as db:
        email= data["email"]
        subject= data["subject"]
        message = data["message"]
        file= db.write(f'\n{email},{subject},{message}')

def dbcsv(data):
    with open('database.csv',mode='a', newline='')as db2:
        email= data["email"]
        subject= data["subject"]
        message = data["message"]
        csvw= csv.writer(db2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvw.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            dbcsv(data)
            return redirect('/thank.html')
        except:
            return 'data doesnt saved'
    else:
