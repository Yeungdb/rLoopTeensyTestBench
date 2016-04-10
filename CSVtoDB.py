#!/usr/bin/python

#import serial
import psycopg2

#Teensy = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

try:
    conn = psycopg2.connect("dnmae='rLoop' user='rloop' host='localhost' password='rloop'")
except:
    print "Connection Failed"

cursor = conn.cursor()

file = open("Test.csv", "r")
line = file.readline();
while(1):
    lineString = line.split(",") #Taking the same string an processing it as if it was the Teensy stream
    counter = 0
    for strings in lineString: #After line is splitted with line.split, it creates an array to lineString
       print strings
       print """INSERT INTO DATA VALUES ((select SID from Sensor where SensorName = "Teensy"), {AID}, NOW(), {DATAVAL})""".format(AID=counter, DATAVAL=float(strings))
       cursor.execute("""INSERT INTO DATA VALUES ((select SID from Sensor where SensorName = "Teensy"), {AID}, NOW(), {DATAVAL})""".format(AID=counter, DATAVAL=float(strings)))
       counter+=1
