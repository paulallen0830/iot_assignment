from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://iot-demo-b1f30-default-rtdb.firebaseio.com/"
})

# Create your views here.

ref = db.reference()  # Reference to the root of your Firebase database

def home_view(request):
    return render(request, 'myApp/home.html')

def insert_sensor(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        sensor_ref = ref.child('SENSOR')  # Reference to 'SENSOR' node in Firebase
        sensor_ref.update({key: value})
        return render(request, 'myApp/success.html')  # Redirect to success page
    return render(request, 'myApp/insert_sensor.html')

def insert_user(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        user_ref = ref.child('USER')  # Reference to 'USER' node in Firebase
        user_ref.update({key: value})
        return render(request, 'myApp/success.html')  # Redirect to success page
    return render(request, 'myApp/insert_user.html')