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
    if response.status_code == 200:
        return responseParser.parse_books_list(response.content)
    
    return response.content, response.status_code

@app.route("/v1/books/<id>", methods = ['GET'])
def getBookInfo(id):
    response = requests.get(BOOKS_API_URLBASE + 'volumes/' + id)
    if response.status_code == 200:
        return responseParser.parse_book_detail(response.content)
    
    return response.content, response.status_code
    
if __name__ == "__main__":
    app.run(port=8080)