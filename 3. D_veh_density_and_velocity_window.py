import csv


# Open the input CSV file and the output CSV file
with open(r'D:\\ITS-2023\\Scenario\\5. Right - Copy.csv', 'r') as f_in:
    # Create CSV reader and writer objects
    reader = csv.DictReader(f_in)
    s = set()
    
    total_time = 1160 #always change its value to final time
    updated_total_time = total_time - 60
    tme = (updated_total_time // 5) + 2
    # tme = (updated_total_time // 10) + 1
    l = [0] * int(tme)
    m = [[] for _ in range(tme)]
    init_time = 0
    end_time = 60
    Velocity = []
    total_size = tme
    ranges = []
    increment = 60
    start = 0

    for _ in range(total_size):
        end = start + increment
        ranges.append((start, end))
        start += 5
        # start += 10

 
    for row in reader:
        # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['vehicle_insertion_time'])) < end:
                l[start // 5] += 1
                m[start // 5].append(float(row['meanXVelocity']))
                # l[start // 10] += 1
                # m[start // 10].append(float(row['meanXVelocity']))

    sum = 0
    for i in m:
        for j in i:
            sum += j
        if(len(i)==0):
            Velocity.append(0)
        else:
            Velocity.append(sum / len(i))
        # Velocity.append(sum / len(i))
        sum = 0
    

    rows = zip(ranges, l,  Velocity)

    with open('D_Veh_Density & Velocity_Total-5. Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Velocity'])  # Write header row
        writer.writerows(rows)