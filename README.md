Auto Timelapse
==============

Script simples para gerar timelapse a partir de um vídeo.

Requisitos
----------

- Python 3.10+
- uv (`pip install uv` se ainda não tiver)

Instalação
----------

```bash
uv sync
uv pip install moviepy    # caso ainda não esteja no lock
```

Uso
---

```bash
uv run python main.py <video_entrada> [duracao_final_segundos]
```

- Se `duracao_final_segundos` não for informado, usa 30.
- Saída padrão: `timelapse.mp4`.

Obs: o áudio é removido automaticamente.
