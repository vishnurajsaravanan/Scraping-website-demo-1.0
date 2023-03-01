from main import *
from stream import *
import pandas as pd
import csv

# dictionary of data
try:
    elements = []
    if dat == 'https://blogs.sap.com/':
        
        for i in range(len(data())):
            for j in range(len(data()[i])):
                auth = data()[i]['Author name']
                head = data()[i]['Heading']
                cont = data()[i]['Content']
                link = data()[i]['Link']
                dict = {
                    "Name": auth, 
                    "Heading": head, 
                    "Text": cont, 
                    "Link":link
                }
                elements.append(dict)
    elif dat == 'https://unfoundation.org/blog/':
        
        for i in range(len(get_data())):
            for j in range(len(get_data()[i])):
                content = get_data()[i]['Content']
                author = get_data()[i]['Author']
                dict = {
                    "Name": author,
                    "Content": content
                }
                elements.append(dict)
    elif dat == 'https://aws.amazon.com/blogs/aws/':
        
        for i in range(len(result_data())):
            for j in range(len(result_data()[i])):
                auth_name = result_data()[i]['Author']
                time = result_data()[i]['Time']
                heading = result_data()[j]['Heading']
                content = result_data()[j]['Content']
                dict = {
                    "Name": auth_name,
                    "On": time,
                    "Title": heading,
                    "Content": content
                }
                elements.append(dict)
except:
    pass

df = pd.DataFrame(elements)
try:
    if dat == 'https://blogs.sap.com/':
        df.to_csv('SAP.csv', index=False)
    elif dat == 'https://unfoundation.org/blog/':
        df.to_csv('unfoundation.csv',index=False)
    elif dat == 'https://aws.amazon.com/blogs/aws/':
        df.to_csv('aws.csv',index=False)
except:
   pass