import json

'''
Function Name: create_my_contact
Function description: the purpose of this function is to creat a dict variable with given data
@param: none
@return: the dictionary variable    
'''

def create_my_contact():
    my_contact = { 
        '01': 
       {
       'firstName':  'John', 
       'lastName':  'Smith', 
       'DOB': '1/20/1991', 
       'phoneNum' :{ 
             'number' :  '510-600-5400', 
               'type' :  'cell'} ,
       'address' : {
             'street' :  '100 main street', 
               'city' :  'Fremont', 
              'state' :  'CA', 
            'zipcode' :  '94536'}
       } ,
          '02': 
       {
       'firstName':  'Ron', 
       'lastName':  'Robertson', 
       'DOB': '5/23/1991', 
       'phoneNum' :{ 
             'number' :  '510-600-8800', 
               'type' :  'cell'} ,
       'address' : {
             'street' :  '4600 Ohlone Way', 
               'city' :  'Fremont', 
              'state' :  'CA', 
            'zipcode' :  '94539'}
       } ,
          '03': 
       {
       'firstName':  'Paul', 
       'lastName':  'Washington', 
       'DOB': '6/15/1995', 
       'phoneNum' :{ 
             'number' :  '510-688-1241', 
               'type' :  'cell'} ,
       'address' : {
             'street' :  '8543 Ohlone Plaza', 
               'city' :  'Fremont', 
              'state' :  'CA', 
            'zipcode' :  '94539'}
       } 
     }
    return my_contact

'''
Function Name: save_json_file
Function description: the purpose of this function is to convert our dictionary to json format and write it into a
json file
@param: fileName - name of the file that we are going to create
@param: contact_list - the dictionary that we just created 
@return: none    
'''

def save_json_file(fileName, contact_list):
    json_object = json.dumps(contact_list,indent=4)#convert the python format dict to json format
    fileName = "contact.json"
    with open(fileName, "w") as outfile: #open the json file and write
        outfile.write(json_object)
    outfile.close()

'''
Function Name: open_json_file
Function description: the purpose of this function is to open a json file that we create from the local folder and read info in it
@param: fileName - name of the file
@return: a dictionary in a regular python format    
'''

def open_json_file(fileName):
    fileName = "contact.json" #convert the json format dict to python format
    with open(fileName, 'r') as json_file: #open the json file and read
        data = json.load(json_file)
    return data 


'''
Function Name: find_my_contact_key
Function description: the purpose of this function is determine the searchkey is in the dictionary or not. If the key exist, it will look up
values from the most upper layer of the key and start grabbing info that we need
@param: searchkey - name of item that we want to search
@param: contact_list - the dictionary that we just created 
@return: none    
'''

def find_my_contact_key(searchkey, my_contact):
    found = False #a varible to tell the key is found in the end or not
    print('***Searching for ', searchkey)
    for keys in my_contact: #going through the value of first layer keys(01 02 03)
        for keys2 in my_contact.get(keys): #going throught the value of the second layer keys (keys inside 01 02 such as lastname)
            if my_contact.get(keys).get(keys2) == searchkey: #if the desire content is found
                print('*** ',searchkey,' found ***')
                print('Name:      ',my_contact.get(keys).get('firstName'),' ',my_contact.get(keys).get('lastName'))
                print('Birthday:  ', my_contact.get(keys).get('DOB'))
                print(my_contact.get(keys).get('phoneNum').get('type'), ':     ', my_contact.get(keys).get('phoneNum').get('number'))
                print('Address:   ', my_contact.get(keys).get('address').get('street'))
                print('           ',my_contact.get(keys).get('address').get('city'), ',',my_contact.get(keys)\
                      .get('address').get('state'),"", my_contact.get(keys).get('address').get('zipcode'))
                print()
                found = True
    if not found:
        print('*** ',searchkey,' not found ***')

