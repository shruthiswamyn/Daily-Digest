import streamlit as st
import os

st.set_page_config(
    page_title="Sarvagna: Your Daily Digest",
    page_icon="🎧",
    layout="wide"
)

# ✅ Show only the banner image
banner_path = os.path.join(os.path.dirname(__file__), "banner.png")
st.image(banner_path, width=1500)

# ✅ Author credit below banner
st.markdown(
    """
    <div style="text-align:center; margin-top:15px; padding:12px; 
                background-color:#E0F2FE; border-radius:10px; color:#0369A1; font-size:18px;">
        👩‍💻 Developed by <b>Shruthi</b>
    </div>
    """,
    unsafe_allow_html=True
)

# ✅ Episodes section (no repeated title/description)
outputs_dir = os.path.join(os.getcwd(), "outputs")
files = sorted([f for f in os.listdir(outputs_dir) if f.endswith(".wav")])

if not files:
    st.warning("No audio files found in outputs/")
else:
    st.subheader("📚 Episodes")
    cols = st.columns(2)
    for i, f in enumerate(files):
        with cols[i % 2]:
            st.markdown(f"### 🎧 {f.replace('.wav','')}")
            audio_bytes = open(os.path.join(outputs_dir, f), "rb").read()
            st.audio(audio_bytes, format="audio/wav")
            st.markdown("---")
