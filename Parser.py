from selenium import webdriver
from bs4 import BeautifulSoup
import json

def copy_data(html, deck_stats):
    # Parse out key infromation.
    soup = BeautifulSoup(html, "html.parser")
    text_elements = soup.find_all('span')
    deck_name = text_elements[4].text
    if deck_name not in deck_stats:
        deck_stats[deck_name] = [{
                                      "Opponent":text_elements[6].text,
                                      "Games":text_elements[8].text,
                                      "Winrate":text_elements[10].text,
                                      "SDWinrate":text_elements[12].text,}]
    else:
        deck_stats[deck_name].append(
                                        {"Opponent":text_elements[6].text,
                                         "Games":text_elements[8].text,
                                         "Winrate":text_elements[10].text,
                                         "SDWinrate":text_elements[12].text,
                                        })


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
            x_offset = 2+23*i
            y_offset = 2+j*31
            act = webdriver.ActionChains(browser)
            act.move_to_element_with_offset(el,x_offset,y_offset)
            act.perform()
            try:
                html = browser.find_element_by_class_name("tab-ubertipTooltip").get_attribute('innerHTML')
            except:
                html = ""
            if html != "":
                copy_data(html, deck_stats)
    browser.close()
    return deck_stats

if __name__ == "__main__":
    deck_stats = scrape_table()
    with open('data.json', 'w') as fp:
        json.dump(deck_stats, fp, sort_keys=True, indent=4)



