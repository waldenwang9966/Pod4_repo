from tkinter.messagebox import showinfo
from stations_challenge import *

subway_station2 = SubwayStation(station_name='Time Travel Portal', location='123 17th Street', lines=['303','222','20-C'])
subway_station2.show_info()

busStation2 = BusStation(routes=['Middle of Nowhere, Hope You Get There, WTF!'], open='closed', close=TRUE, station_name='How did I get here?', location='Are we there yet!')
busStation2.show_info()

secret_station = SubwayStation(station_name='Mind Your Own Business', location='In between Here and There', lines=['Your Wildest Dreams, Your Worst Nightmare, Lucid Dreams'])
secret_station.show_info()