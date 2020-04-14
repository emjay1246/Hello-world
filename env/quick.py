import sys 
import requests
from bs4 import BeautifulSoup

import sys
import requests
import bs4
 
if len(sys.argv) == 3:
    # If arguments are satisfied store them in readable variables
    url = 'http://%s' % sys.argv[1]
    file_name = sys.argv[2]
 
    print('Grabbing the page...')
    # Get url from command line
    response = requests.get(url)
    response.raise_for_status()
 
    # Retrieve all links on the page
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('p')
 
    file = open(file_name, 'wb')
    print('Collecting the links...')
    for link in links:
        href = link.get('href') + '\n'
        file.write(href.encode())
    file.close()
    print('Saved to %s' % file_name)
else:
    print('Usage: ./collect_links.py wwww.example.com file.txt')