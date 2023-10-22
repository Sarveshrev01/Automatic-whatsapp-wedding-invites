import pandas as pd
import pywhatkit as pwk

database = pd.read_excel('numbers.xlsx')

#Stack line 6 to 20 for different columns
number_set = database.Numbers

image = 'blank.jpeg'
caption = "Save the date! You are cordially invited to wedding on <date> at <venue>, <city>"

# Numbers:
wait = input('Numbers')
if wait == 'n':
    assert False

for index in range(len(number_set)):
    if number_set.notnull()[index]:
        pwk.sendwhats_image('+91'+str(int(number_set[index])),image,caption,20,True)
        print(f'Sent message to +91{int(number_set[index])}')

##Old Format:

##for number in number_set:
##    pwk.sendwhats_image('+91'+str(number),image,caption,20,True)
##    print(f'Sent message to +91{number}')