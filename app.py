import streamlit as st
import pickle
import pandas as pd

# Load the model
with open('news_prediction.pkl', 'rb') as file:
    model = pickle.load(file)

# Set page configuration
st.set_page_config(page_title="ML Prediction App", page_icon=":bar_chart:", layout="centered")

# Custom CSS for font color and styling
st.markdown("""
    <style>
    /* Change the overall font color */
    body, .stMarkdown, .stTextInput, .stTextArea, .stSelectbox, .stFormSubmitButton {
        color: #0E1117;
        font-family: Arial, sans-serif;
    }

    /* Specific styling for headers and text */
    .stTitle, .stHeader {
        color: #FFA500; /* Orange color for main headers */
    }

    /* Stylish form input fields */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label {
        color: #a2161f; /* Spring Green for input labels */
    }

    /* Success and error message styling */
    .stAlert > div {
        color: #FFFFFF; /* White text for alerts */
        background-color: #4CAF50; /* Green background for success */
        border-radius: 8px;
    }

    .stError > div {
        color: #FFFFFF; /* White text for errors */
        background-color: #F44336; /* Red background for errors */
        border-radius: 8px;
    }

    /* Submit button style */
    .stButton button {
        background-color: #1E90FF; /* Dodger Blue button */
        color: #FFFFFF; /* White text */
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and introduction
st.title("📰 News Prediction App")
st.markdown("""
    <p style='color:#b2b2b2;'>Welcome to the ML Prediction App! Fill in the details below to get predictions based on our trained model. 
    Enjoy a sleek and user-friendly experience! </p>
    """, unsafe_allow_html=True)

# Form for user inputs
with st.form(key='prediction_form'):
    st.subheader("Enter the Details :")
    
    # Input fields
    id_input = st.text_input("🆔 ID", "")
    title_input = st.text_input("📘 Title", "")
    author_input = st.text_input("🖋️ Author", "")
    text_input = st.text_area("📝 Text", "")
    label_input = st.selectbox("🔖 Label", ["Option 1", "Option 2", "Option 3"])
    content_input = st.text_area("📄 Content", "")
    
    # Submit button
    submit_button = st.form_submit_button(label="Predict 🚀")

# Handle prediction after submission
if submit_button:
    if all([id_input, title_input, author_input, text_input, label_input, content_input]):
        # Organize input data into a DataFrame
        input_data = pd.DataFrame({
            'id': [id_input],
            'title': [title_input],
            'author': [author_input],
            'text': [text_input],
            'label': [label_input],
            'Content': [content_input]
        })
        
        # Predict using the loaded model
        prediction = model.predict(input_data)
        
        # Display prediction
        st.success(f"The predicted output is: {prediction[0]} 🎉")
        
    else:
        st.error("Please fill in all the fields before submitting.")

# Footer
st.markdown("---")
st.markdown("""
    <p style='color:#B0C4DE;'>Developed with ❤️ by <a href='https://yourwebsite.com' style='color:#00BFFF;'>Your Name</a></p>
    """, unsafe_allow_html=True)
