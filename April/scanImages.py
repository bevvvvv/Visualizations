import googleVision
import os
import csv

pictures = os.listdir(os.path.join(os.path.dirname(__file__), 'resources/'))
picLabels = {}
picText = {}

for i in range(len(pictures)):
    name = 'Post ' + str(i + 1)
    print(name)
    picLabels[name] = []
    picText[name] = []
    #if i == 1:
    #    break
    imagePath = googleVision.image_path_here(pictures[i])
    # label text in labels[index].description
    labels = googleVision.detect_label(imagePath)
    for x in labels:
        picLabels[name].append(x.description)
    # text string in text[index].description
    texts = googleVision.detect_text(imagePath)
    for y in texts:
        picText[name].append(y.description)

## Write API Results to CSV
with open(os.path.join(os.path.dirname(__file__),'picLabel.csv'), 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    for key in picLabels:
        for i in range(len(picLabels[key])):
            writer.writerow([key, picLabels[key][i]])
with open(os.path.join(os.path.dirname(__file__),'picText.csv'), 'w') as csvFile:
    writer = csv.writer(csvFile, delimiter=',')
    for key in picText:
        for i in range(len(picText[key])):
            try:
                writer.writerow([key, picText[key][i]])
            except:
                continue
                        

#print(labels)
#print(texts)
