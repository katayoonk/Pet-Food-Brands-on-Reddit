import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
# tab1.write("this is tab 1")
# tab2.write("this is tab 2")
# with open( "streamlit\style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.set_page_config(
    page_title="CatDog",
    page_icon="imgs/images (1).jfif",
    layout="wide",
    initial_sidebar_state="expanded",
)
# with st.sidebar:
#     choose = option_menu("Pages", ["About", "Methodology", "Insights", "Make predictions"],
#                          icons=['info-circle', 'terminal', 'clipboard-data','robot'],
#                          menu_icon="text-left", 
#                          default_index=0,
#                          styles={
#         "container": {"padding": "5!important", "background-color": "#fafafa"},
#         "icon": {"color": "#EFE3F6", "font-size": "20px"}, 
#         "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "#EFE3F6"},
#     }
#     )
page = st.sidebar.radio(
    'Page',
    ('About', 'Approach', 'Insights' 'Make a prediction')
)

if page == 'About':
    st.subheader('About this project')
    st. markdown(
        """
        **:red[As a pet owner, have you ever wondered what other pet owners think about the different pet food brands available on the market?
        Are you curious about the most commonly discussed brands and the overall sentiment around them?]**
        """
        )
    
    st.markdown(
        """
        This project aimed to answer these questions by analyzing posts from the r/Cats and r/Dogs subreddits using Natural Language Processing (NLP) techniques.\n
        In this app, I will share my key findings and insights that can benefit both pet owners and pet food manufacturers.
        """
    )
    st.markdown(
        "**So, let's dive in and discover what the online pet community has to say about their furry friends' food!**"
    )

#     st.write('''
# As a pet owner, have you ever wondered what other pet owners think about the different pet food brands available on the market?\n
# Are you curious about the most commonly discussed brands and the overall sentiment around them?\n 
# This project aimed to answer these questions by analyzing posts from the r/Cats and r/Dogs subreddits 
# using Natural Language Processing (NLP) techniques. 
# In this app, I will share my key findings and insights that can benefit both pet owners and pet food manufacturers. 
# So, let's dive in and discover what the online pet community has to say about their furry friends' food!
#     ''')

    st.write('Use the sidebar to select a page to view.')
elif page == 'Aproach':
    # header
    st.subheader('Exploratory Data Analysis')
    st.write('''The model is trained on paragraphs.
    
Below you can find....''')
    

elif page == 'Make a prediction':
    
    st.title('Which subreddit your text came from?')

    # Read in my model
    with open('data/subreddit_classification.pkl', 'rb') as f:
        model = pickle.load(f)

    text = st.text_area("Please enter some text:", max_chars = 1000)
    text = pd.Series(text)

    # Save predicted subreddit

    predicted_subreddit = model.predict(text)[0]

    if st.button("Submit"):
        if len(text) > 0:
            if predicted_subreddit == 'dogs':
                st.write(f"This is from r/dogs!")
                st.image('imgs/big-fluffy-dog-breeds-1659335104.jpg')

            if predicted_subreddit == 'cats':
                st.write(f"This is from r/cats!")
                st.image('imgs/domestic-cat-lies-in-a-basket-with-a-knitted-royalty-free-image-1592337336.jpg')

        else:
            st.error("Please write some text to generate prediction!")

    