from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks data from JSON
with open('marks.json', 'r') as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist('name')
    marks_list = []

    for name in names:
        mark_entry = next((item for item in marks_data if item["name"].lower() == name.lower()), None)
        if mark_entry:
            marks_list.append(mark_entry["marks"])
        else:
            marks_list.append(None)  # Return None if the name isn't found

    return {"marks": marks_list}
