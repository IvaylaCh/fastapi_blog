from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app=FastAPI()

post: list[dict]=[
    {
        "id":1,
        "author": "mimi",
        "title": "for mice and man",
    },
    {
        "id":2,
        "author": "lili",
        "title": "children's tale",
    },
]

@app.get("/", response_class=HTMLResponse)
def home():
    return f"<h1>{post[0]['title']}</h1>"
@app.get("/api/posts")
def get_posts():
    return post