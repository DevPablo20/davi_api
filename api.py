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

# creating a get method that it can search for an card_id with a description and a default value (None)
@app.get("/get-item/{card-id}")
def get_item(card_id: int = Path(None, description="The Id of the item you want to view")):
    return users_ids[card_id]

# creating a get method that searches for all the person's cards.
@app.get("/get-by-cpf/{cpf}")
def get_item(cpf: str = Path(None, description="The CPF of the person you want to view")):
    person_cards = {}
    for ids in users_ids:
        if users_ids[ids]['cpf'] == cpf:
            person_cards[ids] = users_ids[ids]
    if person_cards != None:
        return person_cards
    else:
        return {"Data": "Not found"}

#












# cmd to run the api:
# # C:\Users\pablo\PycharmProjects\davi_api\davi_api> uvicorn api:app --reload










