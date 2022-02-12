# importing libraries
import json
from fastapi import FastAPI, Path

# creating an api object
app = FastAPI()

# importing the new JSON file:
with open('output_card.json') as jsonfile:
    users_ids = json.load(jsonfile)
    jsonfile.close()

print(users_ids)

# creating endpoints '/'
@app.get("/") #localhost/
def home():
    return {"Data": "Testing"}

@app.get("/about")
def about():
    return{"Data": "About"}

# creating a get method that it can search for an user_id with a description and a default value (None)
@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None, description="The Id of the item you want to view")):
    return users_ids[item_id]

# creating query method that searches for a person using his/her cpf
@app.get("/get-by-name")
def get_item(cpf: str):
    for ids in users_ids:
        if users_ids[ids]['cpf'] == cpf:
            return users_ids[ids]
        return {"Data": "Not found"}










# cmd to run the api:
# # C:\Users\pablo\PycharmProjects\davi_api\davi_api> uvicorn api:app --reload










