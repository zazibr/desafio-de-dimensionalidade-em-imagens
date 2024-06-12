from PIL import Image

# Carregar a imagem colorida
img = Image.open('leao.png')
img.show()

# Converter a imagem para níveis de cinza
img_gray = img.convert('L')
img_gray.save('imagem_cinza.jpg')
img_gray = Image.open('imagem_cinza.jpg')
img_gray.show()


# Binarizar a imagem
threshold = 127
img_binary = img_gray.point(lambda p: p > threshold and 255)
img_binary.save('imagem_binaria.jpg')
img_binary = Image.open('imagem_cinza.jpg')
img_binary.show()
