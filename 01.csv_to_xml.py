import csv
import xml.etree.ElementTree as ET
import pandas as pd

# Define the CSV and XML filenames
csv_filename = "5. Right - Copy.csv"
# csv_filename = "Right Side Veh Density.csv"
xml_filename = "routefile.xml"

tracks_df = pd.read_csv("D:/ITS-2023/Scenario/05_tracks.csv",low_memory=False)
tracks_meta_df = pd.read_csv("D:\ITS-2023\Scenario\\5. Right - Copy.csv",low_memory=False)
# Create the root element of the XML tree
root = ET.Element("routes")


# Define the vehicle types
car_type = ET.SubElement(root, "vType", id="Car", sigma="0.5", maxSpeed="57.97", accel="1.3", speedDev="0.04", color="1,1,0")
truck_type = ET.SubElement(root, "vType", id="Truck", sigma="0.5", maxSpeed="39.6", accel="0.33", speedDev="0.03", color="1,0,0")
# car_type = ET.SubElement(root, "vType", id="Car", sigma="0.5", maxSpeed="48.39", color="1,1,0")
# truck_type = ET.SubElement(root, "vType", id="Truck", sigma="0.5", maxSpeed="34.86", color="1,0,0")



for i in range(len(tracks_meta_df)):
    # max_accel = tracks_df[tracks_df["id"]==i+1]["xAcceleration"].min()
    lane = tracks_df[tracks_df["id"]==i+1]["laneId"].iloc[0]

    vehicle_id = tracks_meta_df["id"].iloc[i]
    length = tracks_meta_df["length"].iloc[i]
    width = tracks_meta_df["width"].iloc[i]
    depart = tracks_meta_df["vehicle_insertion_time"].iloc[i]

    departspeed = tracks_meta_df["minXVelocity"].iloc[i]

    vehicle_type = tracks_meta_df["class"].iloc[i]
    angle = tracks_meta_df["Direction"].iloc[i]
    max_speed = tracks_meta_df["maxXVelocity"].iloc[i]

    # accel=str(max_accel),
    if (angle==0):

        vehicle = ET.SubElement(root, "vehicle", id=str(i+1), type=vehicle_type, length=str(length), width=str(width), 
                            depart=str(depart), departSpeed=str(departspeed), angle=str(angle), maxSpeed=str(max_speed),  departLane="random")
    else:
        vehicle = ET.SubElement(root, "vehicle", id=str(i+1), type=vehicle_type, length=str(length), width=str(width), 
                            depart=str(depart), departSpeed=str(departspeed), angle=str(angle), maxSpeed=str(max_speed), departLane="random")
    if angle == 0:
        route = ET.SubElement(vehicle, "route", edges="E0")
    else:
        route = ET.SubElement(vehicle, "route", edges="-E0")

    # Add a new line character after each vehicle tag
    #ET.SubElement(root, "\n")
# Write the XML file

tree = ET.ElementTree(root)
tree.write(xml_filename, encoding="utf-8", xml_declaration=True)
