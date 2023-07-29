from __future__ import annotations

from flask.views import MethodView
from flask_smorest import Blueprint

from src.llm import text_generation
from src.schema import schema


blp = Blueprint(
    "Text Generation",
    __name__,
    url_prefix="/generate-text",
    description="Text Generation API",
)


@blp.route("")
class TextGeneration(MethodView):
    @blp.arguments(schema.PromptSchema)
    @blp.response(201, schema=schema.TextGenerationSchema)
    def post(self, prompt_data):
        """Generate text from a prompt"""
        result = text_generation.text_generation(prompt_data["prompt"])
        return result
