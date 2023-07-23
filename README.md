# LLama-v2-Text-Gen-API

This project aims to develop an API backend using Flask to support Text Generation Inference with Llama v2 Models

## Results

API Call:

`http://127.0.0.1:5000/generate-text/Name the planets in the solar system`

API Response:
![image](https://github.com/kevinknights29/LLama-v2-Text-Gen-API/assets/74464814/2dff71b2-e102-48d8-ab2e-884ec34109b3)

## Contributing

### Installing pre-commit

Pre-commit is already part of this project dependencies.
If you would like to installed it as standalone run:

```console
pip install pre-commit
```

To activate pre-commit run the following commands:

- Install Git hooks:

```console
pre-commit install
```

- Update current hooks:

```console
pre-commit autoupdate
```

To test your installation of pre-commit run:

```console
pre-commit run --all-files
```
