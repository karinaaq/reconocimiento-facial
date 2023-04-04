import cv2
import os
import numpy as np

def entrenar_modelo():
	rootPath = r'./Data/'
	empleadoPath = r'./Data/Empleado/'
	clientePath = r'./Data/Cliente/'
	empleadoList = ['Empleado/' + x for x in os.listdir(empleadoPath)]
	clienteList = ['Cliente/' + x for x in os.listdir(clientePath)]
	peopleList = empleadoList + clienteList
	
	labels = []
	facesData = []
	label = 0

	for nameDir in peopleList:
		personPath =  rootPath + nameDir
		print('Leyendo las imágenes')

		for fileName in os.listdir(personPath):
			print('Rostros: ', nameDir + '/' + fileName)
			labels.append(label)
			facesData.append(cv2.imread(personPath+'/'+fileName,0))
			#image = cv2.imread(personPath+'/'+fileName,0)
			#cv2.imshow('image',image)
			cv2.waitKey(10)
		label = label + 1

	#face_recognizer = cv2.face.EigenFaceRecognizer_create()
	#face_recognizer = cv2.face.FisherFaceRecognizer_create()
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()

	print("Entrenando el reconocedor de rostros...")
	face_recognizer.train(facesData, np.array(labels))

	#face_recognizer.write('modeloEigenFace.xml')
	#face_recognizer.write('modeloFisherFace.xml')
	face_recognizer.write('modeloLBPHFace.xml')
	print("Modelo almacenado...")
	