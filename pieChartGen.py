# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:59:58 2018

@author: Rimi
"""

import random
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import xml.etree.ElementTree as xml
import csv,json



def pieChart(N,count):
    #fig, ax = plt.subplots(1)#figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    global bbox_legend
    methodLabels = random.sample(set(labelsDict),N)
    
    colorMapList =['viridis','plasma','inferno','magma','cividis']
    colorMapItem = random.choice(colorMapList)
    cmap = plt.get_cmap(colorMapItem)
    colorsM = cmap(np.linspace(0, 1, N))
    textColor = (1,1,1,1)
    
    mydpi=100
    fig = plt.figure(figsize = (6,4))  
    ax = fig.subplots()
    
    legendDict = {}
    xlegpos = random.uniform(0.9,1)
    ylegpos = random.uniform(0,1)
    legwidth = random.uniform(0.2,0.5)
    legheight = random.uniform(0.8,1)
    
    xloc = random.uniform(0.2,0.3)
    yloc = random.uniform(0.75,0.85)
    fontrand = random.randint(7,12)
    
    legendDict["xbbox"]=xlegpos
    legendDict["ybbox"]=ylegpos
    legendDict["width"]=legwidth
    legendDict["height"]=legheight
    legendDict["xloc"]=xloc
    legendDict["yloc"]=yloc
    legendDict["fontsize"]=fontrand
    
    pcts = '%1.1f%%'
    #print methods
    percMethods = func(methods)
    patches,text,_ = plt.pie(percMethods,labels=methodLabels,colors = colorsM,autopct=pcts,textprops=dict(color=textColor))
    
    leg = plt.legend(patches,methodLabels,loc=(xloc,yloc),bbox_to_anchor=(xlegpos, ylegpos, legwidth, legheight),fontsize = fontrand)
    rendererIns = fig.canvas.get_renderer()
    #print(ax.yaxis.get_tightbbox())
    
    #tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    #tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    
    legendDict["legPixelBbox"]={"x1":bbox_legend.x0,"y1":bbox_legend.y0,"x2":bbox_legend.x1,"y2":bbox_legend.y1}
    
    #bbox_legend = leg.get_bbox_to_anchor()
    #print(ax.xaxis.get_label_bbox())
    print (bbox_legend)
    global f
    f = str(numOfMethods)+"_pie_"+str(count)
    
    saveData(percMethods,methodLabels,colorsM,pcts,textColor,legendDict,f)
    plt.tight_layout()
    plt.savefig(("PieCharts/"+str(numOfMethods)+"_pie_"+str(count)+".png"),dpi=mydpi*10)
    matplotlib.pyplot.close()
    #plt.setp(autotexts, size=8, weight="bold")
    #ax.set_title("Matplotlib bakery: A pie")
    #plt.show()


def func(allvals):
    absolutes=[]
    for i in range(len(allvals)):
        absolute = float(((allvals[i]/sum(allvals))*100))
        absolutes.append(absolute)
    return absolutes


def saveData(percMethods,methodLabels,colorsM,pcts,textColor,legendDict,f):
    userelement = xml.Element("piechart")
    root.append(userelement)
    uid = xml.SubElement(userelement, "pieId", attrib={"id":f})    

    NoOfMethods = xml.SubElement(userelement, "NoOfMethods", attrib={"count":str(numOfMethods)})
    
    data = xml.SubElement(userelement, "data")
    for i in range(len(percMethods)):
        method = xml.SubElement(data, "method",attrib={"id":str(i),"value": str(percMethods[i]), "label":str(methodLabels[i]), "color":str(colorsM[i]),"textcolor":str(textColor),"autopct":pcts})
        
    legendTag = xml.SubElement(userelement, "legend", attrib={"xbbox":str(legendDict["xbbox"]), "ybbox":str(legendDict["ybbox"]), "heightbbox":str(legendDict["height"]), "widthbbox":str(legendDict["width"]), "xloc":str(legendDict["xloc"]), "yloc":str(legendDict["yloc"]), "fontsize":str(legendDict["fontsize"]),"pixelBbox":str(legendDict["legPixelBbox"])})
    tree = xml.ElementTree(root)
    with open(xml_file, "wb+") as fh:
        tree.write(fh)
    make_json_type1()
    make_csv_type2()
        
        
def make_json_type1():
    #global json_images
    rects = []
    one_decimal = "{0:0.1f}"
    bbox_list = [bbox_legend]
    for i in range(len(bbox_list)):
        x1 = float(one_decimal.format(bbox_list[i].x0))
        x2 = float(one_decimal.format(bbox_list[i].x1))
        y1 = float(one_decimal.format(bbox_list[i].y0))
        y2 = float(one_decimal.format(bbox_list[i].y1))

        #enforce x1,y1 = top left, x2,y2 = bottom right

        tlx = min(x1,x2)
        tly = min(y1,y2)
        brx = max(x1,x2)
        bry = max(y1,y2)

        bbox = dict([("x1",tlx),("y1",tly),("x2",brx),("y2",bry)])
        rects.append(bbox)
    print(rects)
    json_image = dict([("image_path",("PieCharts/"+f+".png")),("rects",rects)])

    json_images.append(json_image)
    
def make_csv_type2():
    #global json_images
    one_decimal = "{0:0.1f}"
    bbox_list = [bbox_legend]
    classes = ["Legendbbox"]
    for i in range(len(bbox_list)):
        x1 = float(one_decimal.format(bbox_list[i].x0))
        x2 = float(one_decimal.format(bbox_list[i].x1))
        y1 = float(one_decimal.format(bbox_list[i].y0))
        y2 = float(one_decimal.format(bbox_list[i].y1))

        #enforce x1,y1 = top left, x2,y2 = bottom right
        
        tlx = min(x1,x2)
        tly = min(y1,y2)
        brx = max(x1,x2)
        bry = max(y1,y2)
        image_path = str("PieCharts/"+f+".png")
        outfile_csv.writerow([image_path,str(tlx),str(tly),str(brx),str(bry),classes[i]])


if __name__ == "__main__":
    line_foo = open("pie_error_5001_10000.txt","w")
    xml_file = "pie_xml_5000_10000.xml"
    outfile = open("piechart_json_5000_10000.json","w")
    outfile_csv = csv.writer(open("piechart_csv_5000_10000.csv","w"))
    json_images=[]
    root = xml.Element("PieCharts")
    noOfPlot=2000
    for c in range(0,noOfPlot):
        try:
            global numOfMethods
            numOfMethods = random.randint(2,5)
            methods = []
            for i in range(numOfMethods):
                temp = random.random()
                methods.append(temp)
                #print x_gt,y_gt
            labelsDict = []
            Mlabels = open('../XYlabels.txt','r')
            for line in Mlabels:
                line= line.rstrip()
                if len(line)<=20:
                    labelsDict.append(line)
                    
            pieChart(numOfMethods,c) 
            #fileId = str(numOfMethods)+"_line_"+str(c)
            #saveData(xml_file,fileId,numOfMethods)
        except Exception as e:
            print e
            line_foo.write("Failed {0}: {1}\n".format(str(c), str(e))+"\n")
            pass
            continue
        outfile.write(json.dumps(json_images, indent = 1))
