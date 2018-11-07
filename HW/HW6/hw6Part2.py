"""
Minghao Zhu hw6 part2 11/6/2018
This program starts by doing import textwrap, and reading in a file.
A loop that keep going until it gets the command of stop.
Inside the loop, print all relevant info base on requirement.
"""
import textwrap

def removeblank(title):
    """
    A function to remove blank
    """
    title_remove = title.split(" ")
    return title_remove[0]

while True:#A loop that keep going until it gets the command of stop.
    title = input("Enter a title (stop to end) => ")
    print(title)
    if title == "stop":  
        break
    else:
        print("")
        #deal with format of the title
        title = removeblank(title)
        title = title.lower()
        beasts_dict = dict()
        title_dict = dict()
        #read in files
        for lines in open("titles.txt"):
            line = lines.strip("\n")
            line = line.split("|")
            title_1 = line[0].lower().split(" ")
            title_set = set()
            #put titles in title_set
            for j in range(len(title_1)):
                title_set.add(title_1[j])
            title_dict[line[0]] = title_set
            beasts_set = set()
            #put beasts in beasts_set
            for i in range (1,len(line)):
                beasts_set.add(line[i])
            beasts_set = sorted(beasts_set)
            beasts_dict[line[0]] = beasts_set
        #find title
        find_title = set()
        for titles in title_dict:
            if title in title_dict[titles]:
                find_title.add(titles)
        find_title = sorted(find_title)
        if(find_title == []):
            print("This title is not found!\n")
        else:
            #print if find titles
            print("Found the following title: " + find_title[0])
            all_beasts = "Beasts in this title: " + str(beasts_dict[find_title[0]][0])
            #use textwrap to break in lines
            for j in range(1, len(beasts_dict[find_title[0]])):
                all_beasts = all_beasts+", "+ str(beasts_dict[find_title[0]][j])   
            all_break_beasts = textwrap.wrap(all_beasts)
            for line in all_break_beasts:
                print(line)
            print("")
            #put beasts in set
            title_beasts_set = set(beasts_dict[find_title[0]])
            find_more_title = set()
            #find titles containing beasts in common
            for b_sets in beasts_dict:
                inter_set = set()
                inter_set = set(beasts_dict[b_sets]).intersection(title_beasts_set)
                if (not(b_sets == find_title[0]))and(len(inter_set) > 0):
                    find_more_title = set(find_more_title)
                    find_more_title.add(b_sets)
                find_more_title = sorted(find_more_title)
            #print titles in common
            find_more_title_1 = "Other titles containing beasts in common: " + \
                str(find_more_title[0])
            #use textwrap to break in lines
            for i in range(1, len(find_more_title)):
                find_more_title_1 = find_more_title_1 + ", " + str(find_more_title[i])
            break_find_more_title = textwrap.wrap(find_more_title_1)
            for line in break_find_more_title:
                print(line)
            print("")    
            #find Beasts appearing only in this title
            only_set = set(title_beasts_set)
            for b_sets in beasts_dict:
                if not(b_sets == find_title[0]):
                    only_set = only_set.difference(beasts_dict[b_sets])
            #print Beasts appearing only in this title
            only_set = sorted(only_set)
            if(only_set == []):
                print("Beasts appearing only in this title:")
                print("")
            else:
                print_line = "Beasts appearing only in this title: "+ str(only_set[0])
                for i in range(1,len(only_set)):
                    print_line = print_line + ", " + str(only_set[i])
                #use textwrap to break in lines
                break_line = textwrap.wrap(print_line)
                for line in break_line:
                    print(line)
                print("")