#IBM test:

import re
record = input('Enter your record:')
delimiter = input('Enter your special character:')
defaultvalue = 'Null'
    
def replaceMissingField(record, delimiter, defaultvalue):
    a = 0
    if (record[0] == delimiter):
        a+=1
    else:
        a=a
    if (record[len(record)-1] == delimiter):
        a+=1
    else:
        a=a
        
    for i in range(len(record)-1):
        if ((record[i] == delimiter) and (record[i] == record[i+1])):
            a+=1
        else:
            a=a
            
    if record[0] == delimiter:
        text = defaultvalue + record
    else:
        text = record
        
    if text[len(text)-1] == delimiter:
        text = text + defaultvalue
    else:
        text = text
        
    word_split = text.split(delimiter)
    for i in range(len(word_split)):
        if word_split[i]=='':
            word_split[i]=defaultvalue
    result=''
    for i in range(len(word_split)-1):
        result = result + word_split[i] + delimiter
        
    result=result+word_split[len(word_split)-1]
                
    print(result)
    print(a)

def char(record, delimiter):
    match = re.match('[\W]',delimiter)
    search = re.search('[\w]+',record)
    if (search == None) or (re.match('[\W]',delimiter) == None):
        print('Invalid input')
    elif (match != None) and (delimiter in record):
        replaceMissingField(record, delimiter, defaultvalue)
    
    
if __name__=='__main__':
    char(record, delimiter)
    
    