import requests
import base64
import codecs
import cv2

urlOverride = "https://cdn.arparec.dev/images/recworks.jpg"

def doRequest(url):
    reqURL = requests.get(url, headers={'content-type': 'image/jpeg'}) # headers={'content-type': 'image/jpeg'}
    # encodedText = base64.b64encode(bytes(reqURL.text, 'utf-8'))
    # decodedText = encodedText.decode('utf-8')

    hexCoded = codecs.encode(bytes(reqURL.text, 'utf-16'), "hex")
    f = open("./file5.jpg", "wb") #filename
    f.write(hexCoded)
    f.close()

    print(hexCoded) # debug

doRequest(urlOverride)