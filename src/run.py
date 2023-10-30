import streamlit as st 
import sys
from pathlib import Path
#personal data 
st.title('GIT HUB profile readme generator ')
st.header('Personal Info :new_moon_with_face:')
with st.expander('Personal Info'):
    col1, col2 = st.columns(2)
    name = col1.text_input('Name')
    email = col2.text_input('email')
    phone = st.text_input('phone')
    location = st.text_input('location')
st.title('Social Media')
with st.expander('social media'):
    st.markdown('just enter your username')
    col1,col2 = st.columns(2)
    github = col1.text_input('Github')
    email = col1.text_input('Email')
    linkedin = col2.text_input('Linkedin')
    instagram = col1.text_input('Instagram')
    youtube = col2.text_input('Youtube')
    facebook = col2.text_input('Facebook')

#slect themes
st.header ('themes')
with st.expander('theme'):
    themes = Path ('src/themes').iterdir() 
    themes= [theme.name for theme in themes]
    theme = st.selectbox('select theme',themes )
    st.markdown (f'selected theme:**{theme}**')

def generate_profile(theme , **kwargs):
    with open (f'src/themes/{theme}/profile.txt')as f :
        profile = f.read()
        for item, value in kwargs.items():
            with open (f'src/themes/{theme}/{item}.txt') as f:
                profile_item= f.read()

            profile_item = profile_item.replace(f'{value}',value)
            profile = profile.replace(f"{{item}}",profile_item)
        return profile


if __name__ == '__main__':
    name ='sadaf rad'
    email = "sadafismaeili@gmail.com"
    phone = "+316"
    location = "netherlands"

    github = " sadaf_rad"
    linkedin = " sadaf"
    instagram = "sadafrad"
    youtube="sadaf rad"
    facebook = "sadaf rad"
    theme = 'default'

    profile = generate_profile(theme ,name=name , email=email , linkedin = linkedin )
    print(profile)
    




    #generate readme
st.header('generate readme')
if st.button ('generate readme'):
    st.markdown('generating readme ...')
    profile = generate_profile(theme ,name=name , email=email , linkedin = linkedin )
    st.code(profile)

