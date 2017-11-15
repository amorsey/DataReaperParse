import matplotlib.pyplot as plt
import matplotlib.style as style
import json
 
def find_max():
    with open('data.json', 'r') as f:
        matches = json.load(f)
    with open('occurence.json', 'r') as f:
        occurences = json.load(f)

    max = 0
    for deck in matches:
        


def make_graph(deck_name):
    with open('data.json', 'r') as f:
        datastore = json.load(f)
    with open('occurence.json', 'r') as f:
        data_occ = json.load(f)

    deck_names = []
    occurence = []
    winrates = []


    matchup_list = datastore[deck_name]
    for deck in matchup_list:
        name = deck['Opponent']
        occurence.append(data_occ[name])
        deck_names.append(name)
        winrates.append(float(deck['Winrate']))

    style.use('fivethirtyeight')
    hights = []
    colors = []
    start_points = []
    x_points = []
    widths = occurence
    for ele in winrates:
        amount = ele-0.5000
        hights.append(amount)
    total = 0
    for ele in occurence:
        start_points.append(total)
        total = total + ele
    for i in range(len(start_points)):
        x_points.append(widths[i]/2 + start_points[i])
    for i in range(len(hights)):
        area = hights[i]*widths[i]
        if area > 1.5:
            colors.append("#4a8c1c")
        elif area > 1:
            colors.append("#64a550")
        elif area > 0.5:
            colors.append("#82c162")
        elif area > 0:
            colors.append("#a9da78")
        elif area > -.5:
            colors.append("#fd8674")
        elif area > -1:
            colors.append("#ef654d")
        elif area > -1.5:
            colors.append("#d74128")
        else:
            colors.append("#bd1100")



    plt.xticks(x_points, deck_names, rotation='vertical')
    plt.bar(start_points, hights, widths, alpha=0.9, align='edge', color=colors, edgecolor = "black")
    plt.title(deck_name)
    ax = plt.gca()
    plt.ylim([-0.3,0.3])
    ax.grid('false')
    plt.axhline(y = 0, color = 'grey', linewidth = .5, alpha = .7)
    plt.tick_params(axis = 'x', which = 'major', labelsize = 8, tick1On='True')
    plt.tight_layout()
    plt.show()



make_graph("Big Druid")
