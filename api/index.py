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
try:
    with open('marks.json', 'r') as f:
        marks_data = json.load(f)
    print("Data loaded successfully:", marks_data)  # Debug statement
except Exception as e:
    print("Error loading JSON:", e)

@app.get("/api")
def get_marks(request: Request):
    names = request.query_params.getlist('name')
    print("Received names:", names)  # Debug statement
    marks_list = []

    for name in names:
        mark_entry = next((item for item in marks_data if item["name"].lower() == name.lower()), None)
        if mark_entry:
            print(f"Found {name}: {mark_entry['marks']}")  # Debug statement
            marks_list.append(mark_entry["marks"])
        else:
            print(f"{name} not found in data.")  # Debug statement
            marks_list.append(None)

    return {"marks": marks_list}
