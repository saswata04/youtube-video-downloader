from pytube import YouTube as yt
import datetime as dt

# Video Link
url = 'https://www.youtube.com/watch?v=IDj_SBw3C_E'

# YouTube Object
myVideo = yt(url)

# title of the video
print('TITLE:', myVideo.title)

# length of the video in sec
sec = myVideo.length
videoLength = dt.timedelta(seconds=sec)
print('VIDEO LENGTH:', videoLength)

# URL for the video thumbnail pic
print('THUMBNAIL URL:', myVideo.thumbnail_url)

# description of the video
print('DESCRIPTION:', myVideo.description, sep='\n')

# no. of the video has been viewed
print('VIEWS:', myVideo.views)

# average rating of the video
print('RATING:', myVideo.rating)

# check if the video has age restrictions
print('IS AGE RESTRICTED:', myVideo.age_restricted)

# ID of the video, present at the end of the video URL
print('VIDEO ID:', myVideo.video_id)

# get StreamQuery object from YouTube object
# get list of all available streams for the video
myVideoStreams = myVideo.streams
print('STREAMS:', myVideoStreams, sep='\n')

# access first and last stream from myVideoStreams list
videoStream = myVideoStreams.first()
audioStream = myVideoStreams.last()
print('VIDEO STREAM:', videoStream)
print('AUDIO STREAM:', audioStream)

# download the video in videos folder
# videoStream.download('videos/')

# filter streams wrt properties
videoStreams1080p = myVideoStreams.filter(res='1080p', file_extension='mp4')
audioStreams160kbps = myVideoStreams.filter(type='audio', abr='160kbps')
print('1080p VIDEO STREAMS:', videoStreams1080p, '160kbps AUDIO STREAMS:', audioStreams160kbps, sep='\n')

# videoStreams1080p.first().download('videos/')
audioStreams160kbps.first().download('audios/')



