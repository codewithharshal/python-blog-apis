from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

posts: list[dict] = [
    {
        "id":1,
        "author":"Corey Schafer",
        "title":"FastAPI is Awesome",
        "content":"This framewrok is really easy to use and super fast",
        "data_posted":"April 20, 2025",
    },
    {
        "id":2,
        "author":"Corey Schafer",
        "title":"FastAPI is Awesome",
        "content":"This framewrok is really easy to use and super fast",
        "data_posted":"April 20, 2025",
    },
]


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]["title"]}</h1>"

@app.get("/list")
def getList():
    return posts