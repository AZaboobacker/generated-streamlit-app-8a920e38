# Required Libraries
import streamlit as st
import openai
import requests
from geopy.geocoders import Nominatim

# Retrieve User Location
def get_location(user_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(user_address)
    return location

# OpenAI API Request
def openai_request(openai_key, user_query):
    openai.api_key = openai_key
    response = openai.chat.completions.create(
        model='gpt-4', 
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'}, 
            {'role': 'user', 'content': f'list indoor tennis courts near {user_query}'}
        ])
    message_content = response.choices[0].message.content.strip()
    return message_content

# Interface
def main():
    st.title('Indoor Tennis Courts Locator')
    st.image('tennis_icon.png') # put path of your tennis icon image
    user_address = st.text_input("Enter your address", "")
    openai_key = st.text_input("Enter your OpenAI API Key", "")
    if st.button("Find Tennis Courts"):
        if user_address and openai_key:
            user_location = get_location(user_address)
            tennis_courts_info = openai_request(openai_key, user_location)
            st.markdown(f'**Tennis Courts Near You:** {tennis_courts_info}')
        else:
            st.error("Make sure you filled all the fields.")
            
if __name__ == '__main__':
    main()