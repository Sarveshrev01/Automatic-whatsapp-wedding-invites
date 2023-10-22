import pandas as pd
import pywhatkit as pwk

database = pd.read_excel('/Users/bahet_i7cuys5/Desktop/WhatsApp message/numbers.xlsx')
Ghar = database.Ghar
Friends = database.Friends
Baheti = database.Baheti
Laddha = database.Laddha

image = '/Users/bahet_i7cuys5/Desktop/WhatsApp message/WhatsApp Image 2023-07-24 at 5.43.08 PM.jpeg'
caption = "Save the date! You are cordially invited to Shraddha and Aryan's wedding on 14-15 December at Bhanwar Singh Palace, Pushkar"

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
