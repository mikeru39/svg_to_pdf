import svgwrite


class SvgManager:
    __work_sheet: svgwrite.Drawing = None

    def __init__(self, file_name, profile, size):
        self.__work_sheet = svgwrite.Drawing(file_name, profile=profile, size=size)

    def add_text_block(self, text, x, y, style):
        self.__work_sheet.add(self.__work_sheet.text(
            text,
            insert=(x, y),
            style=style,
            # dominant_baseline="middle",
            # text_anchor="middle"
        ))

    def add_image(self):
        self.__work_sheet.add(self.__work_sheet.image('Bg.svg', insert=(0, 0), size=("11in", "8in")))

    def add_rect(self, x, y, w, h, fill):
        self.__work_sheet.add(self.__work_sheet.rect((x, y), (w, h), fill=fill))

    def save(self):
        self.__work_sheet.save()
