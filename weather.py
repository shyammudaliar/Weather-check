import requests
from pprint import pprint 

def bycity():    
    city=input("Enter name of city:")
    url="https://openweathermap.org/data/2.5/weather?q={}&appid=b6907d289e10d714a6e88b30761fae22".format(city)
    res=requests.get(url)
    data=res.json()
    display_data(data)


def byzip():
    zipcode=input("Enter zip code:")
    url="https://openweathermap.org/data/2.5/weather?zip={},us&appid=b6907d289e10d714a6e88b30761fae22".format(zipcode)
    res=requests.get(url)
    data=res.json()
    display_data(data)

def display_data(data):
    temp=data['main']['temp']
    humidity=data['main']['humidity']
    wind_speed=data['wind']['speed']
    latitude=data['coord']['lat']
    longitude=data['coord']['lon']


    print("Temperature:",temp,"Farheneit")
    print("Humidity:",humidity)
    print("Wind Speed",wind_speed)
    print("Latitude:",latitude)
    print("Longitude",longitude)
    
def main():
    print('1. Print data by city')
    print("2. Print data by code")
    option=input("Enter option 1 or 2: ")
    if option=='1':
        bycity()
    else:
        byzip()

if __name__=='__main__':
      main()

