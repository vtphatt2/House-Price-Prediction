import requests
from bs4 import BeautifulSoup

def get_and_save_html(url, filename):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    html_content = soup.prettify() 

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Successfully saved HTML content of {url} to {filename}")

url = "https://batdongsan.vn/cua-nhua-gia-re-lap-dat-phong-ngu-va-toilet-cua-nhua-dai-loan-r285126"  
filename = "../Data/source_file.html"

get_and_save_html(url, filename)

