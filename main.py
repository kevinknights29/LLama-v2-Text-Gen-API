from __future__ import annotations

from flask import Flask

from src.llm import text_generation

app = Flask(__name__)


@app.get("/generate-text/<string:prompt>")
def generate_text(prompt):
    result = text_generation.text_generation(prompt)
    return {"result": result}
