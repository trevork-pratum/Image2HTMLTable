from PIL import Image
import os
import numpy as np

file_path = "image.png"
html_out = "<html><style>.bg {background:white}</style><table style=\"border-collapse: collapse;\">"

image = Image.open(file_path)
image_converted = image.convert("RGB")

pixels = np.asarray(image_converted)

"""print(len(pixels[0]))"""

for i in range(pixels.shape[0]):
    html_out+=str("<tr>")
    for j in range(pixels.shape[1]):
        #print("Pixel RBGA:" + str(pixels[j][i]))
        if(int(pixels[i][j][0]) == 0 and int(pixels[i][j][1]) == 0 and int(pixels[i][j][2]) == 0):
            #Convert the Alpha channel to white to prevent a black background.
            html_out+=str("<td class=\"bg\" />")
        else: 
            html_out+=str("<td style=background:rgb(" + str(pixels[i][j][0]) + "," + str(pixels[i][j][1]) + "," + str(pixels[i][j][2]) + "); />")
    html_out+=str("</tr>")

html_out += "</table></html>"
#print(html_out)

f = open("table-html-out.html", "w")
f.write(html_out)
f.close()