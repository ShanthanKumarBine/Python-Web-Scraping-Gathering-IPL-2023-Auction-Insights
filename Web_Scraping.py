#!/usr/bin/env python
# coding: utf-8

# In[56]:


# pip install beautifulsoup4


# In[57]:


# This package is a Python library that is commonly used for web scraping tasks. Web scraping involves extracting data from websites by parsing the HTML structure of web pages.


# In[58]:


# pip install requests


# In[59]:


# This is a popular Python library used for making HTTP requests. It provides a simple and convenient way to send HTTP requests and handle responses in your Python code.


# In[5]:


import numpy as np 

import pandas as pd 


# In[6]:


# Importing Numpy and pandas for data manipulation and analysis.


# In[60]:


import requests

from bs4 import BeautifulSoup


# In[8]:


# Importing requests and beautiful soup for web scraping.


# In[9]:


url ="https://www.scrapethissite.com/pages/simple/"
req = requests.get(url)
print(req)


# In[10]:


soup=BeautifulSoup(req.text,"lxml")

print(soup)


# In[11]:


# This code is used to create a BeautifulSoup object, which is a Python library for parsing HTML or XML documents. 


# In[12]:


container1 = soup.find("div", id="page")


# In[13]:


# This code uses BeautifulSoup to find a <div> element with the id attribute equal to "page". The soup.find() function searches the BeautifulSoup object, soup, for the specified HTML element.


# In[14]:


container2 = container1.find('div', class_='container')


# In[15]:


# In the code, BeautifulSoup to find a <div> element with the class attribute equal to "container" within the container1 variable.


# In[16]:


container3 = container2.find('p',class_="lead").get_text()


# In[17]:


# In this code, BeautifulSoup to find a <p> element with the class attribute equal to "lead" within the container2 variable. Then,extracting the text content of that element using the get_text() method.


# In[18]:


data_title=container3


# In[19]:


print(data_title)


# In[20]:


# Open the file in write mode

with open('data_title.txt', 'w') as file:
    
    file.write(data_title)
    
        # Write the data_title to the file


# In[21]:


countrys = soup.find_all('div', class_='col-md-4 country')

data = []

for country in countrys:
    # country name
    country_name = country.find('h3', class_='country-name').text.strip()
    
    # capital
    capital = country.find('span', class_='country-capital').text
    
    # population
    population = country.find('span', class_='country-population').text
    
    # area
    area = country.find('span', class_='country-area').text
    
    # Append the extracted data as a list to the main data list
    data.append([country_name, capital, population, area])

print(data)


# In[22]:


# This code extracts data from the HTML elements using BeautifulSoup and storing it in the data lists. When this code is run, it will find all div elements with the class name 'col-md-4 country' in the soup_object, which contains the HTML content i need for scraping. For each country element found, the code extracts the country name, capital, population, and area by using appropriate find() and text methods. It then inserts the extracted data as a list [country_name, capital, population, area] to the data list. Finally, the code prints the data list, which will display the extracted information for each country.


# In[23]:


Country_df = pd.DataFrame(data)


# In[24]:


# In this code i am converting List to dataframe using pandas. data to country_dataframe .


# In[25]:


Country_df.head(5)


# In[26]:


# checking the dataframe and looking at first 5 elements in it .


# In[27]:


column_names = ['country','capital','population','Area(km2)']
Country_df.columns = column_names


# In[28]:


# In this code i am changing the colomns names of the df . From default to the actual names of the colomns for better understanding of the data.


# In[29]:


Country_df


# In[30]:


# verifying the df


# In[31]:


Country_df.to_csv("Countries of the World.csv")


# In[32]:


# converting the dataframe to csv file. The DataFrame will be saved as a CSV file in the current directory with the specified name.


# In[33]:


# End of first web scraping


# In[ ]:





# In[34]:


# Ipl Auction 2023 Web scraping


# In[35]:


url ="https://www.iplt20.com/auction/2023"
req = requests.get(url)
print(req)


# In[36]:


soup=BeautifulSoup(req.text,"lxml")
print(soup)


# In[37]:


# This code is used to create a BeautifulSoup object, which is a Python library for parsing HTML or XML documents. 


# In[38]:


table = soup.find("table",class_="ih-td-tab auction-tbl")
print(table)


# In[39]:


# This is used to search for an HTML table element within the parsed BeautifulSoup object. It seaches for table elements and retrieves the table.


# In[40]:


title = table.find_all("th")
print(title)


# In[41]:


# This code is used find all the table elements.


# In[42]:


header = []
for i in title:
    name = i.text
    header.append(name)
print(header)


# In[43]:


# This code is a loop to iterate over the elements in the title list, which contains table header elements. The loop extracts the text content of each header element using the .text attribute and appends it to the header list.


# In[44]:


Ipl_df=pd.DataFrame(columns=header)


# In[45]:


# here we create a new dataframe and assign coloumns to headers


# In[46]:


Ipl_df


# In[47]:


# print our df here to check.


# In[48]:


row = table.find_all("tr") 
print(row)


# In[49]:


for i in row[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row_data = [tr.text for tr in data]
    row_data.insert(0, first_td)
    Ipl_df.loc[len(Ipl_df)] = row_data


# In[50]:


# In this code , loop is used to iterate over elements in the row list, excluding the first element. The loop extracts specific data from each row, creates a list of row data, inserts a value at the beginning of the row, and then inserts the row data to the Ipl_df DataFrame.


# In[51]:


print(Ipl_df)


# In[52]:


# This is ipl 2023 auction data 


# In[53]:


Ipl_df.to_csv("Ipl Auction 2023.csv")


# In[54]:


df1 = pd.read_csv('Ipl Auction 2023.csv')


# In[55]:


df1.head(2)


# In[ ]:


# Thank you

