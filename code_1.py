import pandas as pd
import pywhatkit as pwk

database = pd.read_excel('numbers.xlsx')
Ghar = database.Ghar
Friends = database.Friends
Baheti = database.Baheti
Laddha = database.Laddha

image = 'blank.jpeg'
caption = "Save the date! You are cordially invited tomwedding on 14-15 December at Venue, city"

# Ghar:
wait = input('Ghar')
if wait == 'n':
    assert False

for index in range(len(Ghar)):
    if Ghar.notnull()[index]:
        pwk.sendwhats_image('+91'+str(int(Ghar[index])),image,caption,20,True)
        print(f'Sent message to +91{int(Ghar[index])}')

# Friends:
wait = input('Friends')
if wait == 'n':
    assert False

for index in range(len(Friends)):
    if Friends.notnull()[index]:
        pwk.sendwhats_image('+91'+str(int(Friends[index])),image,caption,20,True)
        print(f'Sent message to +91{int(Friends[index])}')

# Baheti:
wait = input('Baheti')
if wait == 'n':
    assert False

for index in range(len(Baheti)):
    if Baheti.notnull()[index]:
        pwk.sendwhats_image('+91'+str(int(Baheti[index])),image,caption,20,True)
        print(f'Sent message to +91{int(Baheti[index])}')

# Laddha:
wait = input('Laddha')
if wait == 'n':
    assert False

for index in range(len(Laddha)):
    if Laddha.notnull()[index]:
        pwk.sendwhats_image('+91'+str(int(Laddha[index])),image,caption,20,True)
        print(f'Sent message to +91{int(Laddha[index])}')

##Old Format:

##for number in numbers:
##    pwk.sendwhats_image('+91'+str(number),image,caption,20,True)
##    print(f'Sent message to +91{number}')
