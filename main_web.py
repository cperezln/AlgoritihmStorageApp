from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/null')
def null():
    s = []
    with open("codes/Sorting.py") as f:
        lines = f.readlines()
        i = 0
        while lines[i] != "#Mergesort\n":
            i+=1
        for j in range(i + 1, len(lines)):
            s.append(lines[j])
    return render_template("null.html", code_list = s)
if __name__ == '__main__':
    app.run(debug=True)
