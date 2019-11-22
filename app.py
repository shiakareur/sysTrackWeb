from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/Escuelaclj")
def escuelaclj():
    return render_template("escuelaclj.html")

@app.route("/Hitos")
def hitos():
    return render_template("hitos.html")

@app.route("/Malla")
def malla():
    return render_template("malla.html")

@app.route("/Testimonios")
def testimonios():
    return render_template("testimonios.html")

@app.route("/Instructores")
def instructores():
    return render_template("instructores.html")

@app.route("/Postclj")
def postclj():
    return render_template("postclj.html")

@app.route("/Indicadores")
def indicadores():
    return render_template("indicadores.html")

@app.route("/SysTrack")
def systrack():
    return render_template("systrack.html")

if __name__=="__main__":
    app.run()

