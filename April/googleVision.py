import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types




# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources/wakeupcat.jpg')

text_file = os.path.join(
    os.path.dirname(__file__),
    'resources/jesus.jpg')

def image_path_here(fileName):
    return os.path.join(
    os.path.dirname(__file__),
    'resources/',fileName)

def detect_label(path):
    #Prints the labels associated with an image
    # Instantiates a client
    client = vision.ImageAnnotatorClient()
    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations


    #print('Labels:')
    #for label in labels:
        #print(label.description)

    return labels





def detect_text(path):
    """Detects text in the file."""
    #Prints the text object information found in an image
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print('Texts:')

    #for text in texts:
        #print('\n"{}"'.format(text.description))

        #vertices = (['({},{})'.format(vertex.x, vertex.y)
        #            for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

    return texts

def detect_face(path, max_results=4):
    #Returns an array of Face objects for the picture given
    client = vision.ImageAnnotatorClient()
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image).face_annotations

#detect_label(file_name)
#detect_text(text_file)
