import streamlit as st
from shots import shotPosts
from post_generator import generate_post

length_opt= ["Short","Medium","Long"]
language_opt=["English", "Arabic"]

def main():
    st.title("LinkedIn Post Generator")
    col1,col2,col3=st.columns(3)
    fs=shotPosts()
    with col1:
        selected_tags=st.selectbox("Title", options=fs.get_tags())
    with col2:
        selected_length=st.selectbox("Length", options=length_opt)
    with col3:
        selected_language=st.selectbox("Language",options=language_opt)
    if st.button("Generate"):
        post=generate_post(selected_length,selected_language,selected_tags)
        st.write(post)


if __name__ =="__main__":
    main()
