import string
from PIL import Image, ImageDraw, ImageFont

class CharacterSetup:
    FONT_PATH = "C://Program Files//JetBrains//PyCharm 2025.1.3.1//jbr//lib//fonts//JetBrainsMono-Regular.ttf"
    FONT = ImageFont.truetype(FONT_PATH, size=15)
    CHARACTERS = string.printable[:-5]

    character_dict = {}

    # Checks pixel density of each character and orders them ascending
    def get_characters(self) -> list:
        for character in self.CHARACTERS:
            new_image = Image.new('L', (20, 20))
            image_draw = ImageDraw.Draw(new_image)

            image_draw.text((0, 0), character, font=self.FONT, fill=255)
            self.character_dict[character] = sum(new_image.get_flattened_data())

        character_dict = {k: v for k, v in sorted(self.character_dict.items(), key=lambda item: item[1])}
        return list(character_dict.keys())


