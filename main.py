import numpy as np
from CharacterSetup import CharacterSetup
from PIL import Image, ImageEnhance


if __name__ == '__main__':
    characters = CharacterSetup().get_characters()
    img = Image.open('Images/image4.jpg')
    img_width, img_height = img.size

    new_width = 150
    new_height = int(img_height * new_width / img_width)

    enhancer = ImageEnhance.Contrast(img)
    result_img = enhancer.enhance(1.5)
    output = result_img.resize((new_width, new_height), Image.Resampling.LANCZOS).convert('L')

    pixels = np.array(output)

    output_string = """"""

    for row in pixels:
        for pixel in row:
            output_string += characters[int(pixel // 2.69)] + " "
        output_string += "\n"

    print(output_string)
    file = open("output.txt", "x")
    with open(file.name, "w") as file:
        file.write(output_string)