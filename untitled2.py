
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Content Ideator", page_icon="🧠")
st.title("🧠 AI Content Ideator")
st.caption("Generate viral content ideas, hooks, and captions instantly.")

# Configure Gemini API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

topic = st.text_input("Enter your niche or theme (e.g. AI, self-growth, finance):")

if st.button("Generate Ideas"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        prompt = f"Generate 3 unique content ideas, 3 hooks, and 3 captions for the niche '{topic}'. Make them sound human, engaging, and viral-worthy."
        
        # ✅ Use the correct model name available to you
        model = genai.GenerativeModel("gemini-1.5-flash")

        try:
            response = model.generate_content(prompt)
            st.subheader("Generated Ideas:")
            st.write(response.text)
        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
