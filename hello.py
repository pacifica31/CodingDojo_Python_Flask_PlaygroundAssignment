from flask import Flask,render_template
app = Flask(__name__)

@app.route("/play")
def level1():
    return render_template('index.html', count = 1)

@app.route("/play/<int:num>")
def level2(num):
    
    print(num)
    return render_template('index.html', count = num)

@app.route("/play/<int:num>/<color>")
def level3(num, color):
    return render_template('index.html', count = num, displayMe = color)


if __name__ == "__main__":
    app.run(debug=True)