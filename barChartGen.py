# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 07:46:26 2018

@author: Rimi
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.transforms as tf
from collections import defaultdict
import xml.etree.ElementTree as xml
import math,csv,json,os
import matplotlib

SUBDIRECTORY="BarCharts"
try:
    os.mkdir(SUBDIRECTORY)
except Exception:
    pass

#keeping the data in xml format
def saveData(noOfDiffBars,barType,barStyle,XLabelProp,YLabelProp,XTicks,YTicks,rotationXTicks,rotationYTicks,legProp,WholeData,f,tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fontrand):
    #print(XTicks,YTicks)
    
    userelement = xml.Element("barchart")
    root.append(userelement)
    uid = xml.SubElement(userelement, "barId", attrib={"id":f,"type":barType,"style":barStyle})    

    NoOfBARS = xml.SubElement(userelement, "NoOfBars", attrib={"count":str(noOfDiffBars)})
    
    NoOfDataPoints = xml.SubElement(userelement, "NoOfDataPoints",attrib ={"count": str(N)})
    
    DATA = xml.SubElement(userelement, "data")
    #userelement.append(DATA)
    for i in range(len(WholeData.keys())):
        DATAdet = xml.SubElement(DATA, "method",attrib={"id":str(i),"methodlabel":str(WholeData[i]["method"])})
        #rawData =xml.SubElement(DATAdet,"datapoints",)
        for j in range(len((WholeData[i])["data"])):
            val = xml.SubElement(DATAdet,"datapoints",attrib={"id":str(j),"value":str((WholeData[i]["data"])[j])})
            #val.text = str((WholeData[i]["data"])[j])  
        barprop = xml.SubElement(DATAdet,"barproperties",attrib={"width":str(WholeData[i]["width"]),"color":str(str((WholeData[i]["color"])[0])+","+str((WholeData[i]["color"])[1])+","+str((WholeData[i]["color"])[2])+","+str((WholeData[i]["color"])[3]))})
    
    XLABEL = xml.SubElement(userelement, "XLabel", attrib={"xlabel":str(XLabelProp["xlabel"]),"fontsize":str(fontrand), "xpos":str(XLabelProp["xposX"]),"ypos":str(XLabelProp["yposX"]),"bbox":str(XLabelProp["Xbbox"])})
    
    YLABEL = xml.SubElement(userelement, "YLabel",attrib={"ylabel":str(YLabelProp["ylabel"]),"fontsize":str(fontrand), "xpos":str(YLabelProp["xposY"]),"ypos":str(YLabelProp["yposY"]),"bbox":str(YLabelProp["Ybbox"])})
    
    xtickTag = xml.SubElement(userelement, "xticks", attrib={"rotation":str(rotationXTicks)})   
    
    for k in range(len(XTicks)):
        val = xml.SubElement(xtickTag,"value")
        val.text = str(XTicks[k])
        
    ytickTag = xml.SubElement(userelement, "yticks", attrib={"rotation":str(rotationYTicks)}) 
    
    for k in range(len(YTicks)):
        val = xml.SubElement(ytickTag,"value")
        val.text = str(YTicks[k])
        
    legendTag = xml.SubElement(userelement, "legend",attrib={"xpos":str((legProp["legLoc"])[0]),  "ypos":str((legProp["legLoc"])[1]), "Xbbox":str((legProp["bbox"])[0]),"Ybbox":str((legProp["bbox"])[1]),"fontsize":str(legProp["fontsize"])})
    
    tree = xml.ElementTree(root)
    with open(filename, "wb+") as fh:
        tree.write(fh)
    make_json_type1(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,f)
    make_csv_type2(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,f)

#preparing the colors
def colormapProperties(noOfColorsReq):
    colorMapList =['viridis','plasma','inferno','magma','cividis']
    #print colorMapList
    #color = matplotlib.colors.Colormap('viridis', N=255)
    #print(color)
    colorMapItem = random.choice(colorMapList)
    cmap = plt.get_cmap(colorMapItem)
    colors = cmap(np.linspace(0, 1, noOfColorsReq))
    return colors



def barChart_stack(N,selectedLabels,count):
    
    #Selecting XLabels and YLabels
    XLabel = selectedLabels[0] #x-labels
    YLabel = selectedLabels[1]#y-labels
    
    #defining dpi and size of the figure
    mydpi=100
    fig = plt.figure(figsize = (6,4)) 
    ax = fig.subplots()
    
    data = defaultdict(list) #preparing data
    noOfDiffBars = random.randint(1, 6) #number of different type of bars
    methods = random.sample(set(labelsDict),noOfDiffBars)
    
    colors = colormapProperties(len(methods))
    #print(colors)
    
    #preparing ytick measurement
    ysumlist=[]
    for i in range(noOfDiffBars):
        ysum = 0
        for j in range(N):
            temp = random.uniform(0.1,1.5)
            ysum=ysum+temp
            data[i].append(temp)
        ysumlist.append(ysum)
    ymax = max(ysumlist)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence
    b=None
    p=[]
    WholeData = {} #storing the data in dictionary for each method
    m = 0
    for i in range(noOfDiffBars):
        WholeData[i]={}
        p1 = plt.bar(ind,data[i], width,bottom=b,color=colors[i])
        WholeData[i]["data"]=data[i]
        WholeData[i]["width"]=width
        WholeData[i]["color"]=colors[i]
        WholeData[i]["bottom"]=b
        WholeData[i]["method"]=methods[i]
        p.append(p1)
        b = data[i]
    #properties of XTicks    
    XTicks = []
    rotationXTicks = random.choice([45,90,-90,-45,None])
    rotationYTicks = random.choice([45,90,-90,-45,None])
    for i in range(N): #number of x data points
        XTicks.append(random.randint(1,50))
    #properties of YTicks
    ygrp = random.randint(4,7)
    ystep = float(ymax)/float(ygrp)
    YTicks = np.arange(0, ymax, ystep)
    plt.xticks(ind, XTicks,rotation=rotationXTicks)
    plt.yticks(YTicks,rotation=rotationYTicks)
    
    XLabelProp ={}
    YLabelProp = {}
    #properties of XLabels
    xposX = random.uniform(0.2,0.8)
    yposX = random.uniform(-0.05,-0.4)
    ax.set_xlabel(XLabel,fontsize = fontrand,bbox=None)
    ax.xaxis.set_label_coords(xposX, yposX, transform=None)
    XLabelProp["xposX"]=xposX
    XLabelProp["yposX"]=yposX
    XLabelProp["xlabel"]=XLabel
    XLabelProp["bbox"]="None"
    
    #properties of YLabels
    xposY = random.uniform(-0.08,-0.2)
    yposY = random.uniform(0.2,0.8)
    ax.set_ylabel(YLabel,fontsize = fontrand,bbox=None)
    ax.yaxis.set_label_coords(xposY, yposY, transform=None) 
    YLabelProp["xposY"]=xposY
    YLabelProp["yposY"]=yposY
    YLabelProp["ylabel"]=YLabel
    YLabelProp["bbox"]="None"
    
    #properties of Legend
    legProp={}
    legXLoc = random.uniform(0.1,0.7)
    legYLoc = random.uniform(0.2,0.72)
    legbboxX = random.uniform(0,0.9)
    legbboxY = random.uniform(0.3,0.7)
    fontrand = random.randint(7,12)
    
    leg = plt.legend(p, methods,loc = (legXLoc,legYLoc),bbox_to_anchor=(legbboxX, legbboxY),fontsize = fontrand)
    rendererIns = fig.canvas.get_renderer()
    #print(ax.yaxis.get_tightbbox())
    tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    #print(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend)
    
    XLabelProp["Xbbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    YLabelProp["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    
    
    legProp["legLoc"]=(legXLoc,legYLoc)
    legProp["bbox"]=(legbboxX, legbboxY)
    legProp["fontsize"]=fontrand
    legProp["pixelBbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}


    f =(str(noOfDiffBars)+"_bar_"+str(count))
    plt.savefig(("BarCharts/"+str(noOfDiffBars)+"_bar_"+str(count)+".png"))
    barType="vertical"
    barStyle = "stack"
    saveData(noOfDiffBars,barType,barStyle,XLabelProp,YLabelProp,XTicks,YTicks,rotationXTicks,rotationYTicks,legProp,WholeData,f,tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fontrand)
    plt.tight_layout()
    plt.savefig(("BarCharts/"+str(noOfDiffBars)+"_bar_"+str(count)+".png"),dpi=mydpi*10)
    matplotlib.pyplot.close()
    #plt.show()

def barhChart_stack(N,selectedLabels,count):
    XLabel = selectedLabels[0]
    YLabel = selectedLabels[1]
    
    mydpi=100
    fig = plt.figure(figsize = (6,4)) 
    ax = fig.subplots()
    
    data = defaultdict(list)
    noOfDiffBars = random.randint(1, 6)
    methods = random.sample(set(labelsDict),noOfDiffBars)
    
    colors = colormapProperties(len(methods))
    #print(colors)
    
    ysumlist=[]
    for i in range(noOfDiffBars):
        ysum = 0
        for j in range(N):
            temp = random.uniform(0.1,1)
            ysum = ysum+temp
            data[i].append(temp)
        ysumlist.append(ysum)
    ymax = max(ysumlist)
    
    ind = np.arange(N)    # the x locations for the groups
    width = random.choice([0.2,0.3,0.35,0.4])       # the width of the bars: can also be len(x) sequence
    
    p=[]
    WholeData = {}
    for i in range(noOfDiffBars):
        WholeData[i]={}
        p1 = plt.barh(ind,data[i], width,color=colors[i])
        WholeData[i]["data"]=data[i]
        WholeData[i]["width"]=width
        WholeData[i]["color"]=colors[i]
        WholeData[i]["bottom"]="None"
        WholeData[i]["method"]=methods[i]
        p.append(p1)
    
    XTicks = []
    rotationXTicks = random.choice([45,90,-90,-45,None])
    rotationYTicks = random.choice([45,90,-90,-45,None])
    for i in range(N):
        XTicks.append(random.randint(1,50))   
    ygrp = random.randint(4,7)
    ystep = float(ymax)/float(ygrp)
    YTicks = np.arange(0, ymax+1, ystep)    
    plt.yticks(ind,XTicks,rotation=rotationXTicks)
    plt.xticks(YTicks,rotation = rotationYTicks)
    
    fontrand = random.randint(7,12)
    
    XLabelProp ={}
    YLabelProp = {}
    xposX = random.uniform(0.2,0.8)
    yposX = random.uniform(-0.05,-0.4)
    ax.set_xlabel(XLabel,fontsize = fontrand,bbox=None)
    ax.xaxis.set_label_coords(xposX, yposX, transform=None)
    XLabelProp["xposX"]=xposX
    XLabelProp["yposX"]=yposX
    XLabelProp["xlabel"]=XLabel
    XLabelProp["bbox"]="None"
    
    
    xposY = random.uniform(-0.08,-0.2)
    yposY = random.uniform(0.2,0.8)
    ax.set_ylabel(YLabel,fontsize = fontrand,bbox=None)
    ax.yaxis.set_label_coords(xposY, yposY, transform=None) 
    YLabelProp["xposY"]=xposY
    YLabelProp["yposY"]=yposY
    YLabelProp["ylabel"]=YLabel
    YLabelProp["bbox"]="None"
    
    legProp={}
    legXLoc = random.uniform(0.1,0.7)
    legYLoc = random.uniform(0.2,0.72)
    legbboxX = random.uniform(0,0.9)
    legbboxY = random.uniform(0.3,0.7)
   
    leg = plt.legend(p, methods,loc = (legXLoc,legYLoc),bbox_to_anchor=(legbboxX, legbboxY),fontsize = fontrand)
    
    rendererIns = fig.canvas.get_renderer()
    #print(ax.yaxis.get_tightbbox())
    tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    #print(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend)
    
    XLabelProp["Xbbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    YLabelProp["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    
    
    legProp["legLoc"]=(legXLoc,legYLoc)
    legProp["bbox"]=(legbboxX, legbboxY)
    legProp["fontsize"]=fontrand
    legProp["pixelBbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}

    
    barType="horizontal"
    barStyle = "stack"
    f =(str(noOfDiffBars)+"_bar_"+str(count))
    saveData(noOfDiffBars,barType,barStyle,XLabelProp,YLabelProp,YTicks,XTicks,rotationXTicks,rotationYTicks,legProp,WholeData,f,tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fontrand)
    plt.tight_layout()
    plt.savefig(("BarCharts/"+str(noOfDiffBars)+"_bar_"+str(count)+".png"),dpi=mydpi*10)
    matplotlib.pyplot.close()
    #plt.show()


def barChart_group(N,selectedLabels,count): 
    XLabel = selectedLabels[0]
    YLabel = selectedLabels[1]
    XTicks = []
    
    mydpi=100
    fig = plt.figure(figsize = (6,4)) 
    ax = fig.subplots()

    data = defaultdict(list)
    noOfDiffBars = random.randint(1, 6)
    methods = random.sample(set(labelsDict),noOfDiffBars)
    
    colors = colormapProperties(len(methods))
    
    for i in range(noOfDiffBars):
        for j in range(N):
            data[i].append(random.uniform(1,4))
    
    ind = np.arange(N)    # the x locations for the groups
    width = random.choice([0.2,0.3,0.35,0.4]) 
    #print ind
    p=[]
    xLoc =ind
    WholeData ={}
    for i in range(noOfDiffBars):
        WholeData[i]={}
        p1 = plt.bar(xLoc,data[i], width,bottom=0,color=colors[i])
        WholeData[i]["data"]=data[i]
        WholeData[i]["width"]=width
        WholeData[i]["color"]=colors[i]
        WholeData[i]["bottom"]=0
        WholeData[i]["method"]=methods[i]
        p.append(p1)
        xLoc= xLoc+ width
    #print(ind) 
    
    rotationXTicks = random.choice([45,90,-90,-45,None])
    rotationYTicks = random.choice([45,90,-90,-45,None])
    for i in range(N):
        XTicks.append(random.randint(1,50))
    XTicks = (ind+width/2)
    ymax = 0
    for i in range(len(WholeData.keys())):
        for j in range(len(WholeData[i]["data"])):
            if (WholeData[i]["data"])[j]>ymax:
                ymax =(WholeData[i]["data"])[j] 
    ygrp = random.randint(4,7)
    ystep = float(ymax)/float(ygrp)        
    YTicks = np.arange(0, ymax, ystep)
    plt.xticks(XTicks,rotation = rotationXTicks)
    plt.yticks(YTicks,rotation = rotationYTicks)
    
    fontrand = random.randint(7,12)
    XLabelProp ={}
    YLabelProp = {}
    xposX = random.uniform(0.2,0.8)
    yposX = random.uniform(-0.05,-0.4)
    ax.set_xlabel(XLabel,fontsize= fontrand,bbox=None)
    ax.xaxis.set_label_coords(xposX, yposX, transform=None)
    XLabelProp["xposX"]=xposX
    XLabelProp["yposX"]=yposX
    XLabelProp["xlabel"]=XLabel
    XLabelProp["bbox"]="None"
    
    
    xposY = random.uniform(-0.08,-0.2)
    yposY = random.uniform(0.2,0.8)
    ax.set_ylabel(YLabel,bbox=None)
    ax.yaxis.set_label_coords(xposY, yposY, transform=None) 
    YLabelProp["xposY"]=xposY
    YLabelProp["yposY"]=yposY
    YLabelProp["ylabel"]=YLabel
    YLabelProp["bbox"]="None"
    
    legProp={}
    legXLoc = random.uniform(0.1,0.7)
    legYLoc = random.uniform(0.2,0.72)
    legbboxX = random.uniform(0,0.9)
    legbboxY = random.uniform(0.3,0.7)
    #fontrand = random.randint(7,12)
    leg = plt.legend(p, methods,loc = (legXLoc,legYLoc),bbox_to_anchor=(legbboxX, legbboxY),fontsize = fontrand)
    
    rendererIns = fig.canvas.get_renderer()
    #print(ax.yaxis.get_tightbbox())
    tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    #print(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend)
    
    XLabelProp["Xbbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    YLabelProp["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    
    legProp["legLoc"]=(legXLoc,legYLoc)
    legProp["bbox"]=(legbboxX, legbboxY)
    legProp["fontsize"]=fontrand
    legProp["pixelBbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}

    barType="vertical"
    barStyle = "group"
    f =(str(noOfDiffBars)+"_bar_"+str(count))
    saveData(noOfDiffBars,barType,barStyle,XLabelProp,YLabelProp,XTicks,YTicks,rotationXTicks,rotationYTicks,legProp,WholeData,f,tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fontrand)
    plt.tight_layout()
    plt.savefig(("BarCharts/"+str(noOfDiffBars)+"_bar_"+str(count)+".png"),dpi=mydpi*10)
    matplotlib.pyplot.close()
    #plt.show()
    
def barhChart_group(N,selectedLabels,count): 
    XLabel = selectedLabels[0]
    YLabel = selectedLabels[1]
    #print(XLabel,YLabel)
    #fig = plt.figure()    
    
    mydpi=100
    fig = plt.figure(figsize = (6,4)) 
    ax = fig.subplots()
    
    
    data = defaultdict(list)
    noOfDiffBars = random.randint(1, 6)
    methods = random.sample(set(labelsDict),noOfDiffBars)
    
    colors = colormapProperties(len(methods))
    #print(colors)
    
    for i in range(noOfDiffBars):
        for j in range(N):
            data[i].append(random.uniform(1,2))
            
    ind = np.arange(N)    # the x locations for the groups
    width = random.choice([0.2,0.3,0.35,0.4]) 
    p=[]
    xLoc =ind
    WholeData = {}
    for i in range(noOfDiffBars):
        WholeData[i]={}
        p1 = plt.barh(xLoc,data[i], width,color=colors[i])
        #p1.set_hatch(random.choice(patterns))
        WholeData[i]["data"]=data[i]
        WholeData[i]["width"]=width
        WholeData[i]["color"]=colors[i]
        WholeData[i]["bottom"]=0
        WholeData[i]["method"]=methods[i]
        p.append(p1)
        xLoc= xLoc+ width
    #print(ind) 
    
    XTicks = []
    rotationXTicks = random.choice([45,90,-90,-45,None])
    rotationYTicks = random.choice([45,90,-90,-45,None])
    for i in range(N):
        XTicks.append(random.randint(1,50))
    XTicks = (ind+width/ 2)
    ymax = 0
    for i in range(len(WholeData.keys())):
        for j in range(len(WholeData[i]["data"])):
            if (WholeData[i]["data"])[j]>ymax:
                ymax =(WholeData[i]["data"])[j] 
    ygrp = random.randint(4,7)
    ystep = float(ymax)/float(ygrp)        
    YTicks = np.arange(0, ymax, ystep)
    plt.yticks(XTicks,rotation = rotationXTicks)
    plt.xticks(YTicks,rotation = rotationYTicks)
    
    fontrand = random.randint(7,12)
    XLabelProp ={}
    YLabelProp = {}
    xposX = random.uniform(0.2,0.8)
    yposX = random.uniform(-0.05,-0.4)
    ax.set_xlabel(XLabel,fontsize =fontrand,bbox=None)
    ax.xaxis.set_label_coords(xposX, yposX, transform=None)
    XLabelProp["xposX"]=xposX
    XLabelProp["yposX"]=yposX
    XLabelProp["xlabel"]=XLabel
    XLabelProp["bbox"]="None"
    
    
    xposY = random.uniform(-0.08,-0.2)
    yposY = random.uniform(0.2,0.8)
    ax.set_ylabel(YLabel,fontsize =fontrand,bbox=None)
    ax.yaxis.set_label_coords(xposY, yposY, transform=None) 
    YLabelProp["xposY"]=xposY
    YLabelProp["yposY"]=yposY
    YLabelProp["ylabel"]=YLabel
    YLabelProp["bbox"]="None"
    
    legProp={}
    legXLoc = random.uniform(0.1,0.7)
    legYLoc = random.uniform(0.2,0.72)
    legbboxX = random.uniform(0,0.9)
    legbboxY = random.uniform(0.3,0.7)
    #fontrand = random.randint(7,12)
    leg = plt.legend(p, methods,loc = (legXLoc,legYLoc),bbox_to_anchor=(legbboxX, legbboxY),fontsize = fontrand)
    
    rendererIns = fig.canvas.get_renderer()
    #print(ax.yaxis.get_tightbbox())
    tight_bbox_raw_x = ax.xaxis.get_tightbbox(rendererIns)
    tight_bbox_raw_y = ax.yaxis.get_tightbbox(rendererIns)
    bbox_legend = leg.get_window_extent(rendererIns)
    #print(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend)
    
    XLabelProp["Xbbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    YLabelProp["Ybbox"]={"x1":tight_bbox_raw_y.x0,"y1":tight_bbox_raw_y.y0,"x2":tight_bbox_raw_y.x1,"y2":tight_bbox_raw_y.y1}
    
    legProp["legLoc"]=(legXLoc,legYLoc)
    legProp["bbox"]=(legbboxX, legbboxY)
    legProp["fontsize"]=fontrand
    legProp["pixelBbox"]={"x1":tight_bbox_raw_x.x0,"y1":tight_bbox_raw_x.y0,"x2":tight_bbox_raw_x.x1,"y2":tight_bbox_raw_x.y1}
    #plt.legend(p, methods,loc = selectedLoc)
    
    barType="horizontal"
    barStyle = "group"
    f =(str(noOfDiffBars)+"_bar_"+str(count))
    saveData(noOfDiffBars,barType,barStyle,XLabelProp,YLabelProp,YTicks,XTicks,rotationXTicks,rotationYTicks,legProp,WholeData,f,tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fontrand)
    plt.tight_layout()
    plt.savefig(("BarCharts/"+str(noOfDiffBars)+"_bar_"+str(count)+".png"),dpi=mydpi*10)
    matplotlib.pyplot.close()
    #plt.show()


def make_json_type1(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fileId):
    #global json_images
    rects = []
    one_decimal = "{0:0.1f}"
    bbox_list = [tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend]
    for i in range(3):
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
    #print(rects)
    json_image = dict([("image_path",("BarCharts/"+fileId+".png")),("rects",rects)])

    json_images.append(json_image)
    
def make_csv_type2(tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend,fileId):
    #global json_images
    one_decimal = "{0:0.1f}"
    bbox_list = [tight_bbox_raw_x,tight_bbox_raw_y,bbox_legend]
    classes = ["XAxisbbox","YAxisbbox","Legendbbox"]
    for i in range(3):
        x1 = float(one_decimal.format(bbox_list[i].x0))
        x2 = float(one_decimal.format(bbox_list[i].x1))
        y1 = float(one_decimal.format(bbox_list[i].y0))
        y2 = float(one_decimal.format(bbox_list[i].y1))

        #enforce x1,y1 = top left, x2,y2 = bottom right
        
        tlx = min(x1,x2)
        tly = min(y1,y2)
        brx = max(x1,x2)
        bry = max(y1,y2)
        image_path = str("BarCharts/"+fileId+".png")
        outfile_csv.writerow([image_path,str(tlx),str(tly),str(brx),str(bry),classes[i]])

  


if __name__ == "__main__":
    foo = open("BarCharts/error_file_bar_8001_10000.txt","w")
    filename = "BarCharts/bar_xml_8001_10000.xml"
    outfile = open("barchart_json_8001_10000.json","w")
    outfile_csv = csv.writer(open("barchart_csv_8001_10000.csv","w"))
    N=random.choice([3,4,5,6,7]) #Number of x data points
    barType = ["bar_stacked","barh_stacked","bar_grouped","barh_grouped"]
    json_images=[]
    labelsDict = []
    XYlabels = open('../XYlabels.txt','r')#,encoding="utf8")
    for line in XYlabels:
        line= line.rstrip()
        if len(line)<=20:
            labelsDict.append(line)
    
    #print selectedLabels
    NumberOfBarPlot = 10001
    root = xml.Element("BarCharts")
    #barChart_group(N,selectedLabels,1)
    for count in range(0,NumberOfBarPlot):
        print "Running No.",count
        selectedLabels = random.sample(set(labelsDict),2)
        try:
            selectedType = random.choice(barType)
            #selectedType = "barh_stacked"
            if selectedType == "bar_stacked":
                barChart_stack(N,selectedLabels,count)
            if selectedType == "barh_stacked":
                barhChart_stack(N,selectedLabels,count)
            if selectedType == "bar_grouped":
                barChart_group(N,selectedLabels,count)
            if selectedType == "barh_grouped":
                barhChart_group(N,selectedLabels,count)
        except Exception as e:
            #print e
            foo.write("Failed {0}: {1}\n".format(str(count), str(e)))
            pass
            continue
    outfile.write(json.dumps(json_images, indent = 1))
    foo.close()
    
  
