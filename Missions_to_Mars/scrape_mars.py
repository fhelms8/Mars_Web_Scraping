from bs4 import BeautifulSoup as bs
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pymongo
import os
import time 
import pandas as pd


def mars_scrape():

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Initialize PyMongo to work with MongoDBs
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

    # Define database and collection
    db = client.commerce_db
    collection = db.items

    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    time.sleep(2)



    # Create BeautifulSoup object; parse with 'lxml'
    soup = bs(browser.html, 'lxml')

    ## ------------------------------------------------------------## 

    #Find the columns that contain the title and paragraph texts
    results = soup.find_all('div', class_='list_text')
    # print(results)

    # Loop through returned results
    for result in results:
        
        # Retrieve the thread title
        title = result.find('div', class_='content_title')
        
        
        # Access the thread's text content
        title_text = title.text
    

        try:
            # Access the thread with CSS selectors
            thread = result.find('div', class_='article_teaser_body') 
            

            # The number of comments made in the thread
            teaser_body = thread.text.lstrip()
            
            # Run teaser_body & title 
            if (teaser_body):
                print('\n-----------------\n')
                print(title_text)
                print('Body:')
                print(teaser_body)
        except AttributeError as e:
            print(e)



    ## -------------------------------- ##
    ## JPL Mars Space IMages

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    time.sleep(2)

    soup = bs(browser.html, 'lxml')

    html = browser.html
    img_soup = soup(html, 'html.parser')

    

    #Find the row that contain the picture url
    header = soup.find_all('div', class_='header')
    header_image = soup.find('img', class_='headerimage fade-in').get('src')
    header_image

    featured_image_url = url + header_image
    print(featured_image_url)

    ## -------------------------------------##
    # Mars Facts

    # Give url variable name
    url = 'https://galaxyfacts-mars.com/'

    # Create table and merge into a df
    tables = pd.read_html(url)
    mars_table_df = tables[0]
    mars_table_df.columns = ["Description","Planet 1","Planet 2"]
    mars_table_df.set_index("Description", inplace=True)
    mars_table_df

    # Cover df into html 
    html_table = mars_table_df.to_html()
    html_table

    # Clean up
    clean_html = html_table.replace('\n', '')
    clean_html

    # Save file as html 
    mars_table_df.to_html('mars_table.html')
    print(clean_html)

    ## --------------------------- ## 
    ## Mars Hemispheres

    # Create dictionary to contain all planets img & title 
    planet_dict = []

    ## Cerberus 

    # url https://marshemispheres.com/
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(2)

    #Click on url link 
    browser.links.find_by_partial_text('Cerberus').click()


    html = browser.html
    soup = bs(html,"html.parser")
    # print(soup.prettify())

    #Pull the link that contains the full image 
    img_link = soup.find('img', class_='wide-image').get('src')

    #Pull Hemisphere title 
    cerberus_title = soup.find('h2', class_='title').text
    # print(cerberus_title)

    # Combine url & img link to make full html link=
    cerberus_img = url + img_link
    # print(cerberus_img)

    browser.back()
    #Create dictionaries to the img url and title 

    cerberus_dict = {'title': cerberus_title, 'img_url': cerberus_img}
    planet_dict.append(cerberus_dict)

    print(cerberus_dict)

    ## Schiaparelli

    # url https://marshemispheres.com/
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(2)

    #Click on url link 
    browser.links.find_by_partial_text('Schiaparelli').click()


    html = browser.html
    soup = bs(html,"html.parser")
    # print(soup.prettify())

    #Pull the link that contains the full image 
    img_link = soup.find('img', class_='wide-image').get('src')

    #Pull Hemisphere title 
    schiaparelli_title = soup.find('h2', class_='title').text
    # print(cerberus_title)

    # Combine url & img link to make full html link=
    schiaparelli_img = url + img_link
    # print(cerberus_img)

    browser.back()
    #Create dictionaries to the img url and title 

    schiaparelli_dict = {'title': schiaparelli_title, 'img_url': schiaparelli_img}
    planet_dict.append(schiaparelli_dict)

    print(schiaparelli_dict)

    ## Syrtis

    # url https://marshemispheres.com/
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(2)

    #Click on url link 
    browser.links.find_by_partial_text('Syrtis').click()


    html = browser.html
    soup = bs(html,"html.parser")
    # print(soup.prettify())

    #Pull the link that contains the full image 
    img_link = soup.find('img', class_='wide-image').get('src')

    #Pull Hemisphere title 
    syrtis_title = soup.find('h2', class_='title').text
    # print(cerberus_title)

    # Combine url & img link to make full html link=
    syrtis_img = url + img_link
    # print(cerberus_img)

    browser.back()
    #Create dictionaries to the img url and title 

    syrtis_dict = {'title': syrtis_title, 'img_url': syrtis_img}
    planet_dict.append(syrtis_dict)

    print(syrtis_dict)

    ## Valles Marineris

    # url https://marshemispheres.com/
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    time.sleep(2)

    #Click on url link 
    browser.links.find_by_partial_text('Valles Marineris').click()


    html = browser.html
    soup = bs(html,"html.parser")
    # print(soup.prettify())

    #Pull the link that contains the full image 
    img_link = soup.find('img', class_='wide-image').get('src')

    #Pull Hemisphere title 
    valles_title = soup.find('h2', class_='title').text
    # print(cerberus_title)

    # Combine url & img link to make full html link=
    valles_img = url + img_link
    # print(cerberus_img)

    browser.back()
    #Create dictionaries to the img url and title 

    valles_dict = {'title': valles_title, 'img_url': valles_img}
    planet_dict.append(valles_dict)

    print(valles_dict)

    print(planet_dict)

    mars_scrape = {
        "news_title": title_text,
        "news_p": teaser_body,
        "featured_img_url": featured_image_url,
        "mars_table": clean_html,
        "hempisphere_img_urls": planet_dict
        }

    browser.quit()

    return mars_scrape

if __name__ == "__main__":
    results = mars_scrape()
    print("results")
    print(results) 
