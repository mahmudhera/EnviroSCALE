from time import sleep
import gps3

the_connection = gps3.GPSDSocket()
the_fix = gps3.Fix()

try:
    for new_data in the_connection:
        if new_data:
            the_fix.refresh(new_data)
        if not isinstance(the_fix.TPV['lat'], str):  # check for valid data
            speed = the_fix.TPV['speed']
            latitude = the_fix.TPV['lat']
            longitude = the_fix.TPV['lon']
            altitude = the_fix.TPV['alt']
	    with open('Lon_Lat_Alt_logs', 'a') as f:
            	print('Latitude:', latitude, 'Longitude:', longitude)
		f.write('Latittude: %f, Longitude: %f, Altitude: %f\n' % (latitude, longitude, altitude))
            sleep(2)
except KeyboardInterrupt:
    the_connection.close()
    print("\nTerminated by user\nGood Bye.\n")


