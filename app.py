import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()  
API_KEY = os.getenv('NBA_API_KEY')

# Function to get NBA data
def get_nba_data():  
    url = 'https://api.nba.com/stats/players/'  # Example NBA API URL
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(url, headers=headers)
    return response.json()

# Streamlit application
st.title('NBA Player and Team Statistics')

if st.button('Load NBA Data'):  
    data = get_nba_data()  
    st.write(data)  
else:
    st.write('Click the button to load NBA data.')