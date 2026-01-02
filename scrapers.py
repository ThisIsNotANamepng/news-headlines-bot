import requests
from bs4 import BeautifulSoup
import time

def get_soup(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # Save response.text in file in a structured directory
    #  
    return soup


def guardian_us():
    url = "https://www.theguardian.com/us"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a", attrs={"aria-label": True}):
        headlines.append(a["aria-label"])

    return headlines

def guardian_world():
    url = "https://www.theguardian.com/world"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a", attrs={"aria-label": True}):
        headlines.append(a["aria-label"])

    return headlines

def cnn():
    url = "https://www.cnn.com/"
    soup = get_soup(url)
    headlines = []

    for span in soup.find_all("span", attrs={"data-editable": "headline"}):
        headlines.append(span.get_text(strip=True))
    return headlines

def nytimes():
    # Doesn't capture all

    url = "https://www.nytimes.com/"
    soup = get_soup(url)
    headlines = []

    for element in soup.find_all(class_="indicate-hover"):
        if len(element.get_text(strip=True).split()) > 3 and element.get_text() != "Play Connections: Sports Edition":
            headlines.append(element.get_text(strip=True))
    return headlines

def bbc():    
    url = "https://www.bbc.com/"
    soup = get_soup(url)
    headlines = []

    for element in soup.find_all(attrs={"data-testid": "card-headline"}):
        headlines.append(element.get_text(strip=True))
    return headlines

def foxnews():
    # Filters filtering for headlines < 4 words
    
    url = "https://www.foxnews.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a", attrs={"data-omtr-intcmp": True}):
        if len(a.get_text(strip=True).split()) > 3:
            headlines.append(a.get_text(strip=True))
    return headlines

def reuters():
    # Doesn't work, Reuters requires JS to load

    url = "https://www.reuters.com/"
    soup = get_soup(url)
    headlines = []

    for element in soup.find_all(attrs={"data-testid": "TitleHeading"}):
        headlines.append(element.get_text(strip=True))
    return headlines

def forbes():    
    url = "https://www.forbes.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a"):
        if "Forbes" not in a.get_text(strip=True) and len(a.get_text(strip=True).split()) > 3:
            headlines.append(a.get_text(strip=True))
    return headlines

def usatoday():    
    url = "https://www.usatoday.com/"
    soup = get_soup(url)
    headlines = []

    for element in soup.find_all(attrs={"data-tb-title": ""}):
        headlines.append(element.get_text(strip=True))
    return headlines

def apnews():    
    url = "https://www.apnews.com/"
    soup = get_soup(url)
    headlines = []

    for element in soup.find_all(class_="PagePromoContentIcons-text"):
        headlines.append(element.get_text(strip=True))
    return headlines

def usnews():    
    url = "https://www.usnews.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a"):
        if "Forbes" not in a.get_text(strip=True) and len(a.get_text(strip=True).split()) > 3:
            headlines.append(a.get_text(strip=True))
    return headlines

def wapo():    
    url = "https://www.washingtonpost.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("span"):
        if "Forbes" not in a.get_text(strip=True) and len(a.get_text(strip=True).split()) > 3:
            headlines.append(a.get_text(strip=True))
    return headlines

def npr():    
    url = "https://www.npr.org/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("h3"):
        if "Forbes" not in a.get_text(strip=True) and len(a.get_text(strip=True).split()) > 3:
            headlines.append(a.get_text(strip=True))
    return headlines

def cnbc():    
    url = "https://www.cnbc.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a"):
        headlines.append(a.get_text(strip=True))
    return headlines

def bloomberg():    
    url = "https://www.bloomberg.com/"
    soup = get_soup(url)
    headlines = []

    for a in soup.find_all("a"):
        headlines.append(a.get_text(strip=True))
    return headlines
