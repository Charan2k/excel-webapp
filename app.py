from flask import Flask, render_template, redirect
from flask.globals import request
from numpy import dtype
import pandas as pd


app = Flask("excel-app")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/details', methods=['POST','GET'])
def details():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        path = './static/database/data.xlsx'
        df1 = pd.read_excel(path)
        names = list(df1["Name"])
        emails = list(df1["Email"])
        names.append(name)
        emails.append(email)
        df = pd.DataFrame({"Name": names, "Email": emails})
        df.to_excel(path, index=False)
        df.to_excel('./static/database/userfile.xlsx', index=False)
        return render_template("details.html", names=names, emails=emails, length =len(names))
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5050)
