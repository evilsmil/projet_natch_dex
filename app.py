import streamlit as st
from PIL import Image


def main():

    st.set_page_config(
    page_title="Hello",
    page_icon="👋",)
    
    st.title(" NATCH-DEX ")

    

    im = Image.open("img.jpg")
    st.write(im)






if __name__=="__main__":
    main()