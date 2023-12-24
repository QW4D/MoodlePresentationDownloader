import requests
from img2pdf import convert
import shutil
import os

link = input("ссылка на слайд (номер слайда заменить на {}): ")

if input("тип:\n [0] презентация\n [1] лекция\n") == "1":
    type = 1
else:
    type = 0
i = int(type)

s = requests.session()
cookies = {"MoodleSession": input("moodleSession куки (оставить пустым, если не нужно): ")}
if "tmp" in os.listdir():
    shutil.rmtree("tmp")
os.mkdir("tmp")
while requests.get(link.format(i), cookies=cookies).ok:
    response = requests.get(link.format(i), stream=True, cookies=cookies)
    with open(f'tmp/{i}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print(i)
    i += 1

n = i
imgs = []
for i in range(n):
    if i != (not type):
        imgs.append(f'tmp/{i}.png')

print(imgs)
with open('presentation.pdf', "wb") as pdf:
    pdf.write(convert(imgs))

shutil.rmtree("tmp")
