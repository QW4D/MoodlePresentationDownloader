import requests
from img2pdf import convert
import shutil
import os
#link = input("ссылка на слайд (номер слайда заменить на {}):")

'''
i = 1
while requests.get(link.format(i)).ok:
    response = requests.get(link.format(i), stream=True)
    with open(f'tmp/{i}.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    i += 1
'''
i = 64
n = i
imgs = []
for i in range(n):
    imgs.append(f'tmp/{i+1}.png')
print(imgs)
with open('presentation.pdf', "wb") as pdf:
    pdf.write(convert(imgs))

os.remove("./tmp")