import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_portafolio():
    url = "https://www.portafolio.co/economia"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error al acceder a Portafolio")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("div", class_="listing-default")  # Bloques de noticias
    
    data = []
    for article in articles:
        try:
            title_tag = article.find("a", class_="title")
            title = title_tag.text.strip()
            link = "https://www.portafolio.co" + title_tag.get("href")

            summary_tag = article.find("div", class_="description")
            summary = summary_tag.text.strip() if summary_tag else "Sin resumen"

            data.append({
                "fuente": "Portafolio",
                "titulo": title,
                "resumen": summary,
                "link": link
            })
        except Exception as e:
            print("Error procesando artículo:", e)

    return data
