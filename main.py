import os

from fastapi import FastAPI, Body, HTTPException, Header
from starlette import status

from database import Database

db = Database(os.environ.get("DB_URL"))
token = os.environ.get("TOKEN")

app = FastAPI()


@app.post('/')
def main(query: str = Body(), authorization=Header(default=None)):
    if authorization is None or authorization != token:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str("not valid token"))

    query = query.strip("\n\t\r ")
    try:
        return db.execute(query)
    except Exception as ex:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))
