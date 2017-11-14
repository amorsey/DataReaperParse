from selenium import webdriver
from bs4 import BeautifulSoup

def copy_data(deck_stats):
    # Although a hack, try/except seems to be the best way to deal with
    # empty cells that create no pop-up.
    try:
        # Find and extract HTML from popup window.
        html = browser.find_element_by_class_name("tab-ubertipTooltip")\
        .get_attribute('innerHTML')
        # Parse out key infromation.
        soup = BeautifulSoup(html, "html.parser")
        text_elements = soup.find_all('span')
        deck_stats[text_elements[2]] = {text_elements[3]:{
                                        "Games":text_elements[5]
                                        "Winrate":text_elements[7],
                                        "SDWinrate":text_elements[9],}}
    except:
        pass

def scrape_table():
    url = ("https://public.tableau.com/views/DataReaper69-MatchupWinRat"
           "es/Dashboard1?:embed=y&:showVizHome=no&:host_url=https%3A%2"
           "F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:t"
           "oolbar=yes&:animate_transition=yes&:display_static_image=no"
           "&:display_spinner=no&:display_overlay=yes&:display_count=ye"
           "s&publish=yes&:loadOrderID=0")
    browser = webdriver.Firefox()
    browser.get(url)
    # The browser needs to scroll down to see the whole table.
    # This issue will vary dependent on your screen.
    el = browser.find_element_by_class_name("tvScrollContainer")
    browser.execute_script("window.scrollTo(0, 160);")
    deck_stats = {}
    for j in range(22):
        for i in range(21):
            # It is importnat to create a new ActionChains for every
            # operation otherwise each new iteration will perform ALL
            # previous commands.
            act = webdriver.ActionChains(browser)
            act.move_to_element_with_offset(el,2+23*i,2+j*31)
            act.perform()
            copyData(deck_stats)
    browser.close()
    return deck_stats

if __name__ == "__main__":
    deck_stats = scrape_table()
    # Add write operation.



