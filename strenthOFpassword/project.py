import streamlit as st
import requests
import re

URL = "https://b38e5f3f3b58.ngrok-free.app/check-password"
headers = {"Authorization": "Bearer secret123"}

# --- Helper function to clean strength ---
def clean_strength(text: str) -> str:
    # نحاول نلقط Weak أو Medium أو Strong من ال output
    match = re.search(r"\b(Weak|Medium|Strong)\b", text, re.IGNORECASE)
    if match:
        return match.group(1).capitalize()
    return text.strip()

# --- Helper function to clean explanation ---
def clean_explanation(text: str) -> str:
   
    lines = text.strip().split(". ")
    if len(lines) > 1:
        return ". ".join(lines[-2:])  
    return text.strip()

# Title
st.title("🔐 Password Strength Checker")

# Sidebar for parameters
st.sidebar.header("Settings")
temperature = st.sidebar.slider("Temperature (controls creativity)", 0.0, 1.5, 0.7)
top_p = st.sidebar.slider("Top-p (controls randomness)", 0.0, 1.0, 0.9)

# Input
password = st.text_input("Enter your password:")

if st.button("Check Password"):
    if password:
        payload = {
            "password": password,
            "temperature": temperature,
            "top_p": top_p
        }
        response = requests.post(URL, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()

            raw_strength = result.get("strength", "")
            raw_explanation = result.get("explanation", "")
            breach = result.get("breach", "").strip()

            
            strength = clean_strength(raw_strength)
            explanation = clean_explanation(raw_explanation)

            
            st.subheader("Result")
            st.markdown(f"**Password Strength:** 🟢 {strength}")
            st.markdown(f"**Explanation:** {explanation}")

            if "NOT found" in breach:
                st.success(breach)
            else:
                st.error(breach)

        else:
            st.error(f"Request failed: {response.status_code}")
    else:
        st.warning("⚠️ Please enter a password")
