import folium
import pandas as pd
import streamlit as st
import base64
from streamlit_folium import folium_static
from bokeh.models.widgets import Div
from geopy.distance import geodesic
from PIL import Image,ImageOps

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()}) ;
        background-repeat: no-repeat;
        background-size: 100%;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

def header1(url):
     st.markdown(f'<p style="color:red;font-size:36px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

def headermsg(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:36px;">{url}</p>', unsafe_allow_html=True)


st.set_page_config(page_title="SNS", layout="wide")


# Read the audio file as binary
audio_file = open('media/Miami_Beach_Sound.mp3', 'rb')
audio_bytes = audio_file.read()

# Encode the audio bytes using base64
audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')

# Generate the HTML audio tag
audio_tag = f'<audio src="data:audio/mp3;base64,{audio_base64}" autoplay controls></audio>'

# Apply CSS styling to the audio player
custom_css = """
<style>
audio {
    opacity: 0.2; /* Adjust transparency here */
}
</style>
"""

# Display the audio player and apply CSS
st.header("Play Miami Beach Sound (To Relax)")
st.markdown(custom_css, unsafe_allow_html=True)
st.markdown(audio_tag, unsafe_allow_html=True)

add_bg_from_local('media/Miami.png') 
    

header1("Chances (Probability) of Meeting SNS out of the blue 😅 Look at the Map closely")


df_world=pd.read_excel("Godevendoesntknows.xlsx")


# Get the latitude and longitude of the first point
start_point = (df_world['latitude'].iloc[0], df_world['longitude'].iloc[0])

# Create a map centered on the first location
map_center = start_point
map_zoom = 4
m = folium.Map(location=map_center, zoom_start=map_zoom)

# Add markers for all locations
for i, row in df_world.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['Loc']
    ).add_to(m)

# Add a polyline to connect the locations
polyline_points = [[row['latitude'], row['longitude']] for i, row in df_world.iterrows()]
polyline = folium.PolyLine(polyline_points, color='red').add_to(m)

# Calculate distances and add tooltips to the polyline
distances = [geodesic(polyline_points[i], start_point).km for i in range(len(polyline_points))]
# distances_tooltips = [f"Distance: {round(d, 2)} kms" for d in distances]
distances_tooltips=[]
for i, row in zip(df_world.iterrows(),distances):
    distances_tooltips.append(str(i[1]['Loc'])+" "+str(round(row,2))+" kms")

distances_tooltips[0]="SNS 👩🏻"
distance_p=distances_tooltips[-1]
distances_tooltips[-1]="Pabba's 🍧"+str(distance_p)

for i, tooltip in enumerate(distances_tooltips):
    folium.Marker(polyline_points[i], icon=folium.DivIcon(icon_size=(150, 36), html=f'<div style="font-size: 10pt; color: black;">{tooltip}</div>')).add_to(m)

# Add a polygon to form a triangle
polygon_points = polyline_points + [polyline_points[0]]
folium.Polygon(polygon_points, color='red', fill=True, fill_color='red').add_to(m)

make_map_responsive= """
 <style>
 [title~="st.iframe"] { width: 50%}
 </style>
"""
st.markdown(make_map_responsive, unsafe_allow_html=True)

# Display the map
folium_static(m)


headermsg("Probability Coincidence:")

image = Image.open('media/Probs.png')

st.image(image)

headermsg("""As you see the probabilities are low, but maybe God and fate brought us there. 😅 Call me eccentric, weird, or determined - that's for you to decide. 
I understand if you despise me; I've never been despised by anyone before other than my mother JK. 😅😂 I usually mind my own business and don't bother anyone.
I'm not sure if I deserve to know you or am the right guy. I know I'm not that bad, even though 'bad' is in my name. 😢
But once you get to know the funny, quirky, adventurous, and emotional side of me, I bet you'll never regret knowing me better or earlier.
You made me look inward and opened me up to my thoughts and expression. I don't usually open up like this, but on my way back to Boston from Miami, 
I spoke to a lady in her early 60s who was visiting her ailing mother. Her mom's story, at 80 years old, dating a 65-year-old man, shook me (long story). 
In my usual scenario, I would never open up, but I showed her your picture from Boston (sorry for invading your privacy). She told me you look like a doctor.
I jokingly said that you can't cure my disease though. JK :) I was really in a bad state mentally but the folks (Puerto Rican Aunt and a Colombian Family) 
on the flight (see pics below) cheered me. You also made me think outside the box and got my creative juices flowing, which I didn't know I had yet. 
I know you don't feel anything for me or have any interest in me. Sometimes intuitive feelings can be wrong. 
I don't have the luxury to know you in real-time. Time and feelings can change if you just give it a thought. It's perfectly fine with me.
I'm sorry for intimidating you with those 40+ calls in Miami. I know you're a strong woman, but I was also scared when you didn't pick up for your safety. 
I usually don't speak about myself ever because I don't care about it or because I know I'm the least self-obsessed person. 
Many consider me a nice guy and an gentleman; I don't know if you think the same of me. But there's a famous saying that nice guys finish last, and to some extent, it's true. 
However, I don't want to give up on this race. 😢 My friends know me as jovial, authentic, funny, knowledgeable, helpful, caring, adjusting, accommodating, overthinker, etc.
I've always tried to see the best in a person. You're smart, independent, straightforward, witty, funny, strong, bold, a risk-taker, diplomatic, calm, and understanding. 
It's very difficult to find someone like you. I know times are tough with jobs, responsibilities, and life in general. There are a lot of 'ifs.' 
But I guarantee one thing: this won't be an error. I don't know what impresses you. 
I am not the one to force anyone I just wanna be heard once and also for you get to know me as a person. I wanted to know your though process.
I just don't wanna lose someone good without you knowing where I come from and what it means to me. 
Your 1 in 7,900,000,000 (approximate world Population) chance might surpass the low probability mentioned above by a big margin. 
Even thought the probability of this chance seems even lower than the above estimated probability (In image) PS: Its from almighty ChatGPT. 
But it's an another effort nonetheless.
I apologize for everything and ask forgiveness If I said or done anything wrong before and now. 
I have been frank, authentic, genuine to what I feel and have done for you to the highest order possible from my side. 
I understand emotions quite well textually and in real. Your late reply to my messages. I could see you not wanting to see my face in Miami. 
The first Hi only made it evident for me. But still I had been fooling myself all along till now. If we had ever met again there and you would have known what I am. 
What I am not. I always wanted to make you feel special. I always felt I was misunderstood all along. Those misunderstandings would’ve been cleared. 
Those 2 months of getting to know you was really good phase for me. Sometimes doing the small things matter. I did everything I could for you from my side. 
I have to live with the fact that presumptions outweigh genuine efforts. I just wish you just knew me better because you would’ve never done this to me. 
I am not the one who usually calls anyone much. We both are the same boat being Data something in our careers and have a lot of commonalities but still a lot of differences. 
I felt like an Non Playable Character in Gods Game there (Miami). I put myself through a lot for this and everything till now. You made me show my reality and double question myself every moment from now on as I already used to question myself before.
I just wish we get to travel once together and you get to see the person I am and not what you assume me to be. I put you through a lot too unwarrantedly. 
I don’t want to be in that person ever to cause pain to you. I always want to see you do the best. 
I will try to never bother you. Also I know you might never even a feel a tinge of feeling for me. 
I am sorry for everything till now and ever.
Sorry. 🙏
""")


with open("media/Miami.png", "rb") as fp:
    btn = st.download_button(
        label="Download Beach Image (Background)",
        data=fp,
        file_name="Miami.png",
        mime="image/png"
    )

video_file = open('media/IMG_5655.mov', 'rb')
video_bytes = video_file.read()

if st.button('Play Special Credit Live Video captured by Apple 😂 (Sorry)'):
    st.video(video_bytes)

if st.button('(Disclaimer Allow Multiple Popups Refresh the page and check top right to allow) Stuck with this song on Spotify! 🎧 Especially the last lyrics to this song and also Cupid 💘, (3) Quotes: 🗒️ and an article I\'ve been wanting to write'):
    urls = ['https://www.youtube.com/watch?v=yv1UtpmBU8k', 'https://www.youtube.com/watch?v=Qc7_zRjH808' ,'https://quotecatalog.com/quote/paulo-coelho-when-you-want-s-D1jnWE1',\
    'https://quotecatalog.com/quote/paulo-coelho-when-we-love-w-g7OGAe7', 'https://quotecatalog.com/quote/hplyrikz-nice-guys-finis-V7Lrmxa',
    'https://grape-liquid-f37.notion.site/Nice-Guys-don-t-always-need-to-finish-Last-552c4ff41797417ba7ca1ba9a1242a1d']
    
    for url in urls:
        js = "window.open('{}')".format(url)  # Open each URL in a new tab or window
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)


# Load and transpose the first image
image1 = Image.open('media/IMG_7458.jpg')
image1 = ImageOps.exif_transpose(image1)

# Load and transpose the second image
image2 = Image.open('media/IMG_7453.jpg')
image2 = ImageOps.exif_transpose(image2)

# Load and transpose the third image
image3 = Image.open('media/IMG_7462.jpg')
image3 = ImageOps.exif_transpose(image3)

# Display the images side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.image(image1, use_column_width='never', width=400)

with col2:
    st.image(image2, use_column_width='never', width=400)

with col3:
    st.image(image3, use_column_width='never', width=400)





# Load and transpose the third image
imagefood = Image.open('media/IMG_5644.jpg')
imagefood = ImageOps.exif_transpose(imagefood)

headermsg("All the best!!! (Glow like the best pic below 😅 and hopefully you get to have some good Surmai Fry)")

# Display the images side by side
_, col2, _ = st.columns(3)
with col2:
    st.image(imagefood, use_column_width='never', width=400)










