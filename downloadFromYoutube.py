from pytube import YouTube
#author : eamalindu
# Ask the user for the video URL
url = input("Enter the video URL: ")

# Create a YouTube object
yt = YouTube(url)

# Print the video title and available streams
print("Title:", yt.title)
print("Available streams:")
for stream in yt.streams.filter(progressive=True):
    print(stream, '(', round(stream.filesize/1024/1024, 2), 'MB)')

# Ask the user for the stream to download
itag = input("Enter the itag of the stream to download: ")
print("Download started!")
# Download the video
stream = yt.streams.get_by_itag(itag)
stream.download(output_path='Youtube Videos')
print("******Download finished!\nVideo saved to Youtube Videos folder*******")