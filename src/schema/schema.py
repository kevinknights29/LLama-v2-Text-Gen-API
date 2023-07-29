from __future__ import annotations

from marshmallow import fields
from marshmallow import Schema


class ChoiceSchema(Schema):
    finish_reason = fields.Str(required=True)
    index = fields.Int(required=True)
    logprobs = fields.Str(required=False)
    text = fields.Str(required=True)


class UsageSchema(Schema):
    completion_tokens = fields.Int(required=True)
    prompt_tokens = fields.Int(required=True)
    total_tokens = fields.Int(required=True)


class TextGenerationSchema(Schema):
    choices = fields.List(fields.Nested(ChoiceSchema), required=True)
    created_at = fields.Int(required=True)
    id = fields.Str(required=True)
    model = fields.Str(required=True)
    object = fields.Str(required=True)
    usage = fields.Nested(UsageSchema, required=True)


class PromptSchema(Schema):
    prompt = fields.Str(required=True)
