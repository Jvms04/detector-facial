# 👁️ Real-Time Facial Detection (OpenCV)

Este é um projeto Python simples e funcional para detectar rostos em tempo real usando a webcam. Ele utiliza a biblioteca `OpenCV` e o algoritmo Haar Cascade para identificar faces no vídeo.

## ✨ 1. Pré-requisitos (O que você precisa)

Para executar este script, você precisa ter o Python 3 instalado e a biblioteca `opencv-python` configurada:

1.  **Instale o Python:** Certifique-se de ter o Python 3.x instalado em seu sistema.
2.  **Instale a Biblioteca:** Use o `pip` no seu terminal para adicionar a dependência necessária ao seu ambiente:

    ```bash
    pip install opencv-python
    ```

## ⚙️ 2. Como Clonar o Repositório

Para trazer o código para a sua máquina, você deve clonar este repositório:

1.  **Abra o Terminal** (Prompt de Comando ou PowerShell).
2.  **Clone o Projeto:** Execute o comando `git clone`, usando a URL HTTPS deste repositório:

    ```bash
    git clone [https://github.com/Jvms04/facial-detection-opencv.git](https://github.com/Jvms04/facial-detection-opencv.git)
    ```
3.  **Entre na Pasta:** Navegue para o diretório do projeto:

    ```bash
    cd facial-detection-opencv
    ```

## 💻 3. Tutorial de Uso (main.py)

Abaixo está o código completo do arquivo `main.py` para referência:

```python
import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Inicia a captura de vídeo (conecta na webcam padrão)
video_capture = cv2.VideoCapture(0)

# Função que detecta rostos e desenha o quadrado verde
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

    # Detecta as faces
    faces = face_classifier.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(40, 40)
    )

    # Desenha os retângulos para cada face encontrada
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)

    return faces

# Loop infinito para processar o vídeo ao vivo
while True:
    # Lê um frame da câmera
    result, video_frame = video_capture.read()

    # Se a câmera não ler nada, para o loop
    if result is False:
        break

    # Chama a função para detectar rostos neste frame
    faces = detect_bounding_box(video_frame)

    # Mostra a janela com o vídeo
    cv2.imshow("Detector Facial", video_frame)

    # Se apertar a tecla 'q', sai do programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()
```

### Explicação Passo a Passo

| Linha | Código | Ação (O que a linha faz) |
| :--- | :--- | :--- |
| **Linha 3** | `face_classifier = ...` | **Carrega o Modelo:** Importa o arquivo XML "Haar Cascade" que contém os dados necessários para reconhecer rostos frontais. |
| **Linha 8** | `video_capture = cv2.VideoCapture(0)` | **Acessa a Câmera:** Inicializa a conexão com a webcam padrão do computador (índice 0). |
| **Linha 12** | `gray_image = cv2.cvtColor(...)` | **Converte a Imagem:** Transforma o frame colorido em escala de cinza para tornar a detecção mais rápida e eficiente. |
| **Linha 15** | `faces = face_classifier.detectMultiScale(...)` | **Detecta Faces:** O algoritmo varre a imagem buscando padrões faciais. Parâmetros como scaleFactor ajustam a precisão. |
| **Linha 23** | `cv2.rectangle(...)` | **Desenha o Quadrado:** Para cada rosto encontrado, desenha um retângulo verde (0, 255, 0) nas coordenadas identificadas. |
| **Linha 29** | `while True:` | **Loop Infinito: Mantém o programa rodando continuamente, processando o vídeo quadro a quadro.** |
| **Linha 40** | `cv2.imshow("Detector Facial", video_frame)` | **Exibe o Resultado:** Abre uma janela no Windows mostrando o vídeo com os retângulos desenhados. |
| **Linha 43** | `if cv2.waitKey(1) ... == ord('q'):` | **Comando de Saída:** Verifica se a tecla 'q' foi pressionada para interromper o loop e fechar o programa. |

### 🚀 Para Executar:

1.  **Certifique-se de que a webcam está conectada.**
2.  **Execute o Script:**
    ```bash
    python main.py
    ```

## 🧑‍💻 Autor

Este projeto foi criado por **João Vítor Moço Santos**.
