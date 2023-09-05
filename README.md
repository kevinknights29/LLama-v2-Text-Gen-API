# LLama-v2-Text-Gen-API

This project aims to develop an API backend using Flask to support Text Generation Inference with Llama v2 Models

## Results

### Swagger-UI

![image](https://github.com/kevinknights29/LLama-v2-Text-Gen-API/assets/74464814/f17c4861-a1fe-4869-a598-4632ef62efa3)

### API Call and Response

![image](https://github.com/kevinknights29/LLama-v2-Text-Gen-API/assets/74464814/8cc15848-f317-4e61-8885-8329555dd184)

### Streaming API

![screen_recording](https://github.com/kevinknights29/LLama-v2-Text-Gen-API/assets/74464814/09e39a03-a00f-404f-a98c-3af417effaac)

## Usage

### Build APP Image

```bash
docker compose build
```

### Get everything up and running

```bash
docker compose down && docker compose up -d
```

### Have fun

Visit: `http://localhost:7860/swagger/` to access the Swagger API Docs.

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
