from .models import Event
from .models import FreeTime
from .models import ScheduledEvent
from django.conf import settings

allevents = sorted(Event.objects.all(),  key=lambda m: m.Duration, reverse = False)
for event in allevents:
#def auto_event(event):
    isFound = False
    finaltime = 0
    sortindex = optimal_load(event.frequency)
    count = 0
    finalfreetimes = []
    while(not isFound and count < event.frequency):
        tempFound = False
        for intday in range(sortindex[count], 7, event.frequency):
            tempFound = False
            dayfreetimes = FreeTime.objects.filter(start_time.today().weekday()=intday, end_time.today().weekday()=intday)
            for freetime in dayfreetimes:
                if((freetime.end_time - freetime.start_time - 20).total_seconds()/60 > event.Duration):
                    tempFound = True
                    finalfreetimes.append(freetime)
                    break
            if(not tempFound):
                finalfreetimes = []
                break
        if(tempFound):
            isFound = True
        else:
            count = count + 1
    if(finalfreetimes == []):
        #some message to user saying that doesn't work
    else:
        for finaltime in finalfreetimes:
            settings.load[x::frequency] = [x+1 for x in settings.load[x::frequency]]
            s = ScheduledEvent(name = event.name, start_time = finaltime.start_time + datetime.timedelta(minutes = 10), end_time = finaltime.start_time + datetime.timedelta(minutes = duration) + datetime.timedelta(minutes = 20)''', event_id = event.id''')
            if(finaltime.end_time - (finaltime.start_time + datetime.timedelta(minutes = duration) + datetime.timedelta(minutes = 20)) > 20):
                f = FreeTime(start_time = finaltime.start_time + datetime.timedelta(minutes = duration) + datetime.timedelta(minutes = 20), end_time = finaltime.end_time)
            FreeTime.objects.filter(finaltime.id = id).delete()
        Event.objects.filter(event.id = id).delete()

#def user_event(event):


def optimal_load(frequency):
    loadday = [0] * frequency
    for x in range(frequency):
        loadday[x] = sum(settings.load[x::frequency]) / len(settings.load[x::frequency])
    li = []
    for i in range(len(loadday)):
        li.append([loadday[i],i])
    li.sort()
    sortindex = []
    for x in li:
        sortindex.append(x[1])
    return sortindex