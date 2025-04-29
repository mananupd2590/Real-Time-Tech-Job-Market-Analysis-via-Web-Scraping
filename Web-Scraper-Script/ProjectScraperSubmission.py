# %% [markdown]
# ### Imports

# %%
from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
from multiprocessing import Process
import csv
import pandas as pd
import datetime

# %% [markdown]
# #### URL Formation

# %%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

locations = []
query = []
pageSize = 20
radiusInMiles = 100
filterSponsorship = True
postedDate = 'SEVEN'

with open('location.txt', 'r') as file:
    for line in file:
        locations.append(line.strip()) 

with open('q.txt', 'r') as file:
    for line in file:
        query.append(line.strip())

with open('pageSize.txt', 'r') as file:
    for line in file:
        pageSize = int(line.strip())
        if pageSize in [10, 20, 50, 100]:
            print(f"Page size {pageSize} is correct.")
        else:
            print("Get a correct page size")
    
with open('radiusMiles.txt', 'r') as file:
    for line in file:
        radiusInMiles = int(line.strip())
        if radiusInMiles < 101:
            print(f"Radius {radiusInMiles} is correct.")
        else:
            print("Get a correct Radius")

with open('sponsorship.txt', 'r') as file:
    for line in file:
        filterSponsorship = line.strip()

with open('postedDate.txt', 'r') as file:
    for line in file:
        postedDate = line.strip()

URLS_dict = {}
baseurl = "https://www.dice.com/jobs?"

for job in query:
    for location in locations:
        # Initialize URL list for the location
        keys_value = ''
        keys_value = location +'||'+job
        keys_value = keys_value.replace("%20", " ")
        print(keys_value)
        URLS_dict[keys_value] = []
        for page in range(1, 2): 
            url = f"{baseurl}q={job}&location={location}&page={page}&pageSize={pageSize}&radius={radiusInMiles}&radiusUnit=mi&filters.willingToSponsor={filterSponsorship}"
            print(url)
            URLS_dict[keys_value].append(url)

# Print the total number of URLs for each location
for keys_value, urls in URLS_dict.items():
    print(f"Location: {keys_value}, Total URLs: {len(urls)}")


# %%
from datetime import datetime, timedelta

def estimate_posted_date(time_elapsed):
    # print(time_elapsed)
    if time_elapsed.startswith('Posted'):
        time_elapsed = time_elapsed[7:]
        # print(time_elapsed)

    if 'ago' in time_elapsed:
        time_elapsed = time_elapsed[:-3]
        # print(time_elapsed)
        
    number, unit = time_elapsed.split()
    if(number.endswith('+')):
        number = int(number[:-1])
    else:
        number = int(number)

    unit_multipliers = {
        'minute': 1,
        'hour': 60,
        'day': 24 * 60,
        'week': 7 * 24 * 60,
        'month': 30 * 24 * 60
    }

    if unit.endswith('s'):
        unit = unit[:-1]  # Remove plural 's'
    if unit in unit_multipliers:
        delta_minutes = number * unit_multipliers[unit]
    else:
        return ValueError("Invalid time unit")

    estimated_date = datetime.now() - timedelta(minutes=delta_minutes)

    return estimated_date

# time_elapsed = "60+ months ago"
# time_elapsed = "17 days ago"
# Posted 17 days 
# estimated_date = estimate_posted_date(time_elapsed)
# print("Estimated posted date:", estimated_date.strftime("%Y-%m-%d %H:%M:%S"))


# %%

def scrape_dice_jobs(soup,location):
    employment_types = []
    job_titles = []
    posted_dates = []
    posted_on = []
    updated_dates = []
    updated_on = []
    job_descriptions = []
    company_links = []
    company_names = []
    total_job_count = []
    location_df = []
    query_df = []

    job_cards = soup.find_all('dhi-search-card', {'class': 'ng-star-inserted'})
    location_value , query_value = location.split("||")
    for card in job_cards:
        #Employment Type
        employment_type = card.find('span', {'data-cy': 'search-result-employment-type'})
        if employment_type:
            employment_type = employment_type.text.strip()
        else:
            employment_type = ''
        
        #Job Title
        job_title_elem = card.find('a', class_='card-title-link normal')
        if job_title_elem:
            job_title = job_title_elem.text.strip()
        else:
            job_title = ''

        # Posted Date
        posted_date_elem = card.find('span', class_='posted-date')
        if posted_date_elem:
            posted_date:str = posted_date_elem.text.lstrip('Posted ')
            posted_date = posted_date.rstrip('ago')
        else:
            posted_date = ''

        if posted_date!= '':
            posten_on_date = estimate_posted_date(posted_date)
        else:
            posten_on_date = ''

        # Updated Date
        updated_date_elem = card.find('span', {'data-cy': 'card-modified-date'})
        if updated_date_elem:
            updated_date = updated_date_elem.text.lstrip('- Updated ')
            updated_date = updated_date.rstrip('ago')
        else:
            updated_date = ''
        
        #Job Desc
        job_description_elem = card.find('div', class_='card-description')
        if job_description_elem:
            job_description = job_description_elem.text.strip()
        else:
            job_description = ''

        #Company Link
        company_link_elem = card.find('a', class_='ng-star-inserted')
        if company_link_elem:
            company_link = company_link_elem['href']
        else:
            company_link = ''
        
        #Company Name
        company_name = company_link_elem.text.strip() if company_link_elem else ''

        job_count = soup.find('span', attrs={'id':'totalJobCount','data-cy': 'search-count'})
        # print("Job Count")
        # print(job_count.text)
            
        employment_types.append(employment_type)
        job_titles.append(job_title)
        posted_dates.append(posted_date)
        posted_on.append(posten_on_date)
        updated_dates.append(updated_date)
        job_descriptions.append(job_description)
        company_links.append(company_link)
        company_names.append(company_name)
        total_job_count.append(job_count.text)      
        location_df.append(location_value)
        query_df.append(query_value)
    # print("Length of employment_types:", len(employment_types))
    # print("Length of job_titles:", len(job_titles))
    # print("Length of posted_dates:", len(posted_dates))
    # print("Length of posted_on:", len(posted_on))
    # print("Length of updated_dates:", len(updated_dates))
    # print("Length of job_descriptions:", len(job_descriptions))
    # print("Length of company_links:", len(company_links))
    # print("Length of company_names:", len(company_names))
    # print("Length of total_job_count:", len(total_job_count))
    # print("Length of location_df:", len(location_df))
    # print("Length of query_df:", len(query_df))
    data = {
        'Job Title': job_titles,
        'Company Name': company_names,
        'Job Description': job_descriptions,
        'Location': location_df,
        'Employment Type': employment_types,
        'Query_Value': query_df,
        'Posted Scraped': posted_dates,
        'Posted On': posted_on,
        'Updated Scraped': updated_dates,
        'Updated On': updated_on,
        'Company Link': company_links,
        'From Total Job Count': total_job_count
    }
    df = pd.DataFrame.from_dict(data=data, orient='index')
    df = df.transpose()
    return df


# %% [markdown]
# ## Main function

# %%

for location, urls in URLS_dict.items():
    concatenated_df = pd.DataFrame()
    print(location)
    location=location.replace("%20", " ")
    for url in urls:
        print(url)
        driver = webdriver.Chrome()
        driver.get(url)
        time.sleep(10)
        page_source = driver.page_source
        driver.quit()
        soup = BeautifulSoup(page_source, 'html.parser')
        df = scrape_dice_jobs(soup, location)
        print("Concatenated:")
        print(df.shape)
        concatenated_df = pd.concat([concatenated_df, df])

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f'dice_jobs_{location}_{timestamp}.csv'
    print("Output File:")
    print(filename)
    print("File Shape:",concatenated_df.shape)

    concatenated_df.to_csv(filename, index=False, mode='w')


