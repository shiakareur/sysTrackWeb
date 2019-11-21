from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/indicadores")
def indicadores():
    return render_template("indicadores.html")

if __name__=="__main__":
    app.run()

