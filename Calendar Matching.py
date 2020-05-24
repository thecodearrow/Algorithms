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

def isOverlap(s1,e1,s2,e2):
	"""
	if(minutes(s2)<=minutes(s1) and minutes(s1)<=minutes(e2)):
		#s1 lies in [s2,e2]
		return True
	if(minutes(s2)<=minutes(e1) and minutes(e1)<=minutes(e2)):
		#e1 lies in [s2,e2]
		return True
	return False
	"""
	if(minutes(maxTime(s1,s2))<=minutes(minTime(e1,e2))):
		return True
	return False
def calculateComonFreeTime(free_time1,free_time2,meetingDuration):
	#Merge Free Times! 
	#I think we can use the merge interval algorithm here!
	common_times=[]
	i=0
	j=0
	while i<len(free_time1) and j<len(free_time2):
		s1,e1=free_time1[i]
		s2,e2=free_time2[j]
		#check if there's a overlap
		if(isOverlap(s1,e1,s2,e2)):
			common_time=[maxTime(s1,s2),minTime(e1,e2)]
			if(isTimeGreaterThanMeeting(common_time,meetingDuration)):
				common_times.append(common_time)
		if(minTime(e1,e2)==e1):
			#endpoints need to be checked!
			#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
			#t1 < t2 
			i+=1
		else:	
			#t2 <t1
			j+=1
		
	return common_times


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # Write your code here.
    free_time1=calculateFreeTime(dailyBounds1,calendar1,meetingDuration)
	free_time2=calculateFreeTime(dailyBounds2,calendar2,meetingDuration)
	print(free_time1,"1")
	print(free_time2,"2")
	common_time=calculateComonFreeTime(free_time1,free_time2,meetingDuration)
	return common_time
