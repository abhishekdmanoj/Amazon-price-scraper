import requests                     #requests is what fetches the actual html
from bs4 import BeautifulSoup

def scrape_amazonproduct(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  #disguise our requests as if its from a browser to bypass bot checks
    }

    try:                                                        #throw error messages for any codes except success(200)
        response = requests.get(url, headers=headers)
        response.raise_for_status()                             #the exception is thrown here

        soup = BeautifulSoup(response.text, "html.parser")      #parses the html

        title_tag = soup.find(id = "productTitle")              #replace the id with whichever website product you need to track
        
        if title_tag:
            title = title_tag.get_text().strip()                #fetches product name(website specific)
        
        else:
            title = "Title not found"

        
        price_tag = soup.find(id = "priceblock_dealprice")      #always check for deal/offerprice to ensure lowest price given priority

        if not price_tag:
            price_tag = soup.find(id = "priceblock_ourprice")
        if not price_tag:
            price_tag = soup.find("span", class_="a-price-whole")


        if price_tag:
            price = price_tag.get_text().strip()

        else:
            price = "Price not found"


        return title, price
    

    except Exception as e:                                      #error message if scraping fails
        print("Error scraping: ", e)

        return None, None
    



    #for testing

if __name__ == "__main__":
    url = "https://www.amazon.in/dp/B0CFTZQ8JB"
    title, price = scrape_amazonproduct(url)
    print("Title:", title)
    print("Price:", price)
