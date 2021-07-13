#Membuat fungsi dengan nama function berisi for dan append
def function(newdict):
    a = list()
    for i in newdict.keys():
        a.append(i)
        print(a)
        check_list = type(a) is list
        print(check_list)

#Buat dictionary
dict = {
    1:"Aldo",
    2:"Hanif",
    3:"Yoga",
    4:"Ihsan",
    5:"Prabas",
    6:"Fahri",
    7:"Bagus",
    8:"Fii",
    9:"Hamdy",
    10:"Dandy"
    }

#Panggil fungsi function
function(dict)