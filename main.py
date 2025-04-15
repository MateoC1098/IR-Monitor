from news_scraper.scraper_portfolio import scrape_portafolio
import pandas as pd
import os

def guardar_csv(noticias, nombre_archivo):
    df = pd.DataFrame(noticias)
    os.makedirs("data", exist_ok=True)
    df.to_csv(f"data/{nombre_archivo}", index=False)
    print(f"{len(noticias)} noticias guardadas en data/{nombre_archivo}")

def main():
    print("Scrapeando Portafolio...")
    noticias_portafolio = scrape_portafolio()
    guardar_csv(noticias_portafolio, "noticias_portafolio.csv")

if __name__ == "__main__":
    main()
