import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# ---------------------------
# Function for Scraping Amazon
# ---------------------------

def scrape_amazon(base_url, pages, file_name, category="Product"):
    products = []

    for page in range(1, pages + 1):
        url = base_url.format(page=page)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all("div", {
            "class": "a-section a-spacing-small puis-padding-left-small puis-padding-right-small"
        })

        for item in items:

            # Name
            if category == "Mobiles":
                item_name = item.h2.text.strip() if item.h2 else 'N/A'
            elif category == "Laptops":
                name_tag = item.find("span")
                item_name = name_tag.text.strip() if name_tag else "N/A"


            # Rating
            item_rate = item.find("span", {"class": "a-icon-alt"})
            item_rate = item_rate.text.strip() if item_rate else "N/A"

            # Price
            item_price = item.find("span", {"class": "a-offscreen"})
            item_price = item_price.text.strip() if item_price else "N/A"

            products.append([item_name, item_rate, item_price])

        print(f"{category} - Page {page} scraped successfully!")
        time.sleep(2)  # avoid blocking

    # Save to CSV
    df = pd.DataFrame(products, columns=["Name", "Rating", "Price"])
    df.to_csv(file_name, index=False, encoding='utf-8-sig')
    print(f"The Data are Saved in {file_name}")

    return df


# ---------------------------
# Scraping Mobiles
# ---------------------------
mobiles_url = "https://www.amazon.eg/s?i=electronics&rh=n%3A21832883031&s=popularity-rank&fs=true&language=en&ref=lp_21832883031_sar&page={page}"
df_mobiles = scrape_amazon(mobiles_url, pages=19,file_name="Amazon_Mobiles.csv", category="Mobiles")

# ---------------------------
# Scraping Laptops
# ---------------------------
laptops_url = "https://www.amazon.eg/s?k=Laptops&page={page}&ref=sr_pg_{page}"
df_laptops = scrape_amazon(laptops_url, pages=20,file_name="Amazon_Laptops.csv", category="Laptops")
