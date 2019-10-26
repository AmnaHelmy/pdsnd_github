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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input('Whould you like to see the data for Chicago, New York City, or Washington?\n').lower()
      if city in ['chicago','new york city','washington']:
          break
      else:
          print('Please enter full name of the city.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input('Enter a month name (e.g. january, february, march, april, may, june) or enter "all" to select all months.\n').lower()
      if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
          break
      else:
          print('This isn\'t a valid month name')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('Enter a week day(e.g. monday, tuesday, wednesday, thursday, friday, saturday, sunday) or enter "all" to select all days.\n').lower()
      if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
          break
      else:
          print('This isn\'t a valid week day')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_weekday = df['day_of_week'].mode()[0]
    print('Most common weekday:', common_weekday)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_st = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_st)

    # TO DO: display most commonly used end station
    common_end_st = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ', ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print('Most frequent combination of start station and end station trip:', common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()/60
    print('Total travel time in minutes: ', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()/60
    print('Mean travel time in minutes: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
      print('Users gender info doesn\'t exist')
    else:
      gender_types = df['Gender'].value_counts()
      print('Counts of gender types:\n', gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
      print('Users birth Year info doesn\'t exist')
    else:
      earliest_year = df['Birth Year'].min()
      recent_year = df['Birth Year'].max()
      most_common_year = df['Birth Year'].mode()[0]
      print('Earliest year of birth: ', earliest_year, '\nMost recent year of birth: ', recent_year, '\nMost common year of birth: ', most_common_year )
      print("\nThis took %s seconds." % (time.time() - start_time))
      print('-'*40)


def raw_data(city):
    request = input('Would you like to see users raw data? Enter yes or no.\n').lower()
    df = pd.read_csv(CITY_DATA[city])
    x = 0
    y = 5
    if request == 'yes':
        print(df.iloc[x:y])
        request_more = input('Would you like to see more data? Enter yes or no.\n').lower()
        while request_more == 'yes':
            x += 5
            y += 5
            print(df.iloc[x:y])
            request_more = input('Would you like to see more data? Enter yes or no.\n').lower()
            if request_more == 'no':
                break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
