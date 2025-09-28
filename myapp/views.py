from django.shortcuts import render
import pandas as pd  # For CSV file handling

# Homepage
def home(request):
    return render(request, 'index.html')

# Prediction View
def predict_view(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')

        if csv_file:
            try:
                df = pd.read_csv(csv_file)

                # Assumes 'internal' column exists and has numeric values
                if 'internal' not in df.columns:
                    return render(request, 'predict.html', {'error': "Missing 'internal' column in CSV."})

                result = "Pass" if df.iloc[0]['internal'] > 40 else "Fail"
            except Exception as e:
                return render(request, 'predict.html', {'error': f"Error processing CSV: {str(e)}"})

        else:
            try:
                hours = float(request.POST.get('hours', 0))
                attendance = float(request.POST.get('attendance', 0))
                internal = float(request.POST.get('internal', 0))
                previous = request.POST.get('previous', 'Fail')

                # Simple rule-based logic
                result = "Pass" if internal > 40 and attendance > 75 and previous == "Pass" else "Fail"
            except Exception as e:
                return render(request, 'predict.html', {'error': f"Error in form input: {str(e)}"})

        return render(request, 'predict.html', {'prediction': result})

    return render(request, 'index.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Help Page
def help(request):
    return render(request, 'help.html')

from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject,
            full_message,
            'officialedimaxstudio@gmail.com',  # FROM
            ['akashmasal779@gmail.com'],      # TO
            fail_silently=False,
        )
        return HttpResponse('Message sent successfully!')
    return render(request, 'contact.html')
