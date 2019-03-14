import json

BOOKS_LIST_VI_KEYS = ['title', 'authors', 'categories', 'description', 'imageLinks']

def parse_books_list(books_list_response):
    books_list_response = json.loads(books_list_response)
    items = []
    if books_list_response['totalItems'] > 0:
        for item in books_list_response['items']:
            book = { key: item['volumeInfo'][key] for key in BOOKS_LIST_VI_KEYS if key in item['volumeInfo'] }
            book['id'] = item['id']
            if 'epub' in item['accessInfo']:
                book['epub'] = item['accessInfo']['epub']
            if 'pdf' in item['accessInfo']:
                book['pdf'] = item['accessInfo']['pdf']
            items.append(book)
    items = sorted(items, key=lambda k: k['title'])
    return json.dumps(items)
    
# TODO
def parse_book_detail(book_detail):
    book_detail = json.loads(book_detail)
    book = {}
    return json.dumps(book)