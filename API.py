#Importamos librerias
from flask import Flask, request
from flask import jsonify
import markdown.extensions.fenced_code
import Tools.getdata as get
import Tools.postdata as pos

app = Flask(__name__)

#PÁGINA DE INICIO
@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extensions = ["fenced_code"]
    )
    return md_template

#GET
@app.route("/UN")
def UN():
    UN = get.list_UN()
    return jsonify(UN)

@app.route("/year")
def year():
    year = get.list_year()
    return jsonify(year)

@app.route("/country")
def country():
    country = get.list_country()
    return jsonify(country)

@app.route("/speech")
def speech():
    speech = get.list_speech()
    return jsonify(speech)


# GET DINÁMICA/PARAMETRIZADA
@app.route("/speech_country/<country>")
def speech_country(country):
    res_country = get.sentence_country(country)
    return jsonify(res_country)

@app.route("/speech_year/<year>")
def speech_year(year):
    year = int(year)
    res_year = get.sentence_year(year)
    return jsonify(res_year)

@app.route("/speech_year_country/<year>/<country>")
def speech_year_country(year,country):
    year = int(year)
    res_year_country = get.sentence_year_country(year,country)
    return jsonify(res_year_country)


#POST
@app.route("/speech_new", methods=["POST"])
def speech_insert():
    country = request.form.get("Country")
    speech = request.form.get("Speech")
    year = request.form.get("Year")
    pos.insert_quote (country,speech,year)
    return "Se ha insertado el mensaje correctamente en la base de datos"


app.run("0.0.0.0", 5000, debug=True)