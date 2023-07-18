import csv
import xml.etree.ElementTree as ET

# Path to the XML file
xml_file = 'D:\ITS-2023\Scenario\d3.xml'


# Path to the output CSV file
csv_file = 'Total Flow-3.csv'

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Extract the column headers
columns = ["interval", "begin", "end", "id", "nVehContrib", "flow", "occupancy", "speed",
           "harmonicMeanSpeed", "length", "nVehEntered"]

# Create a CSV writer and write the column headers
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(columns)

    # Extract data from each interval and write to CSV
    for interval in root.findall('interval'):
        row = [interval.attrib.get(col) for col in columns]
        writer.writerow(row)

print("Conversion completed successfully!")
