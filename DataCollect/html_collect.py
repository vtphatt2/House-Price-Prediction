import requests
from bs4 import BeautifulSoup

def get_and_save_html(url, filename):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    html_content = soup.prettify() 

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Successfully saved HTML content of {url} to {filename}")

url = "https://batdongsan.vn/chua-toi-30trm2-hang-ngop-bank-bao-dau-tu-ha-chao-11-ty-r285164"  
filename = "../Data/source_file.html"

get_and_save_html(url, filename)

