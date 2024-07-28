import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = "https://pickledrevieww.blogspot.com/"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
url.svg("myqrBlog.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('myqrBlog.png', scale = 6) 