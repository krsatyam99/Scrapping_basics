#################################### Web scrapping basic commands #########################################

# Requiremnts:
 #1. pip install requests :- This will give us the content from the internet 
 #2 pip install html5lip :
 #3. pip install bs4 :

import requests
from bs4 import BeautifulSoup
import html5lib



## Making a GET request 
url ="https://www.geeksforgeeks.org/python-programming-language/"
url = "https://www.codewithharry.com"

r = requests.get(url)
html_content = r.content
# print( html_content)
## Parsing the HTML
soup = BeautifulSoup(html_content,'html.parser')
# print(soup.prettify)

# Get all the titles of the html page 
title =soup.title


### commonly used types of objects 
# 1.Tag
# 2.Navigable Tag
# 3.BeautifulSoup
# 4. comment 

# print(type(soup))  #output <class 'bs4.BeautifulSoup'>
# print(type(title)) #output <class 'bs4.element.Tag'>
# print(type(title.string)) #output  <class 'bs4.element.NavigableString'>


# Get all the paragraphs  of the html page 
paragraph = soup.find_all("p")
# print(paragraph)


# Get all the anchor   of the html page 
Anchor_tags = soup.find_all("a")
 ## getting all the links in clickable form 
link_set=set()
for link in Anchor_tags:
    if (link.get("href") != "#"):
        clickable_link ="https://www.your_base_url.com" + link.get("href")
        link_set.add(clickable_link)
# print(link_set,"my links ")
# print("clickable",clickable_link)



# print(Anchor_tags)



# Get Classes or Id of any any element 
 ## note* If any of the class or id is not present it will throw key error.
# class_of_paragraphs = soup.find("body")["header-sidebar__list-item"]
# print(class_of_paragraphs)

# id_of_paragraphs = soup.find("p")["id"]  #### so if we want to print any specific class of id data we just have to pass in the written format .



#print(soup.find('p').get_text()) #get text without any html tags 
#print(soup.get_text()) # writing this will give us text without tag for the whole html page.



# differnce between .contents and .children
# navbarSupportedContent =soup.find(id="navbarSupportedContent")
# for elem in navbarSupportedContent.contents:
#     print(elem,"elements")

       ## .contents = Returns a list which need some memory 
       ## .children = Return a generator  , no memory usage 



# If you want to get the parent of any tag you just have to use 

## .parent for just above parent 
## .parents all the parents



# If you want to get siblings easy word previous line tag we will use .previoussiblings  and for next line we will use .nextsibling
## note ** Previous and next siblings also read br tags and spaces  so for getting the previous working tag You have
#  to use .previous / .next siblings multiple times as per requiremnts


#print(soup.select("#loginModal")) # by  using css class
#print(soup.select(".loginModal")) # by  using css id

