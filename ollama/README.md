
```bash
docker compose up
```

```bash
docker exec -it ollama bash
```

В контейнере ollama:

```bash
nvidia-smi
```

```bash
ollama pull mistral-small3.2:24b
```

```bash
ollama run mistral-small3.2:24b
```

```bash
/set parameter num_ctx 64000
```

```bash
/save mistral-small3.2:24b-64k
```

```bash
ollama run mistral-small3.2:24b-64k
```