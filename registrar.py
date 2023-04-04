import cv2
import os
import imutils
import train

def datos_persona():
    '''
    Pregunta al usuario el nombre y si es Cliente o Empleado, para registrarlo.
    '''
    isaWorker = int(input('Es usted Cliente (Ingrese 0) o Empleado (Ingrese 1): ' ))
    classFolder = {0:'Cliente',
                1:'Empleado'}
    personName = str(input('Nombre y Apellido: '))
    prepara_dataset(isaWorker, classFolder, personName)

def prepara_dataset(isaWorker, classFolder, personName):
    '''
    Prepara las carpetas con las imagenes de la persona a registrar, para luego entrenar el modelo
    '''
    dataDir = './Data/' + classFolder[isaWorker] + '/' + personName
    print(dataDir)

    if not os.path.exists(dataDir):
        print('Carpeta Creada: ', dataDir)
        os.makedirs(dataDir)

    #cap = cv2.VideoCapture('aleh.mp4')
    cap = cv2.VideoCapture(0)
    faceClass = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    c = 0
    print('Tomando fotografias...')
    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux = frame.copy()
        faces = faceClass.detectMultiScale(gray, 1.3, 5, flags=cv2.CASCADE_SCALE_IMAGE)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y), (w+x,h+y), (255,0,0), 2)
            face = aux[y:y+h,x:x+w]
            face = cv2.resize(face, (150,150), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(dataDir + '/' + f'face_{c}.jpg', face)
            c+=1
        
        cv2.imshow('frame',frame)

        k = cv2.waitKey(1)
        if k==27 or c >= 200:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    train.entrenar_modelo()