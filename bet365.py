import datetime
import requests
from email.message import EmailMessage
import smtplib

fecha_actual = datetime.datetime.now()
fecha_actual = fecha_actual.strftime("%Y-%m-%d %H:%M:%S")
url = "https://football-betting-odds1.p.rapidapi.com/provider1/live/upcoming"

headers = {
	"X-RapidAPI-Key": "7b7f4e10c1mshf3e6da0ff78eed3p137423jsn6e5e339913c3",
	"X-RapidAPI-Host": "football-betting-odds1.p.rapidapi.com"
}

response_json = requests.get(url, headers=headers).json()
country_list=["Spain"]
response_json_filtered = ""
europe_matchs = []
apuestas = []
apuestas_dict = {}
date = ""

for ids in response_json:
  for country in country_list:
    if response_json[ids]["country"] == country:
      date = datetime.datetime.utcfromtimestamp(int(response_json[ids]['startTime']))
      euro_match = {
        "match" : f"{response_json[ids]['home']} - {response_json[ids]['away']}",
        "date" : f"{date}"
      }
      for odd in response_json[ids]['odds'].items():
        apuestas.append(odd)
        for clave, valor in apuestas:
          apuestas_dict[clave] = valor
    
      euro_match['home'] = apuestas_dict['home'] if 'home' in apuestas_dict.keys() else 0
      euro_match['draw'] = apuestas_dict['draw'] if 'draw' in apuestas_dict.keys() else 0
      euro_match['away'] = apuestas_dict['away'] if 'away' in apuestas_dict.keys() else 0

        
      europe_matchs.append(euro_match)

low_risk_matchs = []
fecha_actual = datetime.datetime.strptime(fecha_actual,"%Y-%m-%d %H:%M:%S")

for matchs in europe_matchs:
  
  date = datetime.datetime.strptime(matchs['date'],"%Y-%m-%d %H:%M:%S")
  if date.day == fecha_actual.day:	
    if float(matchs['home']) > 1.1 and float(matchs['home']) < 1.5:
      low_risk_matchs.append(
        {"Partido":matchs['match'],
         "Apuesta":"Local",
         "Ratio":matchs['home']
        })
    elif float(matchs['draw']) > 1 and float(matchs['draw']) < 1.5:
      low_risk_matchs.append(
        {"Partido":matchs['match'],
         "Apuesta":"Empate",
         "Ratio":matchs['draw']
        })
    elif float(matchs['away']) > 1 and float(matchs['away']) < 1.5:
      low_risk_matchs.append(
        {"Partido":matchs['match'],
         "Apuesta":"Visitante",
         "Ratio":matchs['away']
        })  

mail_low_risk = ""
for matchs in low_risk_matchs:
  mail_low_risk +=  f"Partido: {matchs['Partido']} apostando a {matchs['Apuesta']} con un ratio de {matchs['Ratio']}\n"

remitente = "reales1986@gmail.com"
destinatario = "carlosreales030@gmail.com"
mensaje = mail_low_risk
email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Correo de prueba"
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "kuim kalb eoba vykw")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()