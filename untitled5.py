import sys
import random
import os
import platform
from pyfiglet import Figlet
import time
import requests # added this line to use requests library

# store your NumVerify API keys in a list
api_keys = ["YOUR_API_KEY_1", "YOUR_API_KEY_2", "YOUR_API_KEY_3"]

def clear():

    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')


num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

custom_fig = Figlet(font='graffiti')
print(custom_fig.renderText('Phone Generator'))
print('mrhouse998')
time.sleep(5)
clear()

print('Please Select from list ♥ : \n')
print('1 - Phone Genrator Australia')
print('2 - Phone Genrator Usa')
print('0 - Quit the Program')
print('--- CTRL + C to stop generating---')
a = input('Your Choice : ')

clear()
print(custom_fig.renderText('itslucifero'))

try:
        if a == '1':
            codes1 = ['2', '3', '4', '7', '8']
            code = '+61'

            file = open('AUSphone.txt', 'a')
            c = ''
            while c != 0 :
                for a in random.choice(num):
                    for b in random.choice(num):
                        for c in random.choice(num):
                            for d in random.choice(num):
                                for e in random.choice(num):
                                    for f in random.choice(num):
                                        for g in random.choice(num):
                                            for h in random.choice(num):
                                                number = ares+a+b+c+d+e+f+g+h
                                                ares = random.choice(codes1)
                                                # added this block to validate the number using NumVerify API
                                                api_key = random.choice(api_keys) # select a random API key
                                                response = requests.get(f'http://apilayer.net/api/validate?access_key={api_key}&number={code+number}&country_code=AU&format=1')
                                                if response.status_code == 200: # check if the request was successful
                                                    data = response.json() # get the json data of the response
                                                    if data['valid'] and data['line_type'] == 'mobile': # check if the number is valid and mobile
                                                        file.write(number+'\n')
                                                        print('PHONE ', number)
                                                    else: # skip the number if it is not valid or mobile
                                                        continue
                                                else: # handle the case when the request failed
                                                    print(f'Sorry, I could not validate the number {number}')

        elif a == '2':
            # added this block to ask for a US zip code and get the corresponding area code
            zip_code = input('Please enter a US zip code: ')
            response = requests.get(f'https://www.zip-codes.com/search.asp?fld-zip={zip_code}&selectTab=0&srch-type=zip') # using an external website to get the area code
            if response.status_code == 200: # check if the request was successful
                html = response.text # get the html content of the response
                start = html.find('Area Code:') # find the start index of the area code
                end = html.find('</a>', start) # find the end index of the area code
                area_code = html[start+17:end] # extract the area code
                print(f'The area code for zip code {zip_code} is {area_code}')
            else: # handle the case when the request failed
                print(f'Sorry, I could not find the area code for zip code {zip_code}')

            code = '+1'

            file = open('USAphone.txt', 'a')
            b = ''
            while b != 0 :
                for a in random.choice(num):
                    for b in random.choice(num):
                        for c in random.choice(num):
                            for d in random.choice(num):
                                for e in random.choice(num):
                                    for f in random.choice(num):
                                        for g in random.choice(num):
                                            number = code+area_code+a+b+c+d+e+f+g # modified this line to use the area code
                                            # added this block to validate the number using NumVerify API
                                            api_key = random.choice(api_keys) # select a random API key
                                            response = requests.get(f'http://apilayer.net/api/validate?access_key={api_key}&number={number}&country_code=US&format=1')
                                            if response.status_code == 200: # check if the request was successful
                                                data = response.json() # get the json data of the response
                                                if data['valid'] and data['line_type'] == 'mobile': # check if the number is valid and mobile
                                                    file.write(number+'\n')
                                                    print('PHONE ', number)
                                                else: # skip the number if it is not valid or mobile
                                                    continue
                                            else: # handle the case when the request failed
                                                print(f'Sorry, I could not validate the number {number}')
except requests.exceptions.RequestException as e: # catch the requests library errors
    print(f'Something went wrong with the request: {e}')
except Exception as e: # catch any other errors
    print(f'Something went wrong with the script: {e}')
finally: # execute this code no matter what
    file.close() # close the file
    print('The script has finished')
