from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

def copyData():
    try:
        html = browser.find_element_by_class_name("tab-ubertipTooltip").get_attribute('innerHTML')
        soup = BeautifulSoup(html, "html.parser")
        l = soup.find_all('span')
        for i in range(3,12,2):
            f.write(l[i].text + l[i+1].text + "\n")
        f.write("\n")
    except:
        pass



browser = webdriver.Firefox() 
url = "https://public.tableau.com/views/DataReaper69-MatchupWinRates/Dashboard1?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:toolbar=yes&:animate_transition=yes&:display_static_image=no&:display_spinner=no&:display_overlay=yes&:display_count=yes&publish=yes&:loadOrderID=0"
browser.get(url)
f = open('Data.txt', 'w')

el = browser.find_element_by_class_name("tvScrollContainer")
browser.execute_script("window.scrollTo(0, 160);")

for j in range(22):
    for i in range(21):
        act = webdriver.ActionChains(browser)
        act.move_to_element_with_offset(el,2+23*i,2+j*31)
        act.perform()
        copyData()




# Close everything
f.close()
browser.close()

