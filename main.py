from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from schemas import PostCreate, PostResponse

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

@app.get("/api/post", response_model=list[PostResponse], name="posts")
def getList():
    return posts

@app.post("/api/posts", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    new_id = max(p["id"] for p in posts) + 1 if posts else 1
    new_post = {
        "id":new_id,
        "author":post.author,
        "title":post.title,
        "content":post.content,
        "date_posted":"April 23, 2026"
    }
    posts.append(new_post)
    return new_post

@app.get("/api/posts/{post_id}", response_model=PostResponse, name="post")
def getPost(post_id:int):
    for post in posts:
        if post.get("id") == post_id:
            return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")