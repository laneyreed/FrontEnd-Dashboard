from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


#****************************CSS Routes*****************************************
@app.route("/css")
def css_home():
    return render_template("css/css_home.html")

@app.route("/css_concept/display")
def css_display():
    return render_template("./css/fundamentals/display.html")




if __name__ == "__main__":
    app.run(debug=True)