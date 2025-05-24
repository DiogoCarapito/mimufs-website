# website

[![Github Actions Workflow](https://github.com/DiogoCarapito/mimufs-website/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/website/actions/workflows/main.yaml)

mimufs - biblioteca python e tutoriais para o MIM@UF

[mimufs.com](https://mimufs.com)

___

## cheat sheet

### venv

create and activate .venv

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Dockerfile

#### build

```bash
docker build -t Home:latest .
````

#### check image id

```bash
docker images
````

#### run with image id

```bash
docker run -p 8501:8501 Home:latest
````
