# -*- coding: utf-8 -*-
import urllib.request

from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF


txtdata = "thhp://http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt"
COMMENT_CHARS = '#:'
drawing = Drawing(400, 200)
data = []
with open('data.txt', 'r') as datatxt:
    for line in datatxt.readlines():
        if not line.isspace() and not line[0] in COMMENT_CHARS:
            data.append([float(n) for n in line.split()])

perd = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[1] for row in data]

'''
perdzip, highzip, lowzip = list(zip(times, perd)), list(
    zip(times, high)), list(zip(times, low))
print(perdzip, highzip, lowzip)'''
# print(data)
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = (list(zip(times, perd)), list(
    zip(times, high)), list(zip(times, low)))
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green
drawing.add(lp)
drawing.add(String(65, 150, u'2008年Sunspots',
                   fontSize=18, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'test.pdf', 'A simple PDF file')
'''s = String(50, 50, "wahaha!", textAnchor='middle')
d.add(s)
'''
