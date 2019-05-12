import requests

resp = requests.get('http://127.0.0.1:5000/')

song_state = eval(resp.content)
for idx, mute_value in enumerate(song_state):
	print(idx)
	print(mute_value)
