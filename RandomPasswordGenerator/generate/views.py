from django.shortcuts import render
import os, random, string
from random import shuffle

# Create your views here.
def RandomPasswordGenerator(request):
    return render(request, 'RandomPasswordGenerator.html', {})
def GeneratedPassword(request):
    return render(request, 'GeneratedPassword.html', {})



total_nr_of_characters = int(input("Total nr of characters"))
nr_of_digits = int(input("nr of digits"))
nr_of_special_characters = int(input("nr of special characters"))
if total_nr_of_characters < 8:
        print("The minimum number of characters is 8")
elif nr_of_digits + nr_of_special_characters < total_nr_of_characters:
          pw = ''
          for i in range(total_nr_of_characters - nr_of_digits - nr_of_special_characters):
              pw += random.choice(string.ascii_letters)
          for d in range(nr_of_digits):
            pw += random.choice(string.digits)
          for s in range(nr_of_special_characters):
            pw += random.choice('!@#$%^&*()')
          word = list(pw)
          shuffle(word)
          shuffle(word)
          print (''.join(word))

else: print("The number of digits plus the number of special characters must be smaller than the total number of characters")

