from flask import Flask, render_template  , request # type: ignore
import RPi.GPIO as GPIO # type: ignore
import time

 
app = Flask(__name__)
 
GPIO.setmode(GPIO.BCM)


 
# Set each pin as an output and make it low:

GPIO.setup(21, GPIO.OUT)
GPIO.output(21, GPIO.LOW)
 
@app.route("/")
 
def main():
   return render_template('main.html')

# The function below is executed when someone requests a URL with the pin number and action in it:
 
@app.route("/caldaia" , methods=['POST'] )
def caldaia():
  print("Bottone Premuto")
  if request.method == 'POST':
      print(request.form)
      if request.form.get('stato') == 'ON':
          GPIO.output(21, GPIO.HIGH)
      if request.form.get('stato') == 'OFF':
          GPIO.output(21, GPIO.LOW)
      return('', 204)


@app.route('/temperatura' ,methods=['POST'])
def temperatura():
   print("Temperatura Richiesta")  
   if request.method == 'POST': 
    temperature = ''
    humidity = ''
   
    
 
   
   print("Temperatura :" + temperature) 
   return (temperature , 201)
 
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)