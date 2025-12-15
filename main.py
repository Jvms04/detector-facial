import cv2

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

#  Inicia a captura de vídeo (conecta na webcam padrão)
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


# 3. Loop infinito para processar o vídeo ao vivo
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

# 4. Libera a câmera e fecha as janelas
video_capture.release()
cv2.destroyAllWindows()