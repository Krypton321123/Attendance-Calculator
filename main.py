import numpy as np 
import math
import streamlit as st
import datetime as dt
from day import weekDay
from subject import Subject


def main(): 
    st.write('''
    # Attendance Calculator
    Calculate your attendance *now*!
''')
    global currSub, monday, tuesday, wednesday, thursday, friday, holiday, extraClasses, endDate, currDate, heldClass, attendedClass
    
    currSub = st.text_input("Enter the subject name: ", help="Subject Name")
    heldClass = st.number_input("Enter the total number of classes held till now: ", help="Check the number of classes held for this subject", min_value=0)
    attendedClass = st.number_input("Enter the total amount of Classes attended by you till now: ", min_value=0)
    # currDate = st.date_input()
    currDate = str(st.date_input("Enter today's date: ", help="Leave as is if you want to calculate from now itself"))
    endDate = str(st.date_input("Enter the end date: "))
    monday = st.number_input("Enter the amount of classes of this subject held on Monday: ", min_value=0)
    tuesday= st.number_input("Enter the amount of classes of this subject held on Tuesday: ", min_value=0)
    wednesday = st.number_input("Enter the amount of classes of this subject held on Wednesday: ", min_value=0)
    thursday = st.number_input("Enter the amount of classes of this subject held on Thursday: ", min_value=0)
    friday = st.number_input("Enter the amount of classes of this subject held on Friday: ", min_value=0)
    extraClasses =  st.number_input("Enter the amount of classes which may be held as extra classes(Saturday classes etc): ", min_value=0)
    holiday = ['2024-04-26']
        
    
    if st.button('Calculate!'): 
        st.write(onClick(currSub, monday, tuesday, wednesday, thursday, friday, holiday, extraClasses, endDate, currDate, heldClass, attendedClass))

        
        
def getNumOfDaysOfWeek(startDate,lastDate,holidays,dayOfWeek): 
    numOfDays = np.busday_count(startDate,lastDate,weekmask=dayOfWeek,holidays=holidays)
    return numOfDays

def calculateNoOfClassesForLimit(totalClass,attClass):
    needToAttend = (0.75*totalClass) - attClass
    return math.ceil(needToAttend) 

def onClick(currSub, monday, tuesday, wednesday, thursday, friday, holiday, extraClasses, endDate, currDate, heldClass, attendedClass): 
        monday = weekDay('Mon',monday)
        tuesday = weekDay('Tue',tuesday)
        wednesday = weekDay('Wed',wednesday)
        thursday = weekDay('Thu',thursday)
        friday = weekDay('Fri',friday)

        currSub = Subject(currSub,heldClass,attendedClass)

        numOfMonday = getNumOfDaysOfWeek(startDate=currDate,lastDate=endDate,holidays=holiday,dayOfWeek='Mon')
        numOfTuesday = getNumOfDaysOfWeek(startDate=currDate,lastDate=endDate,holidays=holiday,dayOfWeek='Tue')
        numOfWednesday = getNumOfDaysOfWeek(startDate=currDate,lastDate=endDate,holidays=holiday,dayOfWeek='Wed')
        numOfThursday = getNumOfDaysOfWeek(startDate=currDate,lastDate=endDate,holidays=holiday,dayOfWeek='Thu')
        numOfFriday = getNumOfDaysOfWeek(startDate=currDate,lastDate=endDate,holidays=holiday,dayOfWeek='Fri')

        currAtt = currSub.getCurrentAttendance()
        
        leftClasses = (numOfMonday*monday.getNumOfLecture()) + (numOfTuesday*tuesday.getNumOfLecture()) + (numOfWednesday*wednesday.getNumOfLecture()) + (numOfThursday*thursday.getNumOfLecture()) + (numOfFriday*friday.getNumOfLecture())

        totalHeldClasses = currSub.getHeldLecture() +  leftClasses + extraClasses

        if currAtt > 75: 
            needToAttend = calculateNoOfClassesForLimit(totalHeldClasses, attendedClass)
            canBeBunked = leftClasses - (needToAttend)
            return (f"{math.floor(canBeBunked)} is the amount of classes that you can bunk for {currSub.getName()} and {math.ceil(needToAttend)} is the amount of classes you still need to attend!")
        
        else: 
            needToAttend = calculateNoOfClassesForLimit(totalHeldClasses, attendedClass)
            canBeBunked = leftClasses - (needToAttend)
            leftAtt = (attendedClass + leftClasses)/totalHeldClasses
            if needToAttend > leftClasses: 
                return (f"Sorry, nothing can be done! Your attendance won't reach 75! and it will only reach {leftAtt*100}")
            else: 
                return (f"{math.ceil(needToAttend)} is the amount of that you need to attend for 75! and {math.floor(canBeBunked)} is the amount of classes that can be bunked!")


if __name__ == "__main__":
    main()

