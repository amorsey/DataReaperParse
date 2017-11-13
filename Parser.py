from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

def copy_data(dictionary):
    try:
        # Find and extract HTML from popup window.
        html = browser.find_element_by_class_name("tab-ubertipTooltip")\
        .get_attribute('innerHTML')
        # Parse out lines with key infromation.
        soup = BeautifulSoup(html, "html.parser")
        spanElements = soup.find_all('span')


        
    except:
        pass

def scrape_table():
    browser = webdriver.Firefox() 
    url = ("https://public.tableau.com/views/DataReaper69-MatchupWinRat"
           "es/Dashboard1?:embed=y&:showVizHome=no&:host_url=https%3A%2"
           "F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:t"
           "oolbar=yes&:animate_transition=yes&:display_static_image=no"
           "&:display_spinner=no&:display_overlay=yes&:display_count=ye"
           "s&publish=yes&:loadOrderID=0")
    browser.get(url)
    f = open('Data.txt', 'w')
    el = browser.find_element_by_class_name("tvScrollContainer")
    browser.execute_script("window.scrollTo(0, 160);")
    classMatchup = {}
    for j in range(22):
        for i in range(21):
            act = webdriver.ActionChains(browser)
            act.move_to_element_with_offset(el,2+23*i,2+j*31)
            act.perform()
            copyData(classMatchup)
    f.close()
    browser.close()


if __name__ == "__main__":
    scrapeTable()



