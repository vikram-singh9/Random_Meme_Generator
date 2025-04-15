import streamlit as st
import requests

st.title("😁 Random Meme generator 😂")
st.subheader("It's simple meme generator for fun fetches meme from the real time API.")

if st.button("Generate meme"):

    try:
        response = requests.get("https://meme-api.com/gimme")
        if response.status_code == 200:
            data = response.json()
            result = data["url"]
            a = data["author"]
            st.image(result, caption="funny😂", width=500)
            st.write(a)
        elif response.status_code != 200:
            st.error("error fetching memes")
            
    
    except:
        st.write("api not fetcing data from the backend")
    