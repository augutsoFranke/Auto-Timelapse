import sys
from moviepy import VideoFileClip

def criar_timelapse(arquivo_entrada, duracao_final, arquivo_saida="timelapse.mp4"):
    clip = VideoFileClip(arquivo_entrada)

    duracao_original = clip.duration
    fator = duracao_original / duracao_final
    fator = max(fator, 1)  # garante que não desacelere vídeos curtos

    timelapse = clip.with_speed_scaled(factor=fator)
    timelapse = timelapse.without_audio()  # remove o áudio

    timelapse.write_videofile(arquivo_saida, codec="libx264", fps=30)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    arquivo = sys.argv[1]
    duracao = int(sys.argv[2]) if len(sys.argv) > 2 else 30

    criar_timelapse(arquivo, duracao)
