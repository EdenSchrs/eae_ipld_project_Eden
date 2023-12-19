import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="<Your Name> Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write("###")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:** <Your Name>")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Eden</h1></div>""", unsafe_allow_html=True)


# ----- Profile image file -----
profile_image_file_path = "profile_image.jpg"

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Big Data Master Student"   

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

st.write("""
- 🧑‍💻 I am a Big Data Master Student in Barcelona

- 🛩️ Coming from an international educational background, I excel in multicultural environments. I have lived in 8 countries growing up, spanning 3 continents. My Bachelor studies was in International Management with a specialization in Digital Marketing. All my work experience has been in different cities which include roles in sales and marketing as well as web development.

- ❤️ I am passionate about all things organization, reading and self-help. 

- 🤖 Currently I am working on finding job opportunities abroad and in Barcelona. On the side, I am interested in reaching out to creators online to see what I can learn from helping them.

- 🏂 I love to play volleyball and occasionally I run as well. 

- 📫 How to reach me: eden.schreurs@gmail.com

- 🏠 Barcelona
""")

# Feel free to add other points like your Linkedin, Github, Social Media, etc.
