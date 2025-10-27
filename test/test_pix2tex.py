from PIL import Image
from pix2tex.cli import LatexOCR
import os

# Lấy đường dẫn thư mục chứa file này
current_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(current_dir, 'img', 'pure.png')

img = Image.open(img_path)
model = LatexOCR()
latex_code = model(img)
print(latex_code)
