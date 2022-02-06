from fractions import Fraction
from io import BytesIO
from typing import Tuple

import cairosvg
import filetype
from PIL import Image

from streamdeck_ui.display.filter import Filter


class ImageFilter(Filter):
    """
    Represents a static image. It transforms the input image by replacing it with a static image.
    """

    def __init__(self, size: Tuple[int, int], file: str):
        super(ImageFilter, self).__init__(size)
        self.file = file
        self.image = None

        try:
            kind = filetype.guess(self.file)
            if kind is None:
                svg_code = open(self.file).read()
                # TODO: Verify that the size works properly here. Previously was hardcoded to 72x72
                png = cairosvg.svg2png(svg_code, output_height=size[1], output_width=size[0])
                image_file = BytesIO(png)
                self.image = Image.open(image_file)
            else:
                self.image = Image.open(self.file).convert("RGBA")
        except (OSError, IOError) as icon_error:
            print(f"Unable to load icon {self.file} with error {icon_error}")
            self.image = Image.new("RGBA", size)

        self.image.thumbnail(size, Image.LANCZOS)

    def transform(self, input: Image, time: Fraction):
        """
        The transformation returns the loaded image, ando overwrites whatever came before.
        """
        Image.Image.paste(input, self.image)
        return input