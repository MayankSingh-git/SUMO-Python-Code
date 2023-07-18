import csv

############   FOR CAR & TRUCK   ###########

# Open the input CSV file and the output CSV file
with open(r'D:\\ITS-2023\\Scenario\\fcd_export.csv', 'r') as f_in:
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

    vehicle_ids_car= [[] for _ in range(tme)]
    vehicle_ids_truck= [[] for _ in range(tme)]
    
    init_time = 0
    end_time = 60
   
    Velocity_car = []
    Velocity_truck = []

    total_size = tme
    ranges = []
    increment = 60
    start = 0

    for _ in range(total_size):
        end = start + increment
        ranges.append((start, end))
        start += 5

    num_vehicles_car=[]
    num_vehicles_truck=[]

    string_column_name = 'type'
    for row in reader:
        # while float(row['vehicle_insertion_time']) < end_time:
        # print(row)
        if float(row['pos']) > 0 and float(row['pos'] )<= 400 and (row['lane']=='E0_0' or row['lane']=='E0_1'):
            for start, end in ranges:
                if start < (float(row['time'])) < end:
                    if(row[string_column_name]=='Car'):
                        l_car[start // 5] += 1
                        m_car[start // 5].append(float(row['speed']))
                        vehicle_ids_car[start // 5].append(int(row['vehicle_id']))
                    else:
                        l_truck[start // 5] += 1
                        m_truck[start // 5].append(float(row['speed']))
                        vehicle_ids_truck[start // 5].append(int(row['vehicle_id']))
                    # s.add(float(row['vehicle_id']))
                    # num_vehicles.append(len(s))
   

   
    sum = 0             # Old Start
    for i in m_car:
        for j in i:
            sum += j
        Velocity_car.append(sum / len(i))
        sum = 0
    
    for i in vehicle_ids_car:
        s=set()
        for j in i:
            s.add(j)
        num_vehicles_car.append(len(s))
        
    sum = 0
    for i in m_truck:
        for j in i:
            sum += j
        Velocity_truck.append(sum / len(i))
        sum = 0
    
    for i in vehicle_ids_truck:
        s=set()
        for j in i:
            s.add(j)
        num_vehicles_truck.append(len(s))
        

    rows_car = zip(ranges, num_vehicles_car,  Velocity_car)
    rows_truck = zip(ranges, num_vehicles_truck,  Velocity_truck)   # Old End


    # non_empty_m_car = [lst for lst in m_car if lst]
    # sum = 0
    # for i in non_empty_m_car:
    #     for j in i:
    #         sum += j
    #     Velocity_car.append(sum / len(i))
    #     sum = 0

    
    # for i in vehicle_ids_car:
    #     s=set()
    #     for j in i:
    #         s.add(j)
    #     num_vehicles_car.append(len(s))
    # non_zero_num_vehicles_car = [num for num in num_vehicles_car if num != 0]
    # # print(len(non_zero_num_vehicles))
    # # print(len(Velocity))
    # ranges = ranges[169:]
    # # print(len(ranges))
    # rows_car = zip(ranges, non_zero_num_vehicles_car,  Velocity_car)

    # non_empty_m_truck = [lst for lst in m_truck if lst]
    # sum = 0
    # for i in non_empty_m_truck:
    #     for j in i:
    #         sum += j
    #     Velocity_truck.append(sum / len(i))
    #     sum = 0

    
    # for i in vehicle_ids_truck:
    #     s=set()
    #     for j in i:
    #         s.add(j)
    #     num_vehicles_truck.append(len(s))
    # non_zero_num_vehicles_truck = [num for num in num_vehicles_truck if num != 0]
    # # print(len(non_zero_num_vehicles))
    # # print(len(Velocity))
    # ranges = ranges[169:]
    # # print(len(ranges))
    # rows_truck = zip(ranges, non_zero_num_vehicles_truck,  Velocity_truck)


   
    with open('E_Veh_Density_and_Velocity_Car-5.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Speed'])  # Write header row
        writer.writerows(rows_car)
    
    with open('E_Veh_Density_and_Velocity_Truck-5.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 'Vehicles', 'Speed'])  # Write header row
        writer.writerows(rows_truck)