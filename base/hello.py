import base64
print("helloworld")
str = 'you_are_beautiful'
print(base64.b64encode(bytes(str,'utf-8')))
ba = 'eW91X2FyZV9iZWF1dGlmdWw=' #base64.b64encode(bytes(str,'utf-8'))
print(base64.b64decode(ba))
print("fuck")