'''
Function Name: Main
Function description: the purpose of this function is to call functions from local to create dictionary, store a dict to
local in json format, open the json file and read the dictionary in python format, and do some key searching in the end.
@param: none
@return: none    
'''

import functions
import print_me_first


if __name__ == '__main__': 
    print(print_me_first.printinfo())
    
    contact_list = functions.create_my_contact() # create dictionary 
    functions.save_json_file("my_contact.json", contact_list) # save disctionary to JSON file 
 
    json_data = functions.open_json_file('my_contact.json') #open JSON file load to distionary
 
    print("***BEGINNING OF JSON List: \n", contact_list, \
          "\n***END OF JSON LIST\n\n") 
         
    functions.find_my_contact_key("Ron", json_data) # find record 'Ron' 
    functions.find_my_contact_key("Sha", json_data) # find record 'Sha'
