import time 
import pandas as pd 
import numpy as np 
import json  

CITY_DATA = { 'chicago': 'chicago.csv', 
              'new york': 'new_york_city.csv', 
              'washington': 'washington.csv' }
cities = ('chicago', 'new york', 'washington')
months = ('all','january', 'february', 'march', 'april', 'may', 'june')
days = ('all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
  

def get_filters(): 
    """ 
    Asks user to specify a city, month, and day to analyze. 
    Returns: 
        (str) city - name of the city to analyze 
        (str) month - name of the month to filter by, or "all" to apply no month filter 
        (str) day - name of the day of week to filter by, or "all" to apply no day filter 
    """ 

    print('Hello! Let\'s explore some US bikeshare data!') 
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs 
    while True: 
        city=input('Which of these cities do you want to explore : Chicago, New York or Washington? \n> ').lower() 
        if city in cities: 
            break       

    # TO DO: get user input for month (all, january, february, ... , june) 
    while True:
        month = input('Now you have to enter a months from {} to get some months result or type \'all\' if you need all months data. \n>'.format(months)).lower()
        if month in months:
            break  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Now you have to choose any day in a week from {} or type \'all\' if you need the whole week data. \n> '.format(days)).lower()  
        if day in days:
            break

    print('-'*40) 
    return city, month, day 

def load_data(city, month, day): 
    """ 
    Loads data for the specified city and filters by month and day if applicable. 
    Args: 
        (str) city - name of the city to analyze 
        (str) month - name of the month to filter by, or "all" to apply no month filter 
        (str) day - name of the day of week to filter by, or "all" to apply no day filter 
    Returns: 
        df - Pandas DataFrame containing city data filtered by month and day 
    """   

    # load data from csv according to city selected 
    df = pd.read_csv(CITY_DATA[city]) 
      
    ## convert the Start Time column to datetime  
    df['Start Time'] = pd.to_datetime(df['Start Time'])  

    # extract month and day of week and hour from Start Time to create new columns 
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour'] = df['Start Time'].dt.hour 

    # filter by month if applicable 
    if month != 'all': 
        month =  months.index(month) + 1 
        df = df[ df['month'] == month] 

    # filter by day of week if applicable 
    if day != 'all': 
        # filter by day of week to create the new dataframe 
        df = df[ df['day_of_week'] == day.title()] 

    return df 

def time_stats(df): 
    """Displays statistics on the most frequent times of travel.""" 
  
    print('\nCalculating The Most Frequent Times of Travel...\n') 
    start_time = time.time() 

    # value_counts - Return a Series containing counts of unique rows in the DataFrame. 
    # idxmax - Return index of first occurrence of maximum over requested axis. 
    # TO DO: display the most common month 
    most_common_month = df['month'].value_counts().idxmax() 
    months_title=months[most_common_month-1] 
    print('The most common month {}'.format(months_title)) 

    # TO DO: display the most common day of week 
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax() 
    print('The most common day of week {}'.format(most_common_day_of_week)) 

    # TO DO: display the most common start hour 
    most_common_start_hour = df['hour'].value_counts().idxmax() 
    print('The most common start hour {}'.format(most_common_start_hour)) 

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def station_stats(df): 
    """Displays statistics on the most popular stations and trip.""" 

    print('\nCalculating The Most Popular Stations and Trip...\n') 
    start_time = time.time() 

    # TO DO: display most commonly used start station 
    most_common_start_station = df['Start Station'].value_counts().idxmax() 
    most_common_start_station_count = df['Start Station'].value_counts()[most_common_start_station] 
    print('The most commonly used start station {} with count {} '.format(most_common_start_station,most_common_start_station_count)) 

    # TO DO: display most commonly used end station 
    most_common_end_station = df['End Station'].value_counts().idxmax() 
    most_common_end_station_count = df['Start Station'].value_counts()[most_common_end_station] 
    print('The most commonly used end station {}with count {} '.format(most_common_end_station,most_common_end_station_count)) 

    #loc - is primarily label based, but may also be used with a boolean array (Access group of values using labels.) 
    # TO DO: display most frequent combination of start station and end station trip 
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print('The most frequent combination of {}'.format(most_common_start_end_station))

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def trip_duration_stats(df): 
    """Displays statistics on the total and average trip duration.""" 
    print('\nCalculating Trip Duration...\n') 
    start_time = time.time() 

    # TO DO: display total travel time 
    total_travel_time = df['Trip Duration'].sum() 
    print('The total travel time {}'.format(total_travel_time)) 

    # TO DO: display mean travel time 
    mean_travel_time = df['Trip Duration'].mean() 
    print('The mean travel time {}'.format(mean_travel_time)) 
    
    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def user_stats(df): 
    """Displays statistics on bikeshare users.""" 

    print('\nCalculating User Stats...\n') 
    start_time = time.time() 

    # TO DO: Display counts of user types 
    user_types_counts = df['User Type'].value_counts() 
    print(' \nDisplay counts of user types:') 
    for index, user_types_count in enumerate(user_types_counts): 
        print('{} - {}'.format(user_types_counts.index[index],user_types_count)) 

    print()

    # TO DO: Display counts of gender 
    if 'Gender' in df.columns:
        user_gender_stat(df)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:    
        user_birthday_stat(df)


    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40) 

def user_gender_stat(df):
    gender_counts = df['Gender'].value_counts() 
    print('\nDisplay counts of gender:') 
    for index, gender_count in enumerate(gender_counts): 
        print('{} - {}'.format(gender_counts.index[index],gender_count))

def user_birthday_stat(df):
    # Display earliest year of birth 
    print('\nDisplay year of birth data:') 
    earliest_year = df['Birth Year'].min() 
    print('The most earliest year of birth: {}'.format(earliest_year)) 

    # Display most recent year of birth 
    most_recent_year = df['Birth Year'].max() 
    print('The most recent year of birth: {}'.format(most_recent_year)) 
        
    # Display most common year of birth 
    most_common_year = df['Birth Year'].value_counts().idxmax() 
    print('The most common birth year: {}'.format(most_common_year)) 

def display_data(df):
    row_length = df.shape[0]
    # iterate from 0 to the number of rows in steps of 5
    for i in range(0, row_length, 5):
        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break
        
        # retrieve and convert data to json format
        # split each json row data 
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # check if row is not an empty string before attempting to parse
            if row.strip():
                # pretty print each user data
                parsed_row = json.loads(row)
                json_row = json.dumps(parsed_row, indent=2)
                print(json_row)
            else:
                print("Empty or invalid JSON row: '{}'".format(row))

# Main System flow
# 1. User choose the city
# 2. User choose the month interested
# 3. User choose the day of the week to check
def main():  
    while True:  
        city, month, day = get_filters()  
        df = load_data(city, month, day)  

        time_stats(df)  
        station_stats(df)  
        trip_duration_stats(df)  
        user_stats(df)
        
        display_data(df)
 
        restart = input('\nWould you like to restart? Enter yes or no.\n')  
        if restart.lower() != 'yes':  
            break  

  
if __name__ == "__main__":
    main() 