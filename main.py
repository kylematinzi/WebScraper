import requests
from bs4 import BeautifulSoup
import csv


# Webpage URL
url = 'https://finance.yahoo.com/crypto/'


def main():
    # Send the HTTP request
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find the crypto table
    table = soup.find('table', {'class': 'W(100%)'})
    # Extract table headers
    headers = [th.text for th in table.find_all('th')]
    # Extract table rows
    rows = []
    for tr in table.find_all('tr'):
        row = [td.text for td in tr.find_all('td')]
        if row:
            rows.append(row)
    # write and save the information to a CSV file
    with open('crypto_info.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in rows:
            writer.writerow(row)


if __name__ == '__main__':
    main()
