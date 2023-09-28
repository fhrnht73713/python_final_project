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

    while True:
        print('\nHello! Let\'s explore some US bikeshare data! \n')

        #initialize city, month, day variables
        city = None
        month = None
        day = None

        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            city = input('Select a city to analyze - Chicago, New York City or Washington: \n').lower()
            print()
            if city in ['chicago', 'new york city', 'washington']: #check input against list of cities
                break
            else:
                print('Please choose a valid city. \n')
    
        # get user input for month (all, january, february, ... , june)
        while True:      
            month = input('Select all or filter by month (January-June): \n').lower()
            print()
            if month in ['all','january', 'february', 'march', 'april', 'may', 'june']: #validate user input
                break
            else:
                print('Please choose a valid month. \n')

        # get user input for day of week (all, monday, tuesday, ... sunday)
        while True:       
            day = input('Select all or filter by day of week: \n').lower()
            print()
            if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']: #validate user input
                break
            else:
                print('Please choose a valid day. \n')

        # display user inputs
        if month != 'all':
            if day != 'all':
                print(f'You chose to analyze {day.title()}s in {month.title()} for {city.title()}. \n')
            else:
                print(f'You chose to analyze all days in {month.title()} for {city.title()}. \n')
        else:
            if day != 'all':
                print(f'You chose to analyze {day.title()}s in all months for {city.title()}. \n')
            else:
                print(f'You chose to analyze all days in all months for {city.title()}. \n')    

        # confirm user intended to select inputs
        while True:
            confirm = input('Is this correct? (Type "yes" or "no"): \n').lower()
            print()

            if confirm.lower() == 'yes':  # move forward with analysis section given chosen filters
                print('LET\'S GOOOOOOO!')
                print('-'*40)
                time.sleep(1)
                return city, month, day
            elif confirm.lower() == 'no': # allow user to re-select inputs
                print('Let\'s try again.')
                break
            else:
                print('Please type "yes" or "no". \n') # prompt for valid inputs
                continue


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
    df['month'] = df['Start Time'].dt.month #DO NOT USE .month_name(), as it conflicts with later code... must return type(int)
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
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (DataFrame) df - pandas DataFrame containing city data filtered by month and day
        (int) all_month - an int displaying either 1 or 0 to indicate whether a user selected "all" months
        (int) all_day - an int displaying either 1 or 0 to indicate whether a user selected "all" days of the week
    Returns:
        prints outputs answering descriptive statistics about most popular month, day and hour of travel. 
        Does not return any variables.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n') #This code was modified to only show most common month and day outputs if those filters were not applied.
    
    start_time = time.time()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    # display the most common month  
    if all_month == 1:
       popular_month = df['month'].mode()[0] # find the most common (mode) month
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

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most commonly used bikeshare stations.
    Args:
        (DataFrame) df - pandas DataFrame containing city data filtered by month and day
    Returns:
        prints outputs answering descriptive statistics about most popular start, end and combination of start and end bikeshare stations. 
        Does not return any variables.
    """
    # Displays statistics on the most popular stations and trip.

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is {start_station}. \n')

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'The most commonly used end station is {end_station}. \n')

    # display most frequent combination of start station and end station trip
    combo_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'The most frequent combination of start and end stations is {combo_station[0]} and {combo_station[1]}. \n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the most commonly used bikeshare stations.
    Args:
        (DataFrame) df - pandas DataFrame containing city data filtered by month and day
    Returns:
        prints outputs answering descriptive statistics about most popular start, end and combination of start and end bikeshare stations. 
        Does not return any variables.
    """
    # Displays statistics on the total and average trip duration.

    # Breakdown of number of seconds in each unit of time. This is provided for transparency (specifically with regard to handling the varying number of days in a month).
    minute = 60
    hour = (60 * minute)
    day = (24 * hour)
    week = (7 * day)
    month = ((365 / 12) * day)
    year = (365 * day)

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display breakdown of total travel time
    total_time = df['Trip Duration'].sum()

    years = total_time // year
    seconds_remainder = total_time % year

    months = seconds_remainder // month
    seconds_remainder %= month

    weeks = seconds_remainder // week
    seconds_remainder %= week
    
    days = seconds_remainder // day
    seconds_remainder %= day

    hours = seconds_remainder // hour
    seconds_remainder %= hour

    minutes = seconds_remainder // minute
    seconds_remainder %= minute

    seconds = seconds_remainder
    
    print(f'The total duration of all trips for the selected city and timeframe is {total_time} seconds. ')
    print(f'-------> This equates to {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes and {seconds} seconds. \n')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()

    mean_mins = mean_time // minute
    mean_seconds_remainder = np.floor(mean_time % minute)

    print(f'The mean travel time for all trips for the selected city and timeframe is {mean_time} seconds. ')
    print(f'-------> This equates to roughly {mean_mins} minutes and {mean_seconds_remainder} seconds. \n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on the bikeshare user types and pedigree information.
    Args:
        (DataFrame) df - pandas DataFrame containing city data filtered by month and day
    Returns:
        prints outputs answering descriptive statistics about bikeshare users' types, genders, a birth years. 
        Does not return any variables.
    """
    # Displays statistics on bikeshare users.
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    type_count = df['User Type'].value_counts()
    print(('User Types: '))
    for user_type, count in type_count.items():
        print(f"-------> {user_type}: {count}")
    print()

    # Display counts of gender
    if 'Gender' in df: # Necessary as the "Washington" data file does not contain information about gender or year of birth.
        gender_count = df['Gender'].value_counts()
        print(('Counts for each gender: '))
        for gender, count in gender_count.items():
            print(f'-------> {gender}: {count}')
        print()
    else:
        print('Gender data was not captured for this city. \n')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df: # Necessary as the "Washington" data file does not contain information about gender or year of birth.
        print('Interesting facts: \n')

        earliest_year = int(df['Birth Year'].min())
        print(f'The oldest person in the dataset was born in {earliest_year}. \n')

        recent_year = int(df['Birth Year'].max())
        print(f'The youngest person in the dataset was born in {recent_year}. \n')

        common_year = int(df['Birth Year'].mode()[0])
        print(f'The most common year for a person in the dataset to be born is {common_year}. \n')
    else:
        print('Birth year data was not captured for this city. \n')

    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data_scroller(df, window = 5):
    """
    Displays a rolling selection of raw data from provided dataframe.
    Args:
        (DataFrame) df - pandas DataFrame containing city data filtered by month and day
    Returns:
        Displays a rolling selection of raw data from provided dataframe. 
        Does not return any variables.
    """
    row_count = len(df) # Set an upper bound (and terminating condition) for loop.
    i = 0 # Initialize the incrementing variable
    print()
    while True:
        view_choice = input('Would you like to see the source data? Choose yes or no: \n').lower()

        if view_choice not in ['yes', 'no']: # Validate user input against accepted values
            print()
            print('Please choose yes or no. \n')
            continue

        if view_choice == 'yes':
            print()
            while i < row_count: # Will loop until increment exceeds data file size (i.e. reaches end of file)
                stop = min(i + window, row_count) # Sets condition for number of rows in a given window - specifically for nearing end of file
                selection = df.iloc[i:stop] # Returns a dataframe selection range from row i (incrementing variable) to row "stop" set above
                print(selection)
        
                continue_choice = input(f'\nWould you like to see the next {window} row(s)? Choose yes or no: \n').lower()
                print()

                if continue_choice not in ['yes', 'no']:
                    print('Please choose yes or no. \n')
                    continue

                if continue_choice != 'yes':
                    print('Got it... that\'s enough.')
                    return

                i += window

            print('End of file. \n')
            return
        else:
            print('Got it... you just want the highlights. \n')
            return
      


def main():
    while True:
        city, month, day = get_filters()
        df, all_month, all_day = load_data(city, month, day)

        time_stats(df, all_month, all_day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_scroller (df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        print()
        if restart.lower() in ['yes', 'no']:
            if restart.lower() != 'yes':
                print('Thanks for taking a look! \n')
                return
            else:
                print('Once more into the breach... ')
        else:
            print('Please state "yes" to restart or "no" to quit.')


if __name__ == "__main__":
	main()