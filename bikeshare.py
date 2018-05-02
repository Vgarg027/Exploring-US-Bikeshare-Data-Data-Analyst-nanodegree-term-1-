import csv # reading and writing to CSV files
import time
from datetime import datetime # operations to parse dates
import calendar
from pprint import pprint # use to print data structures like dictionaries in a nicer way than the base print function.
import pandas as pd # converts CSV files into dataframes which are more practical to use than plain text


# Filenames
chicago         = 'chicago.csv'
new_york_city   = 'new_york_city.csv'
washington      = 'washington.csv'

def get_city():
    '''
    Asks the user for a city and returns the filename for that city's bike share data.
    Args:			none.
    Returns:		(str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for chicago, new_york_city, or washington?  (Not case sensitive)\n'
                 'Enter exit to terminate\n')
    city=city.lower()
    while(city != 'chicago' and city != 'new_york_city' and city != 'washington' and city != 'exit'):     #not case sensitive

        print("Oops... Sorry, wrong input \n Please give correct choice: chicago, new_york_city or washington")
        print("Enter exit to terminate")
        city = input()
        city=city.lower()

    return city




def get_time_period():
    '''
    Asks the user for a time period and returns the specified filter.
    Args: none.
    Returns: Choice of Filter
    '''
    time_period = input('\nWould you like to filter the data by month, day, both or not at'
                        ' all? Type "none" for no time filter.(not case sensitive)\nEnter exit to terminate\n')
    time_period=time_period.lower()
    while(time_period != 'month' and time_period != 'day' and time_period != "both" and time_period != 'none' and time_period != "exit"):
        print('Sorry, wrong input \n Please type "month", "day", "both" or "none" as filter choice')
        print("Enter exit to terminate")
        time_period = input()
        time_period=time_period.lower()
    return time_period


def get_month():
    '''
    Asks the user for a month and returns the specified month.
    Args:   none.
    Returns: Month name as choice entered by user
    '''
    month = input('\nWhich month? Jan(1), Feb(2), March(3), April(4), May(5), or June(6)?\nPlease enter integer values\n Enter -1 to exit\n')
    while(month!='1' and month!='2' and month!='3' and month!='4' and month!='5' and month!='6' and month!='-1'):
        print('Sorry, wrong input \n Please enter "1-Jan", "2-Feb", "3-March", "4-April", "5-May", or "6-June" ')
        print("Enter -1 to exit")
        month = input()
    return int(month)




def get_day():
    '''
    Asks the user for a day and returns the specified day.
    Args:    none.
    Returns: Day name as choice entered by user
    '''
    day = int(input('\nWhich day? Please type your response as an integer.\n'
                    '0-Mon, 1-Tues, 2-Wed, 3-Thurs, 4-Fri, 5-Sat, 6-Sun\n'))
    while(day < -1 or day > 6):
        print('Sorry invalid input \nPlease type integer between 0 and 6 as day of week(0 and 6 inclusive)')
        print('Enter -1 to exit\n')
        day = int(input())
    return day



def popular_month(datetime_col, time_period):
    '''
    Question: What month occurs most often in the start time?
    Args:     datetime column, user specified filter
    Returns: none

    Discription: Only datetime_col is passed as argument because in csv file the datetime col had different format than standard
    and after making changes in the city_file itself took lot of time to execute... So to avoid that only modified datetime col
    has been passed from statistics...
    '''
    month       = pd.Series((x.month) for x in datetime_col)    #making a column of month no. values from given datetime column
    pop_month   = month.value_counts().idxmax()                 #finding month_name with max occurance
    count       = month.value_counts().max()                    #finding count of month with max occurance
    print("Most Popular month : ",calendar.month_name[pop_month],end="    ")
    print("Count :",count,end="    ")
    print("Filter:",time_period)





def popular_day(datetime_col, time_period):
    '''
    Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
    Args:     datetime column, user specified filter
    Returns: none
    '''
    day       = pd.Series((x.weekday()) for x in datetime_col)  #making a column of weekday values from given datetime column
    pop_day   = day.value_counts().idxmax()                     #finding weekday_name with max occurance
    count     = day.value_counts().max()                        #finding count of weekday with max occurance
    print("Most Popular weekday : ",calendar.day_name[pop_day],end="    ")
    print("Count :",count,end="    ")
    print("Filter:",time_period)



def popular_hour(datetime_col, time_period):
    '''
    Question: What hour of the day (1, 2, ... 23, 24) occurs most often in the start time?
    Args:     datetime column, user specified filter
    Returns: none
    '''
    hour       = pd.Series((x.hour) for x in datetime_col)      #making a column of hour values from given datetime column
    pop_hour   = hour.value_counts().idxmax()                   #finding hour time with max occurance
    count      = hour.value_counts().max()                      #finding count of hour time with max occurance
    print("Most Popular hour : ",pop_hour,end="    ")
    print("Count :",count,end="    ")
    print("Filter:",time_period)




def trip_duration(Trip_dur_col, time_period):
    '''
    Question: What is the total trip duration and average trip duration?
    Args    : Trip duration column, time period filter
    Returns : none
    '''
    #duration_col=time_diff_col.apply(lambda x : int(x.total_seconds()/60)) #calculation of trip duration in minutes
    print("Total trip duration : {} hours ".format(sum(Trip_dur_col)/3600),"        Filter :",time_period) #calculating total trip duration in hours

    print("Average trip duration : {} minutes ".format((Trip_dur_col.mean())/60),end="    ")              #calculating average trip duration in minutes
    print("Filter:",time_period)



def popular_stations(city_file, time_period):
    '''
    Question: What is the most frequently used start station and most frequently used end station?
    Args    : city_file, time_period filter
    Returns : none
    '''
    start_st_count  =   city_file['Start Station'].value_counts()
    end_st_count    =   city_file['End Station'].value_counts()
    Max_start_st    =   start_st_count.idxmax()                             #Start station name with maximum occurance
    count1          =   start_st_count.max()                                #Start station count with maximum occurance
    Max_end_st      =   end_st_count.idxmax()                               #End station name with maximum occurance
    count2          =   end_st_count.max()                                  #End station name with maximum occurance

    print("Most Frequent Start station is:",Max_start_st, end="    ")
    print("Count: ",count1,end="    ")
    print("Filter:",time_period)

    print("Most Frequent End station is:",Max_end_st,end="    ")
    print("Count: ",count2,end="    ")
    print("Filter:",time_period)



def popular_trip(city_file, time_period):
    '''
    Question: What is the most common trip (i.e., the combination of start station and end station that occurs the most often)?
    Args    : city_file, time_period filter
    Returns : none
    '''
    start_station   =   city_file['Start Station']        #seperating out start station column from city_file for easy access
    end_station     =   city_file['End Station']          #seperating out end station column from city_file for easy access

    trip_col        =   start_station +" --to-- "
    trip_col        +=  end_station                                  #combining start_station and end_station into single trip_col
    Most_common     =   trip_col.value_counts().idxmax()             #trip name with max occurance
    count           =   trip_col.value_counts().max()
    print('Most common trip is:   ', Most_common)
    print('Count = ',count,"         Filter:",time_period)


def users(User_col, time_period):
    '''
    Question: What are the counts of each user type?
    '''
    counts  =   pd.Series(User_col.value_counts())         #creating a dataframe with user name and their count
    print('Various users :             Filter is ',time_period)
    for name in counts.index:
        print(name," : ",counts[name])                     #or use iloc[]  #printing names of users along with the count



def gender(Gender_col, time_period):
    '''Question: What are the counts of gender?'''
    Gender_col  =   Gender_col.dropna(how = 'any')         #removing null values from gender column
    counts      =   Gender_col.value_counts()              #creating a dataframe with gender name and their count
    print("Gender count :              Filter is ",time_period)
    for name in counts.index:
        print(name," : ",counts[name])                     #printing names of users along with the count


def birth_years(Birth_col, time_period):
    '''Question: What is the earliest birth year (when the oldest person was born), most recent birth year, and most common birth year?'''
    Birth_col   =   Birth_col.dropna(how = 'any')           #ignoring null values from Birth_col
    oldest      =   int(Birth_col.min())                    #calculating earliest birth year
    most_recent =   int(Birth_col.max())                    #calculating the most recent birth year
    most_common =   int(Birth_col.value_counts().idxmax())  #printing the birth year occuring max number of times
    print('Earliest birth year:',oldest,"             Filter is: ",time_period)
    print('Most recent birth year:',most_recent,"           Filter is: ",time_period)
    print('Most common birth year:',most_common,"           Filter is: ",time_period)



def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.'''

    display = input('\nWould you like to view individual trip data?'
                   'Type \'yes\' or \'no\'.\n')

    count = 1                                   #postion of row being printed from csv file
    count2 = 1                                  #counter to keep record of how many rows have been printed
    while True:                                 #while loop to take repeated input from user and printing rows of raw dataframe
        if(display=="yes"):
            print('{')
            print(city_file.iloc[count2])       #printing row of csv file according to count2
            print('}\n')
            count+=1
            count2+=1
        elif(display=="no"):
            break
        else:
            print("Wrong input... \n")          # asking user to enter again in case of wrong input
            count=5

        if(count==5):
            display = input('\nWould you like to view more?'
                            'Type \'yes\' or \'no\'.\n')
            count=1                             #resetting the count of rows printed
        # print()


def statistics():
    '''
    Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    Args:   none.
    Returns:none.
    '''

    city                 = get_city()        # Choice of city for statistics (Chicago, New York, Washington)
    if(city=='exit'):
        return
    time_period          = get_time_period() # Filter by time period (month, day, both, none)
    if(time_period=='exit'):
        return
    print("Fetching data.....")
    path                 ='G:/school work/nanodegree/Python/bikeshare/'
    city_file            = pd.read_csv(path+city+'.csv') #fetching csv file using name specified by user

    print("Just few moments.....")
    start_time_col       = city_file['Start Time']
    actual_start_time_col= pd.to_datetime(start_time_col) #converting string format date to standard datetime format

    #pd.Series(datetime.strptime(x,'%d-%m-20%y %H:%M') for x in start_time_col)
    #print(actual_start_time_col)

    print("Performing necessary calculations.....")
    city_file['month_col']      = actual_start_time_col.dt.month      #creating a month column in csv file
    city_file['day_of_week_col']= actual_start_time_col.dt.weekday    #creating a weekday column in csv file

    if(time_period == "month" or time_period == "both"):              #filtering the data month wise if filter is month or both
        month                   = get_month()
        if(month==-1):
            return
        city_file               = city_file[city_file['month_col'] == month]
        start_time_col          = city_file['Start Time']
        actual_start_time_col   = pd.to_datetime(start_time_col)
        #print(city_file)

    if(time_period == "day" or time_period == "both"):              #filtering the data day wise if filter is day or both
        day                     = get_day()
        if(day==-1):
            return
        city_file               = city_file[city_file['day_of_week_col'] == day]
        start_time_col          = city_file['Start Time']
        actual_start_time_col   = pd.to_datetime(start_time_col)
        #print(city_file)

    print('Please wait while we are calculating statistics....\n')
    s_time = time.time()

    if(time_period=='none'):
        popular_month(actual_start_time_col, time_period)     #priting popular month only if filter is none

    if(time_period=='none' or time_period=='month'):          #priting popular day only if filter is none or month
        popular_day(actual_start_time_col,time_period)

    popular_hour(actual_start_time_col,time_period)
    trip_duration(city_file['Trip Duration'],time_period)
    popular_stations(city_file, time_period)
    popular_trip(city_file,time_period)
    print()
    users(city_file['User Type'],time_period)
    print()
    if('Gender' in city_file):                             #Washington file seperated out because it does not contain gender and time period time periods
        gender(city_file['Gender'],time_period)
        print()
    if('Birth Year' in city_file):
        birth_years(city_file['Birth Year'],time_period)
        print()

    print("That took %s seconds." % (time.time() - s_time))
    display_data(city_file)
    print("\n")

    restart = input("Do you wish to restart\nType Yes or No\n")
    restart = restart.lower()

    if(restart == "yes"):
        print("Restarting the script...\n")
        statistics()

    elif(restart == "no"):
        print("Thank You\n")
        return

    else:
        print("Sorry wrong input....\nTerminating....\n")
        return


'''
city=get_city()  #for specific columns
path='G:/school work/nanodegree/Python/bikeshare/'
city_file=pd.read_csv(path+city+'.csv',usecols=['Start Time','End Time','Start Station','End Station'])

print(city_file)
'''
if __name__ == "__main__":
    statistics()
