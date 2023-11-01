from flask import Flask,render_template,url_for,redirect,request
from flask_mysqldb import MySQL
import requests
import mysql.connector
from modules.apiFunctions import getCountries,getCompetitions,getEvents,getMatch,getHeadToHead,getTeam



app = Flask(__name__)
# Configura los datos de conexión
config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "futbol"
}

# Crea una conexión a la base de datos
connection = mysql.connector.connect(**config)

# Crea un cursor para ejecutar consultas


@app.route('/')
def inicio():
    return render_template("index.html")

@app.route('/buscador',methods=['GET', 'POST'])
def buscador():
    countries = getCountries()["countries"]
    response = getCountries()["response"]
    mostrar_competicion = False
    pais = "0"
    competicion = "0"
    competitions = "0"
    events = "0"
    if request.method == "POST":
        pais = request.form.get('pais') 
        competitions = getCompetitions(pais)["competitions"]
        response = getCompetitions(pais)["response"]
    
    if pais != '0':
        mostrar_competicion = True
        competicion = request.form.get('competicion') or "0"
    else:
        mostrar_competicion = False
    if competitions != "0":
        events = getEvents(request.form.get('competicion'))["events"]

    # Check if the request was successful
    if response.status_code == 200:
        return render_template('buscador_eventos.html',
                               countries=countries, 
                               mostrar_competicion=mostrar_competicion,
                               pais=pais,
                               competitions=competitions,
                               competicion=competicion,
                               events=events)
    else:
        print("Error: Unable to retrieve data. Status code:", response.status_code)
    

@app.route('/insertar-partido', methods = ['GET','POST'])
def insertar_partido():
    if request.method == "POST":

        local = request.form['local']
        visitante = request.form['visitante']
        resultado = request.form['resultado']

        return f"{local} {visitante} {resultado}"

        """r = connection.cursor()
        insert_query = "INSERT INTO partidos VALUES (NULL,%s, %s, %s)"
        data = ("Real Madrid", "Osasuna", "2-1")
        cursor.execute(insert_query, data)
        connection.commit()
        return redirect(url_for('inicio')) """
    return render_template('insertar_partido.html')
#PARTIDO
@app.route('/partido')
@app.route('/partido/<string:id>')
def partido(id = None):
    if id != None:
        match = getMatch(id)["events"]
        h2h = getHeadToHead(match[0]["match_hometeam_id"],match[0]["match_awayteam_id"])
        return render_template('partido.html',
                               id=id,
                               match=match,
                               h2h=h2h["h2h"]
                               )
    return render_template('partido.html')

@app.route('/equipo')
@app.route('/equipo/<string:id>')
def equipo(id = None):  
    if id != None:
        team = getTeam(id)["team"][0]
        return render_template('equipo.html',
                               team=team
                               )
    return render_template('equipo.html')

if __name__ == '__main__':
    app.run(debug=True)



