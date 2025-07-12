import streamlit as st  
import pandas as pd 
import matplotlib.pyplot as plt

# st.title("welcome to my app")
# st.header("This is a header")
# st.subheader("This is a subheader")
# a = st.text_input("Enter your name:")
# st.write(f"Hello, {a}!")
# st.text_area("Enter your message:")
# age = st.number_input("Enter your age:", min_value=0, max_value=60)
# st.write(f"You are {age} years old.")
# st.button("Submit")
# st.write("Thank you for using the app!")#paragraph type
# k = st.slider("Select a value:", 0, 100, 50)
# st.write(f"You selected: {k}")
# st.checkbox("Check me!")
# st.write("This is a checkbox.")
# st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
# st.write("This is a radio button.")
# st.image("kiki.jpeg", caption="Sample Image")
# # st.video("h.mp4", caption="Sample Video")
# # st.audio("sample_audio.mp3", format="audio/mp3", caption="Sample Audio")

# df = pd.DataFrame({
#     "name": ["Alice", "Bob", "Charlie"],
#     "age": [25, 30, 35],
#     "city": ["New York", "Los Angeles", "Chicago"]
# })
# st.write("DataFrame Example:")
# st.dataframe(df)
# st.table(df)  # Display as a static table
# df2 = pd.DataFrame({
#     "x": [1, 2, 3],
#     "y": [4, 5, 6],
# })
# st.line_chart(df2)  # Display as a line chart
# st.bar_chart(df2)  # Display as a bar chart
# st.area_chart(df2)  # Display as an area chart

# fig, ax = plt.subplots()    
# ax.plot(df2['x'], df2['y'])
# st.pyplot(fig)  # Display the matplotlib figure

# lets create a simple form
with st.form("my_form"):
    st.text_input("Enter your name:")
    st.number_input("Enter your age:", min_value=0, max_value=100)
    st.text_area("Enter your message:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Form submitted successfully!")
