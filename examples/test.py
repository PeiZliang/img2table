from IPython.display import display_html
from PIL import Image as PILImage
from openpyxl import load_workbook
from io import BytesIO
import cv2
from img2table.document import Image
from img2table.ocr import PaddleOCR

paddle_ocr = PaddleOCR(lang="en", kw={"use_dilation": True})
img_path = "data/tables.png"


from img2table.document import Image


img = Image(src="D:\\github\\img2table\\examples\\data\\tables.png")

# Extract tables
extracted_tables = img.extract_tables()