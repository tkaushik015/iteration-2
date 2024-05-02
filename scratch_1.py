import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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

        # Visualizations for Bowling Stats
        st.subheader('Bowling Statistics Visualizations')

        # Bar plot of Wickets by Country
        st.write("Bar plot of Wickets by Country:")
        wickets_by_country = filtered_bowling_df.groupby("Country")["Wickets"].sum()
        st.bar_chart(wickets_by_country)

        # Heatmap of Correlation Matrix
        st.write("Heatmap of Correlation Matrix:")
        corr_matrix = filtered_bowling_df.corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
        st.pyplot()

    elif analysis_option == 'Batting Stats':
        filtered_batting_df = filter_batting_data(batting_df)
        st.write(filtered_batting_df)

        # Visualizations for Batting Stats
        st.subheader('Batting Statistics Visualizations')

        # Pie chart of Hundred's distribution by Country
        st.write("Pie chart of Hundred's distribution by Country:")
        hundreds_by_country = filtered_batting_df.groupby("Country")["Hundreds"].sum()
        st.write(hundreds_by_country)
        fig, ax = plt.subplots()
        ax.pie(hundreds_by_country, labels=hundreds_by_country.index, autopct='%1.1f%%')
        st.pyplot(fig)

        # Scatter plot of Strike Rate vs Fifties
        st.write("Scatter plot of Strike Rate vs Fifties:")
        plt.figure(figsize=(8, 6))
        plt.scatter(filtered_batting_df["Strike_rate"], filtered_batting_df["Fifties"], alpha=0.5)
        plt.xlabel("Strike Rate")
        plt.ylabel("Fifties")
        st.pyplot()

else:
    if analysis_option == 'Bowling Stats':
        st.write(bowling_df)

    elif analysis_option == 'Batting Stats':
        st.write(batting_df)
