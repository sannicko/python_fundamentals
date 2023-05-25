import requests
from bs4 import BeautifulSoup

# specify the URL of the web page to be scraped
url = 'https://ikapestore.com/'

# send a GET request to the URL and store the response in a variable
response = requests.get(url)

# use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# find all the hyperlinks on the page
links = soup.find_all('a')

# print the text and URL of each link
for link in links:
    print(link.text)
    print(link['href'])

# open a file in write mode
with open('links_test.txt', 'w') as f:
    # loop through the links and write each one to the file
    for link in links:
        f.write(link.text + '\n')
        f.write(link['href'] + '\n')
        
# print a message to confirm that the links have been saved
print('Links saved to file.')