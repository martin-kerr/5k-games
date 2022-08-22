from datetime import datetime
import pandas as pd

#construct test DataFrame 
'''
a=([
        ['Bushy',  '09/02/2022',  '201',  '24',  '18:38',  '75.21%',  'PB'],
        ['Worcester',  '25/03/2022',  '360',  '13',  '17:38',  '76.84%',  ''],
        ['Alvaston',  '18/04/2022', '86','17', '16:38', '80.10%', 'PB'],
        ['Aberdeen','04/04/2022','358','25','17:00','78.10%', '']
        ])

df = pd.DataFrame(a)
'''
# Input: Load DataFrame from clipboard (Copy data in athlete's 'All Results' table )
df = pd.read_clipboard()

#add column headings
df.columns=["Event","Run Date","Run Number","Pos","Time","Age Grade","PB"]

#initiate lists of letters completed and needed 
seconds_completed=[]
seconds_needed=[]

#Parse Time column to datetime format
df['Time']=pd.to_datetime(df['Time'],format= '%M:%S')

#make seconds only column
df['Seconds']=df['Time'].dt.strftime('%S')#string format
df['Seconds'] = pd.to_numeric(df['Seconds'])#converted to numeric format

#make dictionary of occurrences of each second
sec_counts={}
for s in range(60):    
    sec_counts[s] = ((df['Seconds'].values==s).sum())

#iterate through occurrences dictionary and add to list of completed or needed
for s in sec_counts:
    if sec_counts[s]==0 :
        seconds_needed.append(s)
    else:
        seconds_completed.append(s)

#print total parkruns
print(len(df),"parkruns completed")
print("")

#print comma separated string of seconds completed starting with number of   
print(len(seconds_completed),"seconds completed:", ",".join(str(i) for i in seconds_completed))

print(" ")

#print comma separated string of seconds  needed  starting with number of   
print(len(seconds_needed),"seconds needed:", ",".join(str(i) for i in seconds_needed))
