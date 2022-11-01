from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/test')
def test():
    return 'SUIIII.><>?><?><<>>>>'

