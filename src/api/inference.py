from __future__ import annotations

from flask.views import MethodView
from flask_smorest import Blueprint

from src.llm import text_generation


blp = Blueprint(
    "Text Generation",
    __name__,
    url_prefix="/inference",
    description="Text Generation API",
)

blp.route("/generate-text/<string:prompt>")


class TextGeneration(MethodView):
    @blp.response(200, "Success")
    def get(self, prompt):
        """Generate text from a prompt"""
        result = text_generation.text_generation(prompt)
        return {"result": result}
