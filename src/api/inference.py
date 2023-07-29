from __future__ import annotations

from flask import Response
from flask import stream_with_context
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


@blp.route("/stream")
class TextGenerationStream(MethodView):
    @blp.arguments(schema.PromptSchema)
    def post(self, prompt_data):
        """Generate streaming text from a prompt"""

        def generate():
            for result in text_generation.text_generation_stream(prompt_data["prompt"]):
                yield result["choices"][0]["text"].encode("utf-8")

        return Response(stream_with_context(generate()), mimetype="text/plain")
