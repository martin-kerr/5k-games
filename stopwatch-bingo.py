import pandas as pd
import matplotlib.pyplot as plt

# Input: Load DataFrame from clipboard (Copy data in athlete's 'All Results' table )
df = pd.read_clipboard()

#add column headings
df.columns=["Event","Run Date","Run Number","Pos","Time","Age Grade", "PB"]

#Parse Time column to datetime format
df['Time']=pd.to_datetime(df['Time'],format= '%M:%S')

#make seconds only column
df['Seconds']=df['Time'].dt.strftime('%S')#string format
df['Seconds'] = pd.to_numeric(df['Seconds'])#converted to numeric format

#make dictionary of occurrences of each second
sec_counts={}
for s in range(60):    
    sec_counts[s] = ((df['Seconds'].values==s).sum())

#initiate lists of seconds completed and needed 
seconds_completed=[]
seconds_needed=[]

#iterate through occurrences dictionary and add to list of completed or needed
for s in sec_counts:
    if sec_counts[s]==0 :
        seconds_needed.append(s)
    else:
        seconds_completed.append(s)
'''
PLOT
bar plot showing count of each second with text box
underneath listing seconds yet to be completed
'''
#calulate variables to include in output f strings
pr_completed=len(df)

no_secs_completed=len(seconds_completed)
str_secs_completed=",".join(str(i) for i in seconds_completed)

no_secs_needed=len(seconds_needed)
str_secs_needed=",".join(str(i) for i in seconds_needed)

# include list of smallest of completed or needed list in text box caption
if no_secs_needed < 30:
    caption=f'{pr_completed} parkruns completed\n\n{no_secs_completed} seconds completed\n\n {no_secs_needed} seconds needed: {str_secs_needed}'
else:
    caption=f'{pr_completed} parkruns completed\n\n{no_secs_completed} seconds completed: {str_secs_completed}\n\n {no_secs_needed} seconds needed'

#create fig and axes
fig = plt.figure()
fig.suptitle('Stopwatch Bingo', fontsize=20)
ax=plt.subplot(3,1,(1,2)) #axes takes up two thirds of figure
x=sec_counts.keys()
y=sec_counts.values()
ax.bar(x,y)
ax.set_xlabel('Second')
ax.set_ylabel('Occurances')
plt.xlim([-0.5,59.5])

#arrange textbox caption with box round
plt.figtext(0.5,0.18,caption,ha='center',va='center',bbox={"fc":"white"}, wrap=True)
plt.show()

