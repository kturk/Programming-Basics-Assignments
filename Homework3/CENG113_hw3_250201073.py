#250201073
import os

def attributes(query):
    query = input('What is your query?')
    query = query.split(' ')
    if query[0] == 'create':
        del query[1]
        del query[3]

    print(query)


def create_file(file_name, identifiers):
    file = open(file_name, 'w')
    file.write('------------------------------------')
    for identifier in identifiers:
        file.write('|', identifier)
    file.write('------------------------------------')
    file.close()
    
def delete_file(file_name):
    os.remove(file_name)
    
#def add_line():
    
a = 'a'   
attributes(a)

























#def display_files():

#create_file('eafdjkh', 's')