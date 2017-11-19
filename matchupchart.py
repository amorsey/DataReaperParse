import matplotlib.pyplot as plt
import matplotlib.style as style
import matplotlib.patches as mpatches
import json
 
def find_max():
    with open('data.json', 'r') as f:
        matches = json.load(f)
    with open('occurence.json', 'r') as f:
        occurences = json.load(f)

    max_val = 0
    classes = ""
    for names in matches:
      oppnt = matches[names]
      for deck in oppnt:
        value = (float(deck["Winrate"])-0.50)*occurences[deck["Opponent"]]
        if value > max_val:
            max_val = value
            classes = names+deck["Opponent"]
    print(max_val)
    print(classes)


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
        elif area > -0.5:
            colors.append("#fd8674")
        elif area > -1:
            colors.append("#ef654d")
        elif area > -1.5:
            colors.append("#d74128")
        else:
            colors.append("#bd1100")

    my_y_labels = ["20","30","40","50","60","70","80"]
    y = [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]
    plt.yticks(y, my_y_labels)
    rects = plt.bar(start_points, hights, widths, alpha=0.9, align='edge', color=colors, edgecolor = "black")
    plt.title(deck_name+" Win/Loss Relevancy", fontsize=12)
    ax = plt.gca()
    ax.set_ylabel('Matchup Winrate [%]', fontsize=10)
    ax.set_xlabel('Deck Prevalence [out of 100%]', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=12)

    plt.ylim([-0.4,0.4])
    plt.xlim([-1,100])
    ax.grid('false')
    plt.axhline(y = 0, color = 'grey', linewidth = .5, alpha = .7)
    red_patch = mpatches.Patch(color='#4a8c1c', label='Very Good')
    grn_patch = mpatches.Patch(color='#a9da78', label='Good')
    prp_patch = mpatches.Patch(color='#bd1100', label='Very Bad')
    blu_patch = mpatches.Patch(color='#fd8674', label='Bad')
    plt.legend(bbox_to_anchor=(1.00, 0.1), ncol=2,handles=[grn_patch,red_patch,blu_patch,prp_patch],prop={'size': 7})
    count = 0
    last_hight = 0
    switch = True
    for rect in rects:
        height = rect.get_height()
        width = rect.get_width()
        if height > 0.25:
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                deck_names[count],
                ha='center', va='bottom',fontsize=7)
            switch = True
        elif height < 0:
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                deck_names[count]+"-",
                ha='center', va='top',rotation='vertical',fontsize=7)
        elif width < 2  and last_height >= height  and switch: 
            ax.text(rect.get_x() + rect.get_width()/2., 0,
                deck_names[count]+"-",
                ha='center', va='top',rotation='vertical',fontsize=7)
            switch = False
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                "-"+deck_names[count],
                ha='center', va='bottom',rotation='vertical',fontsize=7)
            switch = True
            
        count +=1
        last_height = height
        
    plt.tight_layout()
    plt.savefig(deck_name+".png")
    plt.clf()



#print(find_max())
with open('data.json', 'r') as f:
    matches = json.load(f)
for names in matches:
    #print(names)
    make_graph(names)







