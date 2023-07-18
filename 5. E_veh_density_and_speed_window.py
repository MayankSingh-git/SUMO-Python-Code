import csv


# Open the input CSV file and the output CSV file
with open(r'D:\\ITS-2023\\Scenario\\fcd_export.csv', 'r') as f_in:
    # Create CSV reader and writer objects
    reader = csv.DictReader(f_in)
    s = set()
    
    total_time = 1160 #always change its value to final time
    updated_total_time = total_time - 60
    tme = (updated_total_time // 5) + 2
    # tme = (updated_total_time // 10) + 2
    l = [0] * int(tme)
    m = [[] for _ in range(tme)]
    vehicle_ids= [[] for _ in range(tme)]
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

    num_vehicles=[]

    # and int(row['vehicle_id']) > 453
    for row in reader:
        # while float(row['vehicle_insertion_time']) < end_time:
        # print(row)
        if float(row['pos']) > 0 and float(row['pos'] )<= 400 and (row['lane']=='E0_0' or row['lane']=='E0_1'):
            for start, end in ranges:
                if start < (float(row['time'])) < end:
                    l[start // 5] += 1
                    m[start // 5].append(float(row['speed']))
                    vehicle_ids[start // 5].append(int(row['vehicle_id']))
                    # vehicle_ids_car[start // 5].append(int(row['vehicle_id']))

                    # l[start // 10] += 1
                    # m[start // 10].append(float(row['speed']))
                    # vehicle_ids[start // 10].append(int(row['vehicle_id']))

                    # s.add(float(row['vehicle_id']))
                    # num_vehicles.append(len(s))
    # writer = csv.writer(f_out)
    # writer.writerow(['#Minutes', '#Vehicles'])
    # for i, d in enumerate(l):
    #     writer.writerow([i+1, d])
    # print(l)

    non_empty_m = [lst for lst in m if lst]
    sum = 0
    for i in non_empty_m:
        for j in i:
            sum += j
        Velocity.append(sum / len(i))
        sum = 0

    
    for i in vehicle_ids:
        s=set()
        for j in i:
            s.add(j)
        num_vehicles.append(len(s))
    non_zero_num_vehicles = [num for num in num_vehicles if num != 0]
    # print(len(non_zero_num_vehicles))
    # print(len(Velocity))
    ranges = ranges[0:]
    # print(len(ranges))
    rows = zip(ranges, non_zero_num_vehicles,  Velocity)

    with open('E_Veh_Density_and_Velocity_Total-5.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Speed'])  # Write header row
        writer.writerows(rows)