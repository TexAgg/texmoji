import base64

# http://stackoverflow.com/questions/2323128/convert-string-in-base64-to-image-and-save-on-filesystem-in-python
def save_raw_img(imgData, file):
	with open(file, "wb") as fh:
		fh.write(base64.decodestring(imgData))