# TP0 - Web app

## Run locally (port 8080)

#### 1. Install the app
```bash
make install
```

#### 2. Run
```bash
make run
```

## Endpoints
#### - Get books list
```bash
curl -XGET http://localhost:8080/v1/books?search=WORDS+TO+SEARCH
```

#### - Get book detail
```bash
curl -XGET http://localhost:8080/v1/books/:BOOK_ID
```
