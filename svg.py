import svgwrite

from svg_manager import SvgManager

svg_filename = "test-pysvg.svg"
profile = 'full'
size = ('11in', '8in')
svg_file = SvgManager(svg_filename, profile, size)
# svg_file.add_rect(0, 0, '9in', '6in', svgwrite.rgb(50, 50, 50, '%'))
# svg_file.add_rect(0, 0, '8in', '6in', svgwrite.rgb(30, 30, 30, '%'))
# svg_file.add_rect(0, 0, '7in', '6in', svgwrite.rgb(50, 50, 50, '%'))
# svg_file.add_rect(0, 0, '6in', '6in', svgwrite.rgb(30, 30, 30, '%'))
# svg_file.add_rect(0, 0, '5in', '5in', svgwrite.rgb(50, 50, 50, '%'))
# svg_file.add_rect(0, 0, '4in', '4in', svgwrite.rgb(30, 30, 30, '%'))
# svg_file.add_rect(0, 0, '3in', '3in', svgwrite.rgb(50, 50, 50, '%'))
# svg_file.add_rect(0, 0, '2in', '2in', svgwrite.rgb(30, 30, 30, '%'))
# svg_file.add_rect(0, 0, '1in', '1in', svgwrite.rgb(50, 50, 50, '%'))
# svg_file.add_rect(0, 0, '0.5in', '0.5in', svgwrite.rgb(30, 30, 30, '%'))
# svg_file.add_rect(0, 0, '0.25in', '0.25in', svgwrite.rgb(50, 50, 50, '%'))
#
# svg_file.add_text_block('Hello 10pt', 0, '0.2in', 'font-size:10pt; font-family: Arial')
svg_file.add_text_block('Hello 18pt', '0.2in', f'{1}in', 'font-size:18pt; font-family: Arial')
svg_file.add_text_block('Hello 36pt', '0.5in', f'{2}in', 'font-size:36pt; font-family: Arial')
svg_file.add_text_block('Hello 54pt', '1in', f'{3}in', 'font-size:54pt; font-family: Arial')
svg_file.add_text_block('Hello 72pt', '1.5in', f'{5}in', 'font-size:72pt; font-family: Arial')

svg_file.save()
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

drawing = svg2rlg('Bg.svg')
drawing.add( svg2rlg(svg_filename))
# scaleFactor = 1./0.3527
# drawing.width *= scaleFactor
# drawing.height *= scaleFactor
# drawing.scale(scaleFactor, scaleFactor)
renderPDF.drawToFile(drawing, "file.pdf", autoSize=1)
