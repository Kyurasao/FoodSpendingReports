import sqlite3
import sys

import uvicorn
from fastapi import FastAPI

DB = 'request_db.db'
# con = sqlite3.connect(DB)
global con

app = FastAPI()


# running = True

# def stop_server(*args):
#     global running
#     running = False

@app.on_event("startup")
def startup_event():
    print("startup!")
    con = sqlite3.connect(DB)
    # signal.signal(signal.SIGINT, stop_server)


@app.on_event("shutdown")
def shutdown_event():
    print("shutdown!")
#     global running
#     running = False
    con.close()


@app.get('/')
async def root():
    # while running:
    #     await asyncio.sleep(0.1)
    return {"message": "THIS IS TEST WEB SERVER!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    sys.exit(0)
