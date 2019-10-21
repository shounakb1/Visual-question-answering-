# FigCite

Requirements:

python>=2.7 <br/>
matplotlib<br/>
lxml<br/>
numpy<br/>


Instructions:<br/>
To run the above codes, we have make minor changes in few lines in the code. I have mentioned the lines below which you need to modify.

To run barChartGen.py file:<br/>

filename = "BarCharts/bar_xml_8001_10000.xml" #Stores information of each bar chart in xml format. <br/>
outfile = open("barchart_json_8001_10000.json","w") #Also store it in json format <br/>
outfile_csv = csv.writer(open("barchart_csv_8001_10000.csv","w")) #Storing it in csv format<br/>
NumberOfBarPlot = 10001 #change this variable to set the number of plots you want to generate<br/>

To run lineChartGen.py file:<br/>

xml_file = "LineCharts/linechart_xml_15001_20000.xml"<br/>
outfile = open("linechart_json_15001_20000.json","w")<br/>
outfile_csv = csv.writer(open("linechart_csv_15001_20000.csv","w"))<br/>
noOfPlots=12000 #set the number of charts you want to generate<br/>

To run pieChartGen.py file:

xml_file = "pie_xml_5000_10000.xml"<br/>
outfile = open("piechart_json_5000_10000.json","w")<br/>
outfile_csv = csv.writer(open("piechart_csv_5000_10000.csv","w"))<br/>
noOfPlot=2000 #set the number of charts you want to generate<br/>
