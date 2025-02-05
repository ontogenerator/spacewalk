import json
import csv
import datetime as dt
import matplotlib.pyplot as plt


# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv','w')
graph_file = 'cumulative_eva_graph.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]


for i in range(374):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet


w=csv.writer(output_file)



time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    w.writerow(data[j].values())
    if 'duration' in data[j].keys():
        time_duration=data[j]['duration']
        if time_duration == '':
            pass
        else:
            datetime=dt.datetime.strptime(time_duration,'%H:%M')
            time_delta = dt.timedelta(hours=datetime.hour, minutes=datetime.minute, seconds=datetime.second).total_seconds()/(60*60)
            print(datetime,time_delta)
            time.append(time_delta)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

datetime=[0]
for i in time:
    datetime.append(datetime[-1]+i)

date,time = zip(*sorted(zip(date, time)))


plt.plot(date,datetime[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
