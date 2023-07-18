import csv

############   FOR CAR & TRUCK   ###########

# Open the input CSV file and the output CSV file
with open(r'D:\\ITS-2023\\Scenario\\5. Right - Copy.csv', 'r') as f_in:
    # Create CSV reader and writer objects
    reader = csv.DictReader(f_in)
    s = set()
    
    total_time = 1160 #always change its value to final time
    updated_total_time = total_time - 60
    tme = (updated_total_time // 5) + 2

    l_car = [0] * int(tme)
    m_car = [[] for _ in range(tme)]

    l_truck = [0] * int(tme)
    m_truck = [[] for _ in range(tme)]

    init_time = 0
    end_time = 60
    # Velocity = []
    Velocity_car=[]
    Velocity_truck=[]
    total_size = tme
    ranges = []
    increment = 60
    start = 0

    for _ in range(total_size):
        end = start + increment
        ranges.append((start, end))
        start += 5

    string_column_name = 'class'
    for row in reader:
        # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['vehicle_insertion_time'])) < end:
                if(row[string_column_name]=='Car'):
                    l_car[start // 5] += 1
                    m_car[start // 5].append(float(row['meanXVelocity']))  
                else:
                   l_truck[start // 5] += 1
                   m_truck[start // 5].append(float(row['meanXVelocity']))

 
    sum = 0
    for i in m_car:
        for j in i:
            sum += j
        if(len(i)==0):
            Velocity_car.append(0)
        else:
            Velocity_car.append(sum / len(i))
        sum = 0

    sum = 0
    for i in m_truck:
        for j in i:
            sum += j
        if(len(i)==0):
            Velocity_truck.append(0)
        else:
            Velocity_truck.append(sum / len(i))
        sum = 0
    

    rows_car = zip(ranges, l_car,  Velocity_car)
    rows_truck = zip(ranges, l_truck,  Velocity_truck)

    with open('D_Veh_Density & Velocity_Car-5. Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Velocity'])  # Write header row
        writer.writerows(rows_car)

    with open('D_Veh_Density & Velocity_Truck-5. Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Velocity'])  # Write header row
        writer.writerows(rows_truck)