import numpy as np
from CharacterSetup import CharacterSetup
from PIL import Image, ImageEnhance


if __name__ == '__main__':
    characters = CharacterSetup().get_characters()
    img = Image.open('Images/cat_image2.jpg')
    img_width, img_height = img.size

    new_width = 100
    new_height = int(img_height * new_width / img_width)

    enhancer = ImageEnhance.Contrast(img)
    output = img.resize((new_width, new_height), Image.Resampling.LANCZOS).convert('L')

    output.show()
    pixels = np.array(output)

    output_string = """"""

    for row in pixels:
        for pixel in row:
            output_string += characters[int(pixel // 2.69)] + " "
        output_string += "\n"

    print(output_string)

