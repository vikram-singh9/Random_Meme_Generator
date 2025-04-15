import streamlit as st
import requests

st.title("😁 Random Meme generator 😂")
st.markdown("""
    <h3 style='text-align: center; color: orange;'>
        Realtime Random meme generator 👀sddsddsdsd
    </h3>
""", unsafe_allow_html=True)

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

st.write("_____")
    
st.write("""
    <p style='text-align: center; color: orange;'>
        Built by Vikram
    </p>
""", unsafe_allow_html=True)
