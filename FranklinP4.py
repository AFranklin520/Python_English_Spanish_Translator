# FranklinP4
# FranklinP4
# Programmer: Anthony Franklin
# Email: afranklin18@cnm.edu
# Purpose: translate common phrases


#http://www.learnspanishtoday.com/learning_module/grammar.htm
english2spanish={'Good morning.':'Buenos dias.',
'Good afternoon.':'Buenas tardes.',
'Good evening. (greeting)':'Buenas noches.',
'Hello, my name is John.':'Hola, me llamo Juan.',
'What is your name?':'¿Como se llama usted?',
'How are you?':'¿Como esta usted?',
'I am fine.':'Estoy bien.',
'Nice to meet you.':'Mucho gusto.',
'Goodbye.':'Adios.',
'See you later.':'Hasta luego.',
'I am lost. Where is the restroom?':'Estoy perdido. Dónde está el baño',
'Excuse me.':'Con permiso.  OR  Perdóname',
'Please.':'Por favor.',
'Thank you.':'Gracias.',
'Bless you.':'Salud.',
'You are welcome (it was nothing).':'De nada.',
'How much does it cost?':'¿Cuanto cuesta?',
'How many are there?':'¿Cuantos hay?',
'There are many.':'Hay muchos.',
'Do you want to buy this?':'¿Quiere comprarlo usted?',
'What time is it?':'¿Qual hora es?',
'How do you say maybe in Spanish?':'¿Como se dice maybe en Español?',
'Yes.':'Si.',
'No.':'No.',
'I do not understand.':'Yo no comprendo.',
'Would you speak slower, please.':'Por favor, habla mas despacio.',
'Who?':'¿Quien?',
'Why?':'¿Por que?'}

x=english2spanish

intro= 'English to Spanish Translator \ Traductor de Español a Inglés'
print(intro)
text_width =len(intro)
screen_width=80
box_width=text_width+6
left_margin=(screen_width-box_width)//2
print(' '*left_margin+'*'*text_width)
print(' '*left_margin+intro)
print(' '*left_margin+'*'*text_width)


response=input('For English to Spanish please select 1, Para Español a Inglés Seleccione 2: ')

    
if response=='1':
    print('This program provides a list of phrases that it will translate into Spanish for you.')
    
if response=='2':
    print('Este programa proporciona una lista de frases que le traducirá al inglés.')

    
if response=='1':
    i=0
    phrases=[]
    for phrase in x:
        print(str(i)+": "+phrase)
        i += 1
        phrases.extend([phrase])
    s=input('Please select a number from the list: ')
    keys=list(x.keys())
    vals=list(x.values())
    print(phrases[int(s)], ' = ',vals[int(s)])
    
if response=='2':
    i=0
    phrases=[]
    for phrase in(x.values()):
        print(str(i)+": "+phrase)
        i += 1
        phrases.extend([phrase])
    s=input('Por favor seleccione un número de la lista: ')
    keys=list(x.keys())
    vals=list(x.values())
    print(phrases[int(s)], ' = ',keys[int(s)])

input()


