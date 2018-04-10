from PIL import Image
import numpy as np

js_image=image.open(r"C:\Users\anass\Pictures\stries\StriesC2.TIF")
js_array=np.array(js_image)
print(js_array)