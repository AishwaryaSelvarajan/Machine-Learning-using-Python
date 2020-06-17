# Web Scraping - Download  static web page
# To load the URL
import requests

# For Web Scraping
from bs4 import BeautifulSoup

# The URL from which the web page has to be scraped
url = "http://15.206.143.222/webscrap/demo1.html"

# Check whether the page has been successfully loaded
page = requests.get(url)
print("The response of the page is ")
print(page)

# Display the content of the page
print("The content of the pages are: ")
print(page.content)

# Using html.parser to extract from the html webpage
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

# To retrieve the target data, I have two ways
# Method 1 - Take all the children elements in the list and get the target element from the list
target_element = list(soup.children)[2]
print(target_element)


# Method 2
# # The second element of the above is somewhat close to the target
body = list(target_element.children)[3]
print(body)

# Drilling it further
p = list(body.children)[1]
print(p)

data = p.get_text()
print(data)

# Another Example

# The URL from which the web page has to be scraped
url2 = "http://15.206.143.222/webscrap/demo2.html"

# Check whether the page has been successfully loaded
page = requests.get(url2)
print("The response of the page is ")
print(page)

# Display the content of the page
print("The content of the pages are: ")
print(page.content)

# Using html.parser to extract from the html webpage
soup = BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

# How to get the data using <p> tag
req_data = soup.find_all('p')
print(req_data)

len_of_req_data = len(req_data)
print(len_of_req_data)

# The above will return the data in the list with <p> tag attached. To eliminate the <p> tag.
for i in range(0,3):
    print(req_data[i].get_text())

# Another Example

# The URL from which the web page has to be scraped
url3 = "http://15.206.143.222/webscrap/demo3.html"

# Check whether the page has been successfully loaded
page = requests.get(url3)
print("The response of the page is ")
print(page)

# Display the content of the page
print ("The content of the pages are: ")
print (page.content)

# Using html.parser to extract from the html webpage
soup = BeautifulSoup(page.content,'html.parser')
print (soup.prettify())

# To search a specific tag with the id name
data = soup.find_all('p' , id = 'first')
print (data)

# To search a tag inside a tag, example search a p tag inside a div tag
data = soup.select('div p') # Div is the parent tag, p is the child tag
print (data)

# From the above loc I may have many p tags, so I can mention either class name or id name to select a speciic tag from the result
data = soup.select('div p.first-item') # first_item followed by dot is the class name
print (data)

data = soup.select('div p#first') # first followed by hash is the id name
print  (data)