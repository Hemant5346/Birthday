import streamlit as st
from datetime import datetime

# App title with a subtle emoji
st.title('Happy Birthday, Nepoznadevic!')

# Current date
today = datetime.now().date()

# Birthday message as today is the birthday
st.header("🎉 Today is Your Special Day!")


# Show a professional birthday message
st.subheader("Wishing you a fantastic day filled with all your favorite things.")

# Button to display balloons for a bit of celebratory fun
if st.button('Click to Celebrate!'):
    st.balloons()
