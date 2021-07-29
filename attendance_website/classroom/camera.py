import numpy as np
import cv2
import os
import urllib.request
from django.conf import settings
from PIL import Image
import base64

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")

faceCascade = cv2.CascadeClassifier(os.path.join(
    "OpenCv_Haarcascade/haarcascade_frontalface_alt.xml"))

recognizer = cv2.face.LBPHFaceRecognizer_create()


def save_base64Array(Id, content, count):
    dataset_dir = "dataSet/"
    Id = str(Id) + "/"
    path = os.path.join(settings.BASE_DIR, dataset_dir, Id)
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    decodeit = open(path + '/' + str(count) + ".jpeg", 'wb')
    decodeit.write(base64.b64decode(content))
    decodeit.close()
    return True


def ImageTrainer(Id):
    try:
        recognizer.read(os.path.join(settings.BASE_DIR, 'trainner.yml'))
    except:
        pass

    dataset_dir = "dataSet/"
    id = str(Id) + "/"

    path = os.path.join(settings.BASE_DIR, dataset_dir, id)

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

    def getImagesAndLabels(path):

        # # create empth face list
        faceSamples = []
        count = 0
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')

            # extract the face from the training image sample
            faces = face_detector.detectMultiScale(imageNp)
            # gray = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)

            for (x, y, w, h) in faces:
                faceSamples.append(imageNp[y:y+h, x:x+w])
                count += 1

        return faceSamples

    faces = getImagesAndLabels(path)
    Ids = []
    for i in range(len(faces)):
        Ids.append(int(Id))

    print(Ids)
    if os.path.exists(os.path.join(settings.BASE_DIR, 'trainner.yml')):
        recognizer.update(faces, np.array(Ids))
        recognizer.save(os.path.join(settings.BASE_DIR, 'trainner.yml'))
        print("updated the trainning model")
    else:
        recognizer.train(faces, np.array(Ids))
        recognizer.save(os.path.join(settings.BASE_DIR, 'trainner.yml'))
        print("created new training model")
        print(os.path)

    return True


def face_recognition(id):
    flag = False
    recognizer.read(os.path.join(settings.BASE_DIR, 'trainner.yml'))
    count = 0
    dataset_dir = "dataSet/"
    Id = str(id) + "/51.jpeg"
    paths = os.path.join(settings.BASE_DIR, dataset_dir, Id)

    pilImage = Image.open(paths).convert('L')
    # Now we are converting the PIL image into numpy array
    imageNp = np.array(pilImage, 'uint8')
    # extract the face from the training image sample
    faces = face_detector.detectMultiScale(imageNp)
    # gray = cv2.cvtColor(faces, cv2.COLOR_BGR2GRAY)
    print(faces)
    for (x, y, w, h) in faces:
        Id, conf = recognizer.predict(imageNp[y:y+h, x:x+w])
        print(id)
        print(Id)
        cv2.imwrite('C:/Users/nairn/OneDrive/Desktop/DataBase' + '/' +
                    str(count) + ".jpeg", imageNp[y:y+h, x:x+w])
        count += 1
        if int(Id) == int(id):
            flag = True
    print(flag)
    return flag
