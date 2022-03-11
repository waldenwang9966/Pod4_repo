from stations_challenge import * 

subway_station2 = SubwayStation(station_name='LaLaLa', location='W 5th ave and a house', lines=['5', '3', 'A', '45'])
subway_station2.show_info()


bus_station2 = BusStation(routes=['ThisWay', 'ThatWay', 'Nowhere'], open=False, station_name='Where TF Am I', location='Somewhere and maybe somewhere else')
bus_station2.show_info()


random_station = SubwayStation(station_name='A Planet', location='Far, far away', lines=['Here', 'Over', 'Under', 'i'])
random_station.show_info()
