import os
import cv2

path = 'Images/'

images = []

sorted_images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.jpg', '.jpeg']:
        file_name = path + file
        images.append(file_name)
        
sorted_images = sorted(images)
print(sorted_images)

count = len(sorted_images)

frame = cv2.imread(sorted_images[0])

height, width, channel = frame.shape
size = (width, height)

print(size)

out = cv2.VideoWriter("project.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 1, size)

for i in range (0, count-1):
    img = cv2.imread(sorted_images[i])
    out.write(img)

out.release()
print("video complete!")
    

