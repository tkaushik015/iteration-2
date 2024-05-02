import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
@st.cache
def load_bowling_data():
    return pd.read_csv('2023_bowling.csv')

@st.cache
def load_batting_data():
    return pd.read_csv('2023_batting.csv')

bowling_df = load_bowling_data()
batting_df = load_batting_data()

# Sidebar filters
st.sidebar.header('Filters')
analysis_option = st.sidebar.selectbox('Analysis Option', ['Bowling Stats', 'Batting Stats'])

# Function to filter bowling data
def filter_bowling_data(df):
    country = st.sidebar.text_input('Country')
    if country:
        df = df[df['Country'].str.contains(country, case=False)]
    return df

# Function to filter batting data
def filter_batting_data(df):
    country = st.sidebar.text_input('Country')
    if country:
        df = df[df['Country'].str.contains(country, case=False)]
    return df

if st.sidebar.button('Submit'):
    if analysis_option == 'Bowling Stats':
        filtered_bowling_df = filter_bowling_data(bowling_df)
        st.write(filtered_bowling_df)

        # Visualizations and Insights for Bowling Stats
        st.subheader('Bowling Statistics Visualizations and Insights')

        # Summary statistics
        st.write("Summary Statistics:")
        st.write(filtered_bowling_df.describe())

        # Distribution of Wickets
        st.write("Distribution of Wickets:")
        fig, ax = plt.subplots()
        sns.histplot(filtered_bowling_df['Wickets'], kde=True, ax=ax)
        ax.set_xlabel('Wickets')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_batting_data(batting_df)
        st.write(filtered_batting_df)

        # Visualizations and Insights for Batting Stats
        st.subheader('Batting Statistics Visualizations and Insights')

        # Summary statistics
        st.write("Summary Statistics:")
        st.write(filtered_batting_df.describe())

        # Distribution of Strike Rate
        st.write("Distribution of Strike Rate:")
        fig, ax = plt.subplots()
        sns.histplot(filtered_batting_df['Strike_rate'], kde=True, ax=ax)
        ax.set_xlabel('Strike Rate')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

else:
    if analysis_option == 'Bowling Stats':
        st.write(bowling_df)
    elif analysis_option == 'Batting Stats':
        st.write(batting_df)
