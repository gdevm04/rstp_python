# Repositório Python para Captura de Vídeo via RTSP de Câmera IP

## Introdução

Este repositório oferece uma solução simples e eficiente para capturar vídeos de uma câmera IP via RTSP usando Python. A implementação utiliza a biblioteca `rtsp` para a comunicação RTSP e a biblioteca `cv2` do OpenCV para o processamento de vídeo.

## Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados:

- Python 3.x
- Biblioteca `rtsp`: Você pode instalá-la usando o comando `pip install rtsp`
- Biblioteca `opencv-python`: Instale com `pip install opencv-python`

## Configuração

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/seu-username/nome-do-repositorio.git
   ```

Navegue até o diretório do projeto:

Abra o arquivo main.py em seu editor de escolha.
Crie um arquivo .env no diretório do projeto e adicione sua URL RTSP:

RTSP_URL=rtsp://admin:PASSWORD@IP/axis-media/media.amp

Substitua o valor da variável rtsp_url com a URL RTSP de sua câmera IP:

Uso
Execute o script main.py para iniciar a captura do vídeo. A janela será exibida, mostrando o feed de vídeo da câmera IP.

python main.py
Para encerrar a execução, pressione a tecla 'q'.

Personalizações
Sinta-se à vontade para personalizar o script para atender às suas necessidades. Você pode adicionar funcionalidades como processamento de imagem, detecção de objetos, ou integração com modelos de IA.

Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, enviar pull requests ou sugerir melhorias.

Licença
Este projeto é licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

Espero que este repositório seja útil para a comunidade. Divirta-se explorando e contribuindo!
