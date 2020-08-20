from urllib import request
req = request.Request("http://www.yhdm.tv/")
req.add_header("user-agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36 Edg/84.0.522.61")
resp = request.urlopen(req)
# resp = request.urlopen(req)
print(resp.read().decode("utf-8"))