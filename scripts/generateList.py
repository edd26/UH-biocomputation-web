from random import shuffle, permutate

core_staff = ["Na Helian", "Shabnam Kadir", "Rod Adams", "Rene te Boekhorst", , "Volker Steuber"]
research_fellows = ["Mohammad Tayarani-Najaran", "Reinoud Maex", "Yi Sun", "Damien Drix", "Ritesh Kumar"]
active_students = ["Yaqoob Muhammad", "Emil Dmitruk  ", "Ohki Katakura", "Rebecca Miko", "Nathan Beka", "Ankur Sinha", "Deepak Panday", "Sam Sutton"]
# -Julia Goncharenko
unknown_status= ["Ronak Bhavsar", "Udeshika Dissanayake", "Edward Wakelam", "Marco Craveiro"]


everyone_list = core_staff + research_fellows + active_students
non_core_list = research_fellows+ active_students

def shuffle_list_twice(new_list):
    print ("Original list : ",  new_list)
    shuffle(new_list)
    print ("List after first shuffle  : ",  new_list)

    shuffle(new_list)
    print ("List after second shuffle  : ",  new_list)

shuffle_list_twice(everyone_list)

shuffle_list_twice(non_core_list)