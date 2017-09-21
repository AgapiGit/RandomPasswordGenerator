from django.shortcuts import render
import random, string
from random import shuffle

from django.template.response import SimpleTemplateResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def RandomPasswordGenerator(request):
    return render(request, 'RandomPasswordGenerator.html', {})


@csrf_exempt
def generate_password(request):
    result = ''
    total_nr_of_characters = int(request.POST.get('total_nr_of_characters'))
    nr_of_digits = int(request.POST.get('nr_of_digits'))
    nr_of_special_characters = int(request.POST.get('nr_of_special_characters'))
    if total_nr_of_characters < 8:
        result = "The minimum number of characters is 8"
    elif nr_of_digits + nr_of_special_characters < total_nr_of_characters:
        pw = ''
        for i in range(total_nr_of_characters - nr_of_digits - nr_of_special_characters):
            pw += random.choice(string.ascii_letters)
        for d in range(nr_of_digits):
            pw += random.choice(string.digits)
        for s in range(nr_of_special_characters):
            pw += random.choice('!@#$%^&*()')
        password = list(pw)
        shuffle(password)
        shuffle(password)
        result = ''.join(password)
    else:
        result = "The number of digits plus the number of special characters must be smaller than the total number of characters"
    return SimpleTemplateResponse(template='GeneratedPassword.html', context={'password': result})
