import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Select a city to analyze - Chicago, New York City or Washington: ').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Please choose a valid city.')
    
    # get user input for month (all, january, february, ... , june)
    while True:      
        month = input('Select all or filter by month (January-June): ').lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Please choose a valid month.')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:       
        day = input('Select all or filter by day of week: ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Please choose a valid day.')

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
        df - pandas DataFrame containing city data filtered by month and day
    """
    all_month = 0
    all_day = 0
    
    # load data file into a dataframe
    filename = CITY_DATA[city] 
    df = pd.read_csv(filename)
       
    df['Start Time'] = pd.to_datetime(df['Start Time']) # convert the Start Time column to datetime
    
    # extract month, day and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    months = ['january', 'february', 'march', 'april', 'may', 'june']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # filter by month if applicable
    if month in months:
        month_index = months.index(month) + 1
        df = df[df['month'] == month_index] # filter by month to create the new dataframe
    else:
        all_month = 1 # If 'all' is chosen, set all_month to str(1)

    # filter by day of week if applicable
    if day in days:
        df = df[df['day_of_week'] == day.title()] # filter by day of week to create the new dataframe
    else:
        all_day = 1 # If 'all' is chosen, set all_day to str(0) -indicates 'zero filter'
    return df, all_month, all_day


def time_stats(df, all_month, all_day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    # display the most common month  
    if all_month == 1:
       popular_month = df['month'].mode()[0] # find the most common month
       title_month = months[popular_month].title()
       print(f'The most popular month to use bikeshare assets is: {title_month}. \n')
    else:
       print('Displaying data for selected month. \n')

    # display the most common day of week
    if all_day == 1: 
       popular_day = df['day_of_week'].mode()[0] # find the most common day
       print(f'The most popular day of the week to start using bikeshare assets is: {popular_day.title()}. \n')
    else:
       print('Displaying data for selected day of the week. \n')

    # display the most common start hour  
    popular_hour = df['hour'].mode()[0] # find the most common hour (from 0 to 23)
    print(f'Given the supplied filters, the most popular hour to start using bikeshare assets is: {popular_hour}:00. \n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""
def station_stats(df):
    # Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    # Displays statistics on the total and average trip duration.

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    # Displays statistics on bikeshare users.

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
"""

def main():
    while True:
        city, month, day = get_filters()
        df, all_month, all_day = load_data(city, month, day)

        time_stats(df, all_month, all_day)
        #station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() in ['yes', 'no']:
            if restart.lower() != 'yes':
                print('Thanks for taking a look!')
                break
            else:
                print('Once more into the breach...')
        else:
            print('Please state "yes" to restart or "no" to quit.')



if __name__ == "__main__":
	main()