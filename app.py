from flask import Flask, render_template,request,flash
import pyowm
APIKEY='55b1b0f3bae0226fb44ac0c3f4f8578e'
OpenWMap=pyowm.OWM(APIKEY) 
mgr=OpenWMap.weather_manager()
app=Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'  
cityL=[]
weatherL=[]
def weatherA(city):
    try:
        weather=mgr.weather_at_place(city)
        Data=weather.weather
        tempC = Data.temperature('celsius')
        tempF = Data.temperature('fahrenheit')

        avgC=tempC['temp']
        avgF=tempF['temp']
        Temp=f"Average Temperature of {city} is {avgC} deg. Celcius or {avgF} deg. Farenheit"
        return str(Temp)
    except Exception as e:
        return e

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods = ['POST', 'GET'])
def seeWeather():
   if request.method == 'POST':
      city = request.form['city']
      temp=weatherA(city)
      return render_template('index.html',temp=temp)



app.run(debug=True)
