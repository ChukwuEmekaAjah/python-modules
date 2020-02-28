from flask import Flask,  Response, request

from datetime import datetime
import json
import random 

app = Flask(__name__)

shortened_urls = {} # dictionary for holding shortened links
short_url_seeds = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
'p','q','r','s','t','u','v','w','x','y','z','A','B','C','E','F','G','H','I','J',
'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9'] # seed for creating short links

number_of_shortlink_characters = 5 # length of characters required for a short link

@app.route('/')
def home():
	return "Welcome to my URL Shortener API"

@app.route('/create', methods=['POST'])
def create():
	"""
		This route is for creating a short URL link
		It returns a JSON object of the short link to a URL sent in as request
	"""
	global short_url_seeds 
	global shortened_urls 
	global number_of_shortlink_characters
	request_body = dict(request.get_json())
	if not request_body.get('url'):
		return json.dumps({"message":"Invalid request body. Provide URL to shorten", "error":"true"})
	document_body = dict()
	document_body['url'] = request_body.get('url')
	document_body['creation_date'] = str(datetime.utcnow())
	short_url = ''.join([short_url_seeds[i] for i in range(number_of_shortlink_characters)])
	while shortened_urls.get(short_url):
		short_url = ''.join([random.choice(short_url_seeds) for i in range(number_of_shortlink_characters)])
	document_body['short_url'] = short_url 
	document_body['number_of_clicks'] = 0
	shortened_urls[short_url] = document_body
	return Response(json.dumps(document_body),mimetype="application/json")

@app.route('/links', methods=['GET'])
def get_links():
	"""
		This returns a list of all the shortened URLs on the platform. 
		If there are no shortened links on the platform, it returns an empty list
	"""
	global shortened_urls
	links = []
	for key,value in shortened_urls.items():
		links.append(value)
	return Response(json.dumps(links), mimetype="application/json")

@app.route('/links/<short_link>', methods=['GET'])
def get_link(short_link):
	"""
		This returns a specific shortened link on the platform or returns an error message.
	"""
	global shortened_urls
	if shortened_urls.get(short_link):
		return Response(json.dumps(shortened_urls.get(short_link)), "application/json")
	return Response(json.dumps({"message":"Provided short link does not exist. Please check and try again", "error":"true"}))


if __name__ == '__main__':
	app.run(debug=True)
