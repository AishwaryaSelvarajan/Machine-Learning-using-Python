# Web Scraping - Amazon Product Review

import requests
from bs4 import BeautifulSoup

# The URL from which we are going to scrap the data
url = "https://www.amazon.in/Test-Exclusive-746/product-reviews/B07DJHXTLJ/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"
page = requests.get(url)
print('The response from the page is: ')
print(page)

# Get the contents of th epage using Beautiful Soup
soup = BeautifulSoup(page.content,'html.parser')
#print('The complete content of the page in html form is: ')
#print(soup.prettify())
 
# In the above URL we are going to scrap the review section of the product. The review contains name of the reviewer, 
# Date when the review is posted, title of the review and complete review.
# As this web page has enormous data it is difficult to manually look for the data we are in need of. 
# So to avoid this, in the web page from where the data is required, right click and select Inspect Element
# Now the relevant html code snippet will be shown selected in the new window opened. Using that tag and class name

# names_of_all_the_reviewers = soup.find_all('span',class_ = "a-profile-name")
# print('The names of all the reviewers that has been scraped from the web page is as follows: ')
# print(names_of_all_the_reviewers)

# The first two names will be repeated twicw, so to eliminate the first two redundant data, we have
names_of_all_the_reviewers = soup.find_all('span',class_ = "a-profile-name")[2:]
print('The names of all the reviewers that has been scraped from the web page is as follows: ')
print(names_of_all_the_reviewers)

# Now ignoring the span tag and taking only the names in a separate list
len_of_reviewer_list = len(names_of_all_the_reviewers)
print('The length of reviewer list is ' + str(len_of_reviewer_list))

new_reviewer_names = []
for i in range (0,len_of_reviewer_list):
    new_reviewer_names.append(names_of_all_the_reviewers[i].get_text())

print('The new list of reviewer names are: ')
print(new_reviewer_names)

# Print the star rating
star_rating =soup.find_all('span',class_="a-icon-alt")[3:]
print('The list of rating are: ')
print(star_rating)

cust_rating = [rating.get_text() for rating in star_rating]
print(cust_rating)

# Get the Review title ------------------ To be noted --------------------------------
list_title = soup.select('a.review-title span')
print('The title of the review are: ')
print(list_title)

cust_title = [title.get_text() for title in list_title]
print(cust_title)

# Review Date
list_date = soup.find_all('span',class_='review-date')[2:]
print('The review date is : ')
print(list_date)

cust_review_date = [rev_date.get_text() for rev_date in list_date]
print('The customer review date is')
print(cust_review_date)

# Whole review content
complete_review = soup.select('span.review-text-content span')
print('The list of complete review is: ')
print(complete_review)
print('The length of complete review '+str(len(complete_review)))

cust_review_content = [review.get_text() for review in complete_review]
print(cust_review_content)

# To make this into a neat data frame
import pandas as pd
review_df = pd.DataFrame()
review_df['Date'] = cust_review_date
review_df['Customer Name'] = new_reviewer_names
review_df['Title'] = cust_title
review_df['Ratings'] = cust_rating
review_df['Review'] = cust_review_content

print("The complete Dataframe is : ")
print(review_df)

# Converting this to csv format
review_df.to_csv('Amazon_reviews.csv')