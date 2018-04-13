# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 13:02:40 2018

@author: kates
"""
import zipcode


def open_data(filename):
    file = open(filename)
    data = file.readlines()
    file.close()
    return data
    
def main():
    output = "GeoRegionValuePlot[{"
    biodata = open_data("C:/Users/kates/Desktop/MATH365_BIO.csv")
    states =  {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'}
    zipdict = {}
    popdict = {}
    stateszipdict ={}
    biodata = open_data("C:/Users/kates/Desktop/MATH365_BIO.csv")
    for s in states:
        popdict[s] = 0
        stateszipdict[s] = {}
    for line in biodata[1:]:
        split_line = line.split(",")
        #Check if Alumni and have a zip code in continental us
        if split_line[10]=="Alumni" and len(split_line[9]) == 5 and split_line[9].isdigit():
            if split_line[9] not in zipdict:
                zipdict[split_line[9]] = 0
            zipdict[split_line[9]] += 1
    for z in zipdict:
        zipstate = zipcode.isequal(z)
        if zipstate!= None and zipstate.state in states:
            popdict[zipstate.state] += zipdict[z]
            stateszipdict[zipstate.state][z] = zipdict[z]
# for plotting heat map by state
#    for s in states:
#        output+= 'Entity["AdministrativeDivision","'+states[s]+'"] ->' + str(
#                popdict[s]) + ','

#for plotting heat map of zips in individual states
    for s in stateszipdict["AR"]:
        
        output+= 'Entity["ZIPCode", "'+ str(s) + '"] ->'+str(stateszipdict["AR"][s])+','
    output += "}]"
    print(output)
            
main()       