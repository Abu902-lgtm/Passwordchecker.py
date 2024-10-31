# First, make sure you have Streamlit installed:
# pip install streamlit
pip install streamlit 

import streamlit as st
import re

# Define function to evaluate password strength
def assess_password_strength(password):
    # Initialize feedback and score
    feedback = []
    score = 0

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters for a stronger password.")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters for a stronger password.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers for a stronger password.")

    if re.search(r'[@$!%*?&#]', password):
        score += 1
    else:
        feedback.append("Add special characters (@, $, !, %, *, ?, &, #) for a stronger password.")

    # Determine strength based on score
    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong 👍"
    elif score == 3:
        strength = "Moderate 😐"
    elif score == 2:
        strength = "Weak 😕"
    else:
        strength = "Very Weak 😬"

    return strength, feedback

# Set up Streamlit app layout
st.title("🔒 Password Strength Checker")
st.write("Enter your password below to check its strength.")

# User password input
password = st.text_input("Password", type="password")

# Check password strength and provide feedback
if password:
    strength, feedback = assess_password_strength(password)
    st.markdown(f"**Password Strength:** {strength}")

    if feedback:
        st.subheader("Recommendations to Improve Strength:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
else:
    st.write("Please enter a password to assess its strength.")
