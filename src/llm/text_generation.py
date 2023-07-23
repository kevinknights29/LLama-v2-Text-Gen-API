from __future__ import annotations

from pathlib import Path

from llama_cpp import Llama

LLM = None


def _find_model(model_dir="/otp/app/models", pattern="*.bin"):
    model_path = Path(model_dir)
    model_file_path = list(model_path.glob(pattern))[0]

    return str(model_file_path.resolve())


def _format_prompt(prompt):
    # remove trailing spaces
    prompt = prompt.strip()
    # remove trailing question mark
    prompt = prompt[:-1] if prompt[-1] == "?" else prompt

    return f"Q:{prompt}? A:"


def text_generation(prompt):
    global LLM
    if LLM is None:
        LLM = Llama(_find_model())

    generation_params = {
        "max_tokens": 256,
        "stop": ["Q:", "\n"],
        "echo": True,
    }

    return LLM(_format_prompt(prompt), **generation_params)
