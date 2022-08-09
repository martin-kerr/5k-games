import pandas as pd
"""
INTRODUCTION


#Example data in array format: 
a=([
        ['Bushy',  '09/02/2022',  '201',  '24',  '18:01',  '75.21%',  'PB'],
        ['Worcester',  '25/03/2022',  '360',  '13',  '17:38',  '76.84%',  ''],
        ['Alvaston',  '18/04/2022', '86','17', '16:55', '80.10%', 'PB'],
        ['Markeaton','04/04/2022','358','25','17:21','78.10%', '']
        ])

df = pd.DataFrame(a)


Example output:

4 events attended:  Alvaston, Bushy, Markeaton, Worcester
 
4 letters completed:  B, A, M, W
 
22 letters needed:  C, D, E, F, G, H, I, J, K, L, N, O, P, Q, R, S, T, U, V, X, Y, Z

"""


"""
MAIN CODE 
"""
# make dataframe from All Events table (copied to clipboard)
df = pd.read_clipboard()

#add column headings
df.columns=["Event","Run Date","Run Number","Pos","Time","Age Grade","PB"]

#initiate lists of letters completed and needed 
letters_completed=[]
letters_needed=[]

#append first letter of each event done to completed letters list
for event in df['Event']:
    letters_completed.append(event[0])
    
letters_completed =(list(set(letters_completed)))
letters_completed.sort()


#iterate through alphabet to append letters missing from completed list to needed list
    
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for letter in alphabet:
    if letter not in letters_completed:
        letters_needed.append(letter)
  
#print list of events attended in alphabetical order
events_attended= df['Event'].unique()
events_attended.sort()
print(len(events_attended),"events attended: ",", ".join(events_attended))
print(" ")

#print comma separated string of letters completed starting with total number of   
print(len(letters_completed),"letters completed: ", ", ".join(letters_completed))
print(" ")

#print comma separated string of letters needed starting with total number of    
print(len(letters_needed),"letters needed: ", ", ".join(letters_needed))



