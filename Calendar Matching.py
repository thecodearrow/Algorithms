def isTimeGreaterThanMeeting(time,meetingDuration):
	startTime,endTime=time
	availableTime=minutes(endTime)-minutes(startTime)
	if(availableTime>=meetingDuration):
		return True
	return False
def minutes(timeString):
	#calculates time in minutes from 00:00 given a time string
	hh,mm=timeString.split(":")
	return int(hh)*60+int(mm)
def calculateFreeTime(dailyBounds,calendar,meetingDuration):
	#returns free_times apart from scheduled meetings
	if(len(calendar)==0):
		#whole day is free
		return [dailyBounds]
	dayStartTime,dayEndTime=dailyBounds
	free_times=[]
	#free time before first meeting
	startFirstMeeting,_=calendar[0]
	free_time=[dayStartTime,startFirstMeeting]
	if(isTimeGreaterThanMeeting(free_time,meetingDuration)):
		free_times.append(free_time)
	
	#free_times between meetings
	for i in range(1,len(calendar)):
		startMeet1,endMeet1=calendar[i-1]
		startMeet2,endMeet2=calendar[i]
		free_time=[endMeet1,startMeet2]
		if(isTimeGreaterThanMeeting(free_time,meetingDuration)):
			free_times.append(free_time)
		
	#free time after last meeting
	_,endLastMeeting=calendar[-1]
	free_time=[endLastMeeting,dayEndTime]
	if(isTimeGreaterThanMeeting(free_time,meetingDuration)):
		free_times.append(free_time)
	
	return free_times
	
def maxTime(t1,t2):
	if(minutes(t1)>=minutes(t2)):
		return t1
	return t2

def minTime(t1,t2):
	if(minutes(t1)<=minutes(t2)):
		return t1
	return t2
		
def calculateComonFreeTime(free_time1,free_time2,meetingDuration):
	common_times=[]
	for i in range(len(free_time1)):
		s1,e1=free_time1[i]
		for j in range(len(free_time2)):
			s2,e2=free_time2[j]
			common_time=[maxTime(s1,s2),minTime(e1,e2)]
			print(common_time)
			if(isTimeGreaterThanMeeting(common_time,meetingDuration)):
				common_times.append(common_time)
	return common_times


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    free_time1=calculateFreeTime(dailyBounds1,calendar1,meetingDuration)
	free_time2=calculateFreeTime(dailyBounds2,calendar2,meetingDuration)
	common_time=calculateComonFreeTime(free_time1,free_time2,meetingDuration)
	return common_time
