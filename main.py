from scrapers import *
import csv
from datetime import datetime

functions = [nytimes, guardian_us, guardian_world, cnn, bbc, foxnews, forbes, usatoday, apnews, npr]

with open("headlines.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)


    for source in functions:

        headlines = source()

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        for headline in headlines:
            writer.writerow([headline, timestamp, source.__name__])



