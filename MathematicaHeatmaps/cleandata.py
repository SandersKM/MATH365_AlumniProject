# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def open_data(filename):
    file = open(filename)
    data = file.readlines()
    file.close()
    return data
    
def main():
    biodata = open_data("C:/Users/kates/Desktop/MATH365_BIO.csv")
    eventdata = open_data("C:/Users/kates/Desktop/MATH365_EVENT.csv")
    giftdata = open_data("C:/Users/kates/Desktop/MATH365_GIFT.csv")
    #clean_biodata = open("C:/Users/kates/Desktop/MATH365_BIO_ZIP.csv", "w")
    #clean_alumni = open("C:/Users/kates/Desktop/MATH365_BIO_ZIP_YEAR_EVENTS_DONATIONS.csv", "w")
    #clean_alumni.write("ID,ZIP,GRAD_YEAR,TOTAL_EVENTS,TOTAL_DONATIONS\n")
    alumni_dict = get_gift_amount(giftdata,get_event_num(eventdata,get_bio_locations(biodata)))
    zip_population(alumni_dict)
    #write_csv(clean_alumni, alumni_dict)
    #clean_alumni.close()
    #clean_biodata.close()
    return alumni_dict

def get_bio_locations(data):
    locations = {}
    for line in data[1:]:
        split_line = line.split(",")
        #Check if Alumni and have a zip code in continental us
        if split_line[9].isdigit() and split_line[10]=="Alumni":
            if len(split_line[9])>= 5 and not(
                    int(split_line[9]) >= 99500 or (
                            int(split_line[9]) < 96900 and int(split_line[9]) >=96700)):
                #if split_line[9][0] == "9":
                alumn = int(split_line[0])
                zipcode = split_line[9]
                classyear = split_line[25]
                locations[alumn] = []
                #add Zip Code
                locations[alumn].append(zipcode)
                #add Class Year
                if classyear.isdigit():
                    locations[alumn].append(int(classyear))
                else:
                    locations[alumn].append(0)
                #add zero for event num and donations num
                locations[alumn].append(0)
                locations[alumn].append(0)
    return locations

#takes event data and alumni dict
def get_event_num(data,alumni):
    for event in data[1:]:
        info = event.split(",")
        alumn = int(info[0])
        if alumn in alumni:
            alumni[alumn][2] += 1
    return alumni

def get_gift_amount(data, alumni):
    for gift in data[1:]:
        info = gift.split(",")
        alumn = int(info[0])
        if alumn in alumni:
            alumni[alumn][3] += get_amount(info[3])
    return alumni

def get_amount(money):
    amount = ""
    for m in money:
        if m.isdigit() or m == ".":
            amount += m
    return float(amount)

def write_csv(file, dic):
    for k in dic:
        file.write(str(k))
        for i in dic[k]:
            file.write(",")
            file.write(str(i))
        file.write("\n")
        
def zip_population(alumni):
    zip_dict = {}
    for alum in alumni:
        if alumni[alum][0] not in zip_dict:
            zip_dict[alumni[alum][0]] = 0
        zip_dict[alumni[alum][0]] += 1
    mathmatica = "GeoRegionValuePlot[{"
    for z in zip_dict:
        mathmatica += 'Entity["ZIPCode", "'+str(z)+'"] -> '+ str(zip_dict[z])+', '
    mathmatica += '}]'
    print(mathmatica)
    p = open("C:/Users/kates/Desktop/mathematicainput.txt", "w")
    p.write(mathmatica)
        
      
loc = main()
#print(loc)
