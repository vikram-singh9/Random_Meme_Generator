import streamlit as st
import requests

st.title("😁 Random Meme generator 😂")
st.markdown("Realtime Random meme generator👀")
st.write("------")

if st.button("Generate meme"):
    try:
        response = requests.get("https://meme-api.com/gimme")
        if response.status_code == 200:
            data = response.json()
            result = data["url"]
            sub = data["title"]
            st.subheader(sub)
            st.image(result, caption="funny😂", use_container_width=True)
           
        elif response.status_code != 200:
            st.error("error fetching memes")
    except:
        st.write("api not fetcing data from the backend")
    