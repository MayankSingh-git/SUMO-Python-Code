import csv
import xml.etree.ElementTree as ET

# Define the input and output filenames
xml_filename = "fcd-2.xml"
csv_filename = "fcd_export-2.csv"

# Parse the XML file
tree = ET.parse(xml_filename)
root = tree.getroot()

# Open the CSV file for writing
with open(csv_filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row
    writer.writerow(["time", "vehicle_id", "x", "y", "angle", "type", "speed", "pos", "lane", "slope", "acceleration", "leaderID", "leaderSpeed", "leaderGap"])

    # Loop over the timesteps and vehicles
    for timestep in root.findall('timestep'):
        time = timestep.get('time')
        for vehicle in timestep.findall('vehicle'):
            vehicle_id = vehicle.get('id')
            x = vehicle.get('x')
            y = vehicle.get('y')
            angle = vehicle.get('angle')
            vtype = vehicle.get('type')
            speed = vehicle.get('speed')
            pos = vehicle.get('pos')
            lane = str(vehicle.get('lane'))
            slope = vehicle.get('slope')
            acceleration=vehicle.get('acceleration')
            leaderID=vehicle.get('leaderID')
            leaderSpeed=vehicle.get('leaderSpeed')
            leaderGap=vehicle.get('leaderGap')

            # Write the data row
            writer.writerow([time, vehicle_id, x, y, angle, vtype, speed, pos, lane, slope, acceleration, leaderID, leaderSpeed, leaderGap])
