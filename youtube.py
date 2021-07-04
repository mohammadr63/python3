# You must first install pytube
# sudo apt-get install pip3
# pip3 install pytube

from pytube import YouTube 
# Select the video you want, right-click on the video and click copy url
url1 = input('please enter url for video : >> ')
# And you run in the terminal
python_youtube = pytube.Youtube(url1)

video = python_youtube.streams.first()

video.download('video.mp4')

