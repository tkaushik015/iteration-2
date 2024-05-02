import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_bowling_data():
    return pd.read_csv('2023_bowling.csv')

@st.cache
def load_batting_data():
    return pd.read_csv('2023_batting.csv')

bowling_df = load_bowling_data()
batting_df = load_batting_data()

# Get unique countries from both datasets
bowling_countries = bowling_df['Country'].unique()
batting_countries = batting_df['Country'].unique()
countries = sorted(set(bowling_countries).union(set(batting_countries)))

# Sidebar filters
st.sidebar.header('Filters')
analysis_option = st.sidebar.selectbox('Analysis Option', ['Bowling Stats', 'Batting Stats'])
selected_country = st.sidebar.selectbox('Select Country', ['All'] + countries)

# Function to filter bowling data
def filter_bowling_data(df, country):
    if country != 'All':
        df = df[df['Country'] == country]
    return df

# Function to filter batting data
def filter_batting_data(df, country):
    if country != 'All':
        df = df[df['Country'] == country]
    return df

if st.sidebar.button('Submit'):
    if analysis_option == 'Bowling Stats':
        filtered_bowling_df = filter_bowling_data(bowling_df, selected_country)
        st.write(filtered_bowling_df)
    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_batting_data(batting_df, selected_country)
        st.write(filtered_batting_df)
else:
    if analysis_option == 'Bowling Stats':
        st.write(bowling_df)
    elif analysis_option == 'Batting Stats':
        st.write(batting_df)
