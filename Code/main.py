import streamlit as st

# set the title

st.title('Pothole Detection using YOLO v7')
st.subheader(" Deteksi jalan berlubang dengan menggunakan YOLO V7")

st.text(" Silahkan masukkan video yang akan di scan")


# Create file uploader
video_file = st.file_uploader("Upload MP4 video", type=["mp4"])

# Check if file was uploaded
if video_file is not None:
    # Read file contents
    video_bytes = video_file.read()

    # Display video player
    st.video(video_bytes)

# Save file
with open("vid_1.mp4", "wb") as f:
    f.write(video_bytes)
    st.success("File saved")

st.subheader("Scanning pothole")
