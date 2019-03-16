import requests
import responseParser
from flask import Flask
from flask import request

BOOKS_API_URLBASE = 'https://www.googleapis.com/books/v1/'

app = Flask(__name__)

@app.route("/v1/books", methods = ['GET'])
def searchBooks():
    search_words = request.args.get('search')
    querystring = str(search_words).replace(' ', '+')
    response = requests.get(BOOKS_API_URLBASE + 'volumes?q=' + querystring)
    response.raise_for_status()
    return responseParser.parse_books_list(response.content)

@app.route("/v1/books/<id>", methods = ['GET'])
def getBookInfo(id):
    response = requests.get(BOOKS_API_URLBASE + 'volumes/' + id)
    responseParser.parse_book_detail(response.content)
    return('TO_DO')

@app.after_request
def add_header(response):
    response.cache_control.max_age = 300
    return response
    
if __name__ == "__main__":
    app.run(port=8080)