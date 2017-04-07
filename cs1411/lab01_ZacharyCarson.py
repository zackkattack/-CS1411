#Name:Zachary Carson
#Course:CS 1411
#Date:1-30-17
#
#
#Problem:
#The Voyager 1 spacecraft, launched September 15, 1977, is the
#farthest-traveling Earth-made object. It is presently on the outer edges of
#our solar system. The NASA update page on September 25, 2009, reported it as
#being a distance of approximately 16,637,000,000 miles from the sun,
#traveling away from the sun at 38,241 miles/hour.
#
#Write a program that will prompt the user for an integer number that indicates
#the number of days after 9/25/09. You will calculate the distance of Voyager
#from the sun using numbers from 9/25/09 (assume that velocity is constant)
#plus the entered number of days, and report:
#
#Distance in miles
#Distance in kilometers (1.609344 kilometers/miles)
#Distance in astronomical units (AU, 92,955,887.6 miles/AU)
#Round trip time for radio communication in hours. Radio waves travel at the
#speed of light, listed at 299,792,458 meters/second.
#
#Given:
#Velocity of Voyager: 38,241 miles/hour
#Distance from sun at 9/25/09 : 16,637,000,000 miles
#kilometers to miles = 1.609344 kilometers/miles
#Astronomical Units = 92,955,887.6 miles/AU
#Speed of radio transmission = 299,792,458 meters/second
#
#Analysis
#Input: Integer number of days
#Outputs: Distance in miles, kilometers, Astronomical Units, round trip time for
#raido communication
#
#
#Method/Algorithm:
#Step 1: start
#Step 2: Get number of days
#Step 3: Convert number of days to hours
#Step 4: Distance in miles = 16637000000 + (hours*Velocity)
#Step 5: Distance in km = Distance in miles*1.609344
#Step 6: Distance in AU = Dististance miles/92955887.6
#Step 7: round trip distance for radio transmission = Distance in miles/299792458.
#       Time = float(2 * distance in miles/ velocty of radio transmission)) / 3600 seconds
#Step 8: Print out the distances in miles, kmm, Au and the time it takes for a
#       radio transmission
#Step 8: End
#
#TestCases:
#Input:60
#Expected OutPut:
#
#Total distance travled in miles: 16692067040 miles
#Total distance travled in kilometers:  26863277938.4 kilometersrf
#Total distance travled in Astronomical Units:   179.569766595 AU
#Round trip time for radio communication in seconds:645.1650 hours
#
#Input:4
#Expected Output:
#
#Total distance travled in miles:  16640671136 miles
#Total distance travled in kilometers:  26780564248.7 kilometers
#Total distance travled in Astronomical Units:  179.016860208 AU
#Round trip time for radio communication in hours:  643.1785 hours
#
#Write a comment about passing Testing results
#
#Program:

days_str = input("How many days has it been after 9/25/09? : ")
days_int = int(days_str)

velocity = 38241
hours = days_int * 24


Dist_miles = 16637000000 + (hours*velocity)
Dist_km = Dist_miles*1.609344
Dist_AU = Dist_miles/92955887.6
radio_Time = float((2*(Dist_km/299792458)))*3.6

print
print "Total distance travled in miles: ", format(Dist_miles, '.4f'), "miles"
print "Total distance travled in kilometers: ", format(Dist_km, '.4f'), "kilometers"
print "Total distance travled in Astronomical Units: ", format(Dist_AU, '.4f'),"AU"
print "Round trip time for radio communication in hours: ", format(radio_Time, '.4f'),"hours"
