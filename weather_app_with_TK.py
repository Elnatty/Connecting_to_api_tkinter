from tkinter import *
import requests
import json

root = Tk()
root.iconbitmap('computer.ico')

#root.geometry('400x50')
# url = https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A5DC957A-2918-40A8-8D1D-6684DAB8C4C6
# we use error handling to check for errors.
# define wrapper function for button (ie zip lookup).
def ziplookup():
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=A5DC957A-2918-40A8-8D1D-6684DAB8C4C6")
    # we call the json library and use the .content method to load the api request since we know its a json file.
    api = json.loads(api_request.content)
    city = api[0].get('ReportingArea')
    quality = api[0].get('AQI')
    category = api[0]['Category'].get('Name')

    # conditionals to determine colors..
    if category == 'Good':
        weather_color = '#00e400'
    elif category == 'Moderate':
        weather_color = '#ffff00'
    elif category == 'Unhealthy for Sensitive Groups':
        weather_color = '#ff7e00'
    elif category == 'Unhealthy':
        weather_color = '#ff0000'
    elif category == 'Very Unhealthy':
        weather_color = '#8f3f97'
    elif category == 'Hazardous':
        weather_color = '#7e0023'

    root.configure(background=weather_color)

    l1 = Label(root, text=city + ' Air Quality ' + str(quality) + ' ' + category, font=('Helvetica', 20),
               bg=weather_color)
    l1.grid(row=1, column=0, columnspan=2)



# entry form
zip = Entry(root,)
zip.grid(row=0, column=0, sticky=W+E+N+S)

zipbutton = Button(root, text='Lookup Zipcode', command=ziplookup)
zipbutton.grid(row=0, column=1, sticky=W+E+N+S)

root.mainloop()