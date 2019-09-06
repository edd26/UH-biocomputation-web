from random import shuffle

core_staff = ["Na Helian", "Shabnam Kadir", "Rod Adams", "Rene te Boekhorst ?", "David Bowes", "Neil Davey", "Chrystopher Nehaniv", "Maria Schilstra", "Michael Schmuker", "Volker Steuber"]
research_fellows = ["Mohammad Tayarani-Najaran", "Reinoud Maex", "Yi Sun", "Paolo Dini", "Damien Drix", "Ritesh Kumar"]
active_students = ["Yaqoob Muhammad", "Emil Dmitruk  ", "Ohki Katakura", "Rebecca Miko", "Nathan Beka", "Ankur Sinha", "Deepak Panday", "Sam Sutton"]
# -Julia Goncharenko
unknown_status= ["Wajih ul Islam", "Ronak Bhavsar", "Weam Binjumah", "Udeshika Dissanayake", "Edward Wakelam", "Marco Craveiro", "Sudhir Sharma", "Azeemsha Poyil", "Paul Moggridge"]


everyone_list = core_staff+ research_fellows+ active_students
non_core_list = research_fellows+ active_students

def shuffle_list_twice(new_list):
    print ("Original list : ",  new_list)
    shuffle(new_list)
    print ("List after first shuffle  : ",  new_list)

    shuffle(new_list)
    print ("List after second shuffle  : ",  new_list)

shuffle_list_twice(everyone_list)

shuffle_list_twice(non_core_list)