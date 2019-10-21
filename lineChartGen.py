# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:55:51 2018

@author: Rimi
"""
import matplotlib
matplotlib.use('Agg')
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import json,csv
from collections import defaultdict
from matplotlib.transforms import Bbox
import matplotlib.legend as mat_leg
import xml.etree.ElementTree as xml


def linearFunction(x):
    m = random.uniform(0.1, 1)
    b = random.uniform(3, 10)
    y=((m*x)+ b)
    return y
    
def quadraticFunction(x):
    a = random.uniform(1,10)
    b = random.uniform(2,5)
    c = random.uniform(1,10)
    y=((a*x*x)+(b*x)+c)
    return y
    
def powerFunction(x):
    a = random.uniform(0.1,5)
    b = random.randint(1,6)
    y=(a*(x**b))
    return y
    
def polynomialFunction(x):
    n = random.choice([1,2,3,4])
    a = []
    for i in range(n):
        a.append(random.uniform(0.1,1))
    y=0
    for i in range(n):
        y = y+ a[i]*(x**float(i))
    return y
        
def exponentialFunction(x):
    a = random.uniform(0.1,5)
    b = random.uniform(0.1,1)
    y=(a*(b**x))
    #y=math.exp(x)
    return y
    
def logarithmicFunction(x):
    a = random.uniform(0.1,1)
    b = random.uniform(2,10)
    y=(a*math.log(x))#+b
    return y
    
        
        
def LineChartNDataGen(x,y,N,NoOfDataPoints):
    #Here the number of lines = 2
    global lineFunc
    funcs = ["linearFunction","quadraticFunction","powerFunction","polynomialFunction","exponentialFunction","logarithmicFunction"]
    funcChoice = random.choice(funcs)
    lineFunc =funcChoice
    
    print(NoOfDataPoints,N)
    #print funcChoice
    if funcChoice =="linearFunction":
        for i in range(NoOfDataPoints):
            xtemp = random.randint(1,i+3)#float(random.uniform(0.1,15))
            for j in range(N):    
                x[j].append(xtemp)
                ytemp = linearFunction(xtemp)
                y[j].append(ytemp)
    if funcChoice =="quadraticFunction":
        for i in range(NoOfDataPoints):
            xtemp = random.randint(1,i+3)#i+1#float(random.uniform(0.1,15))
            for j in range(N):
                x[j].append(xtemp)
                ytemp = quadraticFunction(xtemp)
                y[j].append(ytemp)
    if funcChoice =="powerFunction":
        for i in range(NoOfDataPoints):
            xtemp = random.randint(1,i+3)#i+1#float(random.uniform(0.1,15))
            for j in range(N):
                x[j].append(xtemp)
                ytemp = powerFunction(xtemp)
                y[j].append(ytemp)
    if funcChoice =="polynomialFunction":
        for i in range(NoOfDataPoints):
            xtemp = random.randint(1,i+3)#i+1#float(random.uniform(0.1,15))
            for j in range(N): 
                x[j].append(xtemp)
                ytemp = polynomialFunction(xtemp)
                y[j].append(ytemp)
    if funcChoice =="exponentialFunction":
        for i in range(NoOfDataPoints):
            xtemp = random.randint(1,i+3)#i+1#float(random.randint(1,7))
            for j in range(N):
                x[j].append(xtemp)
                ytemp = exponentialFunction(xtemp)
                y[j].append(ytemp)
    if funcChoice =="logarithmicFunction":
        for i in range(NoOfDataPoints):
            xtemp =random.randint(1,i+3)# i+1#float(random.uniform(0.1,15))
            for j in range(N):
                x[j].append(xtemp)
                ytemp = logarithmicFunction(xtemp)
                y[j].append(ytemp)
    #print x,y
    for i in range(N):
        x[i],y[i] = zip(*sorted(zip(x[i], y[i])))
    #print x,y
    return x,y,lineFunc 

def ChartProperties(x,y,N,p):
    #box = dict(facecolor='yellow', pad=5, alpha=0.5)
    selectedLabels = random.sample(set(labelsDict),2)
    XLabel = selectedLabels[0]
    YLabel = selectedLabels[1]
    
    xposX = random.uniform(0.2,0.8)
    yposX = random.uniform(-0.05,-0.4)
    #print xposX,yposX
    
    xposY = random.uniform(-0.08,-0.2)
    yposY = random.uniform(0.2,0.8)
    
    
    legXLoc = random.uniform(0.1,0.7)
    legYLoc = random.uniform(0.2,0.72)
    legbboxX = random.uniform(0,0.9)
    legbboxY = random.uniform(0.3,0.7)
    fontrand = random.randint(7,12)
    legboxh = random.uniform(0.1,0.6)
    legboxw = random.uniform(0.1,0.6)

    xtickMax = max([max(i) for i in x.values()])
    xtickgrp = random.randint(4,8)
    xstep = float(float(xtickMax)/float(xtickgrp))
    ytickMax = max([max(i) for i in y.values()])
    ytickgrp = random.randint(4,8)
    ystep = float(float(ytickMax)/float(ytickgrp))
    
    #legColor = colormapProperties(1)
    #leg.get_frame().set_facecolor(legColor)  
    rotationXTicks = random.choice([45,90,-90,-45,None])
    rotationYTicks = random.choice([45,90,-90,-45,None])
    chartFeatures = [XLabel,YLabel,xposX,yposX,xposY,yposY,legXLoc,legYLoc,legbboxX,legbboxY,fontrand,xtickMax,xtickgrp,xstep,ytickMax,ytickgrp,ystep,rotationXTicks,rotationYTicks,legboxh,legboxw]
    return XLabel,YLabel,xposX,yposX,xposY,yposY,legXLoc,legYLoc,legbboxX,legbboxY,fontrand,xtickMax,xtickgrp,xstep,ytickMax,ytickgrp,ystep,rotationXTicks,rotationYTicks,legboxh,legboxw
    

def colormapProperties(noOfColorsReq):
    colorMapList =['viridis','plasma','inferno','magma','cividis']
    #print colorMapList
    #color = matplotlib.colors.Colormap('viridis', N=255)
    #print(color)
    colorMapItem = random.choice(colorMapList)
    cmap = plt.get_cmap(colorMapItem)
    colors = cmap(np.linspace(0, 1, noOfColorsReq))
    return colors
      
def LineChartPlot(x,y,N,count):
    global tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend
    global lineChartProperties
    global XYlabelProperties
    global XYTickProperties
    global legendProperties
    global fontrand
    XYlabelProperties={}
    lineChartProperties ={}
    XYTickProperties ={}
    legendProperties = {}
    mydpi=144
    fig = plt.figure(figsize = (6,6))    
    #fig.canvas.draw() 
    ax = fig.subplots()    
    linestyles = ['-', '--', '-.', ':']
    lineMarkers = {"point":".",	"pixel":",", "circle":"o", "triangle_down":"v", "triangle_up":"^", "triangle_left":"<", "triangle_right":">", "tri_down":"1", "tri_up":"2", "tri_left":"3", "tri_right":"4", "octagon":"8", "square":"s", "pentagon":"p", "plus (filled)":"P", "star":"*", "hexagon1":"h", "hexagon2":"H", "plus":"+", "x":"x", "x(filled)":"X", "diamond":"D", "thin_diamond":"d", "vline":"|", "hline":"_","None":"None"}   
    colors = colormapProperties(N)
    methodLabels = random.sample(set(labelsDict),N)
    p = []
    for i in range(N):
        lineChartProperties[i]={}
        lineSty = random.choice(linestyles)
        linemarker = lineMarkers[str(random.choice(list(lineMarkers.keys())))]
        p1, = plt.plot(x[i],y[i],label = methodLabels[i],linestyle=lineSty, marker=linemarker, color=colors[i]) 
        p.append(p1)
        lineChartProperties[i]["linestyle"]=lineSty
        lineChartProperties[i]["methodlabel"]=methodLabels[i]
        lineChartProperties[i]["linemarker"]=linemarker
        lineChartProperties[i]["linecolor"]=colors[i]
    XLabel,YLabel,xposX,yposX,xposY,yposY,legXLoc,legYLoc,legbboxX,legbboxY,fontrand,xtickMax,xtickgrp,xstep,ytickMax,ytickgrp,ystep,rotationXTicks,rotationYTicks,legboxh,legboxw = ChartProperties(x,y,N,p)
    boxX = {"facecolor": "yellow", "pad": 1,"edgecolor":"black"}
    boxY = {"facecolor": "white", "pad": 1,"edgecolor":"blue"}
    
    ax.set_xlabel(XLabel,fontsize = fontrand,bbox=None)
    ax.xaxis.set_label_coords(xposX, yposX, transform=None)
    
    ax.set_ylabel(YLabel,fontsize = fontrand,bbox=None)
    ax.yaxis.set_label_coords(xposY, yposY, transform=None) 
    
    plt.xticks(np.arange(0,xtickMax+1,xstep),rotation=rotationXTicks)
    plt.yticks(np.arange(0,ytickMax+1,ystep),rotation = rotationYTicks)
    
    
    
    XYTickProperties["xticks"]=np.arange(0,xtickMax+1,xstep)
    XYTickProperties["xticksRT"] = rotationXTicks
    XYTickProperties["xticksMax"] = xtickMax
    XYTickProperties["xticksMin"] = "0"
    XYTickProperties["xstep"]=xstep
    
    XYTickProperties["yticks"]=np.arange(0,ytickMax+1,ystep)
    XYTickProperties["yticksRT"] = rotationYTicks
    XYTickProperties["yticksMax"] = ytickMax
    XYTickProperties["yticksMin"] = "0"
    XYTickProperties["ystep"]=ystep
    #ax.set_xscale('linear')
    #ax.set_yscale('linear')
    #s1= ax.get_yticks()
    #s2= ax.get_xticks()
    #print s1,s2
    #,bbox_to_anchor=(legbboxX, legbboxX,0,0)
    leg = plt.legend(handles= p, loc = 'lower left',fontsize = fontrand,bbox_to_anchor=(legXLoc, legYLoc, legboxw, legboxh))
    print("set",(legXLoc, legYLoc, legboxw, legboxh))
    figure=leg.figure
    figure.canvas.draw()
    bbox_  = leg.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    xmin=bbox_.xmin
    xmax=bbox_.xmax
    ymin=bbox_.ymin
    ymax=bbox_.ymax
    print("bbox_",xmin,xmax,ymin,ymax)
    print("transformed",)
    fig.savefig("legend", bbox_inches=bbox_,dpi=mydpi)#dpi="figure"
    rendererIns = fig.canvas.get_renderer()
    fig.canvas.draw()
    #print(ax.yaxis.get_tightbbox())
    tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    # plt.add_patch(
    #         patches.Rectangle((x0, y0), width, height, color='r',
    #                         fill=False, transform=ax.transAxes)
    #leg.set_bbox_to_anchor((legbboxX,legbboxY,0.2,0.6))#, transform=None)
    XYlabelProperties["XLabel"]=XLabel
    XYlabelProperties["YLabel"]=YLabel
    XYlabelProperties["xposX"]=xposX
    XYlabelProperties["yposX"]=yposX
    XYlabelProperties["Xbbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    XYlabelProperties["xposY"]=xposY
    XYlabelProperties["yposY"]=yposY
    XYlabelProperties["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    XYlabelProperties["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    legendProperties["Xloc"] = legXLoc
    legendProperties["Yloc"]=legXLoc
    legendProperties["legbboxX"]=legbboxX
    legendProperties["legbboxY"] = legbboxY
    legendProperties["legboxh"] = legboxh
    legendProperties["legboxw"] = legboxw
    legendProperties["legPixelBbox"]={"x1":bbox_legend.x0,"y1":bbox_legend.y0,"x2":bbox_legend.x1,"y2":bbox_legend.y1}
    legendProperties["fontsize"] = fontrand
    
    #XYTickProperties["xticks"]=np.arange(0,xtickMax+1,xstep)
    
    #bbox_legend = leg.get_bbox_to_anchor()
    #print(ax.xaxis.get_label_bbox())
    print(tight_bbox_raw_x)
    print (tight_bbox_raw_y)
    print (bbox_legend)
    
    # plt.tight_layout()
    plt.savefig(("LineCharts/"+str(N)+"_line_"+str(count)+".png"),dpi=mydpi)#,bbox_inches ="tight")
    matplotlib.pyplot.close()
    
    #plt.show()
    
def saveData(xml_file,fileId,numOfMethods):
#     userelement = xml.Element("linechart")
#     root.append(userelement)
#     uid = xml.SubElement(userelement, "LineId",attrib={"id":fileId})
#     noOfLine = xml.SubElement(userelement, "No_Of_Line", attrib={"count":str(numOfMethods)})
#     lineFunction = xml.SubElement(userelement,"LineFunction",attrib={"function":lineFunc})
#     NoOfDataP = xml.SubElement(userelement,"No_Of_DataPoints",attrib={"count":str(NoOfDP)})
    
#     data = xml.SubElement(userelement, "data")
#     for i in range(numOfMethods):
#         rawData =xml.SubElement(data,"method",attrib={"id":str(i),"methodlabel":str((lineChartProperties[i])["methodlabel"])})
#         for j in range(NoOfDP):
#             val = xml.SubElement(rawData,"datapoints",attrib={"id":str(j),"x":str((x_final[i])[j]),"y":str((y_final[i])[j])})
#         linestyleTag =xml.SubElement(rawData,"lineproperties",attrib={"linestyle":str((lineChartProperties[i])["linestyle"]),"linemarker":str((lineChartProperties[i])["linemarker"]),"linecolor":(str(((lineChartProperties[i])["linecolor"])[0])+","+str(((lineChartProperties[i])["linecolor"])[1])+","+str(((lineChartProperties[i])["linecolor"])[2])+","+str(((lineChartProperties[i])["linecolor"])[3]))}) 
#     xlabelTag = xml.SubElement(userelement, "XLabel",attrib={"xlabel":str(XYlabelProperties["XLabel"]), "fontsize":str(fontrand),"xpos":str(XYlabelProperties["xposX"]),"ypos":str(XYlabelProperties["yposX"]),"bbox":XYlabelProperties["Xbbox"]})
#     ylabelTag = xml.SubElement(userelement, "YLabel",attrib={"ylabel":str(XYlabelProperties["YLabel"]),"fontsize":str(fontrand), "xpos":str(XYlabelProperties["xposY"]),"ypos":str(XYlabelProperties["yposY"]),"bbox":XYlabelProperties["Ybbox"]})
    
#     legendTag = xml.SubElement(userelement, "legend",attrib={"xpos":str(legendProperties["Xloc"]), "ypos":str(legendProperties["Yloc"]), "Xbbox": str(legendProperties["legbboxX"]),"Ybbox":str(legendProperties["legbboxY"]),"fontsize":str(legendProperties["fontsize"]),"pixelBbox":str(legendProperties["legPixelBbox"])})
#     xtickTag = xml.SubElement(userelement, "xticks", attrib={"xmin":str(XYTickProperties["xticksMin"]),"xmax":str(XYTickProperties["xticksMax"]), "xstep": str(XYTickProperties["xstep"]), "rotation":str(XYTickProperties["xticksRT"])})
#     for k in range(len(XYTickProperties["xticks"])):
#         val = xml.SubElement(xtickTag,"value")
#         val.text = str((XYTickProperties["xticks"])[k])
#     ytickTag = xml.SubElement(userelement, "yticks", attrib={"ymin":str(XYTickProperties["yticksMin"]),"ymax":str(XYTickProperties["yticksMax"]), "ystep": str(XYTickProperties["xstep"]), "rotation":str(XYTickProperties["xticksRT"])})
#     for k in range(len(XYTickProperties["yticks"])):
#         val = xml.SubElement(ytickTag,"value")
#         val.text = str((XYTickProperties["yticks"])[k])
    
#     tree = xml.ElementTree(root)
#     with open(xml_file, "wb+") as xmlf:
#         tree.write(xmlf)
    # make_json_type1()
    make_csv_type2()
 
# def make_json_type1():
#     #global json_images
#     rects = []
#     one_decimal = "{0:0.1f}"
#     bbox_list = [tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend]
#     for i in range(3):
#         xmin = float(one_decimal.format(bbox_list[i].xmin()))
#         xmax = float(one_decimal.format(bbox_list[i].xmax()))
#         ymin = float(one_decimal.format(bbox_list[i].ymin()))
#         ymax = float(one_decimal.format(bbox_list[i].ymax()))

#         #enforce x1,y1 = top left, x2,y2 = bottom right

#         # tlx = min(x1,x2)
#         # tly = min(y1,y2)
#         # brx = max(x1,x2)
#         # bry = max(y1,y2)

#         bbox = dict([("xmin",xmin),("ymin",ymin),("xmax",xmax),("ymax",ymax)])
#         rects.append(bbox)
#     print(rects)
#     json_image = dict([("image_path",("LineCharts/"+fileId+".png")),("rects",rects)])

#     json_images.append(json_image)
    
def make_csv_type2():
    #global json_images
    one_decimal = "{0:0.1f}"
    bbox_list = [tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend]
    classes = ["XAxisbbox","YAxisbbox","Legendbbox"]
    for i in range(3):
        xmin = bbox_list[i].xmin
        xmax = bbox_list[i].xmax
        ymin = bbox_list[i].ymin
        ymax = bbox_list[i].ymax

        #enforce x1,y1 = top left, x2,y2 = bottom right
        
        # tlx = min(x1,x2)
        # tly = min(y1,y2)
        # brx = max(x1,x2)
        # bry = max(y1,y2)

        image_path = str("LineCharts/"+fileId+".png")
        outfile_csv.writerow([image_path,str(int(xmin*1.44)),str(int(864-ymin*1.44)),str(int(xmax*1.44)),str(int(864-ymax*1.44)),classes[i]])

    
    
if __name__ == "__main__":
    line_foo = open("LineCharts/linechart_error_15001_20000.txt","w")
    xml_file = "LineCharts/linechart_xml_15001_20000.xml"
    outfile = open("linechart_json_15001_20000.json","w")
    outfile_csv = csv.writer(open("linechart_csv_15001_20000.csv","w"))
    root = xml.Element("LineCharts")
    outfile_csv.writerow(["image_path","xmin","ymin","xmax","ymax","class"])
    json_images=[]
    noOfPlots=20000
    for c in range(0,noOfPlots):
        try:
            numOfMethods = random.randint(2,5) #number of methods
            NoOfDP = random.randint(3,20) #number of data points
            x_gt ={}
            y_gt = {}
            for i in range(numOfMethods):
                x_gt[i]=[]
                y_gt[i]=[]
                #print x_gt,y_gt
            labelsDict = []
            XYlabels = open('XYlabels.txt','r')#,encoding="utf8")
            for line in XYlabels:
                line= line.rstrip()
                if len(line)<=20:
                    labelsDict.append(line)
                    
            x_final,y_final,lineFunc = LineChartNDataGen(x_gt,y_gt,numOfMethods,NoOfDP)      
            LineChartPlot(x_final,y_final,numOfMethods,c)  
            fileId = str(numOfMethods)+"_line_"+str(c)
            print(fileId)
            saveData(xml_file,fileId,numOfMethods)
        except Exception as e:
            print(e)
            line_foo.write("Failed {0}: {1}\n".format(str(c), str(e))+"\n")
            pass
            continue
    outfile.write(json.dumps(json_images, indent = 1))
    #outfile_csv.close()
    # line_foo.close()
            
        
    
