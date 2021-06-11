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

path='assets/tamplate.txt'

"""
 functon to read text  with input: path and return : the  text in file 

"""

def read_template(path):
   with open(path) as file:
       data =file.read()
   return (data)




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

def parse_template(text):

    data=re.findall(r"\{(.*?)\}",text) 
    text=re.sub( r"\{(.*?)\}", '{}', text)
    return [text, tuple(data)]



"""
function to merge the new inputs with the text in file
"""

def merge(pars1,pars2):
   return( pars1.format( *pars2 ) ) 


"""
copy data from merge 
"""
def copyFile(text ):
    file = open('assets/result.txt','w')
    file.write(text)
    print(text)

if __name__ == "__main__":
    pars1 = parse_template(read_template(path))[0]
    pars2 = inputs(parse_template(read_template(path))[1])
    copyFile(merge(pars1,pars2))