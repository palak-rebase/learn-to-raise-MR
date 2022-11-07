import pafy

pafy.set_api_key('')

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)


video.title
video.viewcount, video.author, video.length

video.duration, video.likes, video.dislikes


video.published

