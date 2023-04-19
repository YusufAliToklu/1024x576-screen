import requests
import tkinter as tk
import datetime
import requests
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import tkinter as tk
root = tk.Tk()
root.geometry("1024x576")
root.configure(background='black')

# saat ve tarih fonksiyonu
def tick():
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time_label.config(text=now.strftime("%H:%M:%S") + "\n" + date)
    time_label.after(1000, tick)

time_label = tk.Label(root, font=('Times New Roman', 40, 'bold'), background='black', foreground='white', padx=20, pady=20)
time_label.grid(row=0, column=0, sticky="nw")
tick()

# hava durumu fonksiyonu
def get_weather():
    city = "İzmir"
    api_key = "f0c975eaea18d867a146646de4607a23"  # OpenWeather API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=tr"
    response = requests.get(url)
    weather_data = response.json()

    if 'main' in weather_data:
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        temp_label.config(text=f"{temp} °C\n{description}\n"+city)
        
    else:
        temp_label.config(text="Hava durumu bilgisi alınamadı.")
        
    temp_label.after(60000, get_weather)  # her dakika güncelle

temp_label = tk.Label(root, font=('Times New Roman', 30,'bold'), background='black', foreground='white', padx=20, pady=10)
temp_label.grid(row=0, column=1, sticky="en")
get_weather()


# haberler fonksiyonu

def get_news():
    url = "https://newsapi.org/v2/top-headlines?country=tr&apiKey=34f3ccd95b7942af96ddf25b0b806129"  # News API key
    response = requests.get(url)
    news_data = response.json()

    articles = news_data["articles"][:7]  # Sadece ilk 5 haber alınıyor
    headlines = "\n\n".join([article["title"] for article in articles])
    news_label.config(text=headlines)
    news_label.after(60000, get_news)  # 3 saniyede bir güncelle

news_label = tk.Label(root, font=('calibri', 15), background='black', foreground='white', padx=20, pady=20, wraplength=1000)
news_label.grid(row=1, column=0, columnspan=2, sticky="n")

get_news()

root.mainloop()
