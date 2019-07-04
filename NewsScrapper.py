#!/usr/bin/env python
# coding: utf-8

# In[141]:


from bs4 import BeautifulSoup
import requests

interestURL = "https://www.rediff.com/news"
newreq = requests.get(interestURL)
c = newreq.content
soup = BeautifulSoup(c, 'html.parser')

data = soup.find_all('ul' , {'class':'navbarul'})[0].find_all("li")
interests = []
for link in data:
    interests.append(link.text.replace(" ",""))

again = 'Y'
while again == 'Y':
    interest = input("Enter Your Interest: ")
    if interest in interests:
        pass
    else:
        print("Please Enter a Valid Interest!\nYou can choose among\n")
        for item in interests:
            print(item)
        again = input("Do you want to enter interest again? (Y or N)")
        if again == 'Y' or 'y':
            continue
        else:
            break

    base_url = "https://www.rediff.com/"

    headline = []
    res = requests.get(base_url + interest.lower())
    soup = BeautifulSoup(res.content, 'html.parser')
    all = soup.find_all('div', {'class' : 'newleftcontainer'})[0].find_all('div', {'class' : 'nbox'})
    for news in all:
        headline.append(news.text)
    for h in headline:
        print("* " + h)
    again = input("\n\nDo you want to Search Again? (Y or N)")