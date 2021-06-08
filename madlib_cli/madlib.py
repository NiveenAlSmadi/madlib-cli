import re
welcomeContent = """
     *************************************************
      _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
     |                                                     |
     |      Welcome to the 'MADLIB' Game                   |
     |     Simply we will ask u some Quastions             |
     |  Then you will have a fuuny story for these answers |
     |          So lets have fun!!!                        |
     |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|

     *************************************************
 """

print(welcomeContent)
path='../assets/tamplate.txt'
"""
 functon to read text  with input: path and return : the  text in file 

"""

def read_template(path):
   with open(path) as file:
       data =file.read()
   return (data)

read_template('../assets/tamplate.txt')


# inputs function to resives data 
def inputs(data):
 
    input_list =[]
    print("        So Enter These list AND don't mess it:   " )
    for x in range(21):
        input_list += [input(f'{data[x]} :')]
    return tuple ( input_list)

"""
function find all word in {} and formated with new input by user

"""

def parse_template(path):

    data=re.findall(r"\{(.*?)\}",read_template(path)) 
    text=re.sub( r"\{(.*?)\}", '{}', read_template(path))
    return [text, tuple(data)]



"""
function to merge the new inputs with the text in file
"""

def merge():
   return( parse_template(path)[0].format( *inputs(data=parse_template(path)[1]) ) ) 


"""
copy data from merge 
"""
def copyFile(text ):
    file = open('../assets/result.txt','w')
    file.write(text)
    print(text)
    
copyFile(merge())