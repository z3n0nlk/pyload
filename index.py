from flask import Flask
import requests
app = Flask(__name__)


@app.route('/')
def hello():
	link = "https://sinhalastorylk.blogspot.com/2020/11/blog-post.html"
	headers = {
		'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
		'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
	}
	for x in range(10):
		requests.get(link, headers=headers)
   	return "Hello World!"

if __name__ == '__main__':
    app.run()



