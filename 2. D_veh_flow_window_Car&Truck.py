import csv

############   FOR CAR & TRUCK   ###########

# Open the input CSV file and the output CSV file
with open(r'D:\\ITS-2023\\Scenario\\5. Right - Copy.csv', 'r') as f_in:
    # Create CSV reader and writer objects
    reader = csv.DictReader(f_in)
    reader1 = csv.DictReader(f_in)
    reader2 = csv.DictReader(f_in)
    reader3 = csv.DictReader(f_in)
    reader4 = csv.DictReader(f_in)
    reader5 = csv.DictReader(f_in)
    s = set()
    
    total_time = 1160            #always change its value to final time
    updated_total_time = total_time - 60
    tme = (updated_total_time // 5) + 2

    j_truck = [0] * int(tme)
    k_truck = [0] * int(tme)
    l_truck = [0] * int(tme)
    ma_truck = [0] * int(tme)
    n_truck = [0] * int(tme)
    o_truck = [0] * int(tme)

    j_car = [0] * int(tme)
    k_car = [0] * int(tme)
    l_car = [0] * int(tme)
    ma_car = [0] * int(tme)
    n_car = [0] * int(tme)
    o_car = [0] * int(tme)

    m = [[]for _ in range(tme)]
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
    string_column_name = 'class'
    # for row in reader:
    #     # while float(row['vehicle_insertion_time']) < end_time:
    #     for start, end in ranges:
    #         if start < (float(row['T at D=20m'])) < end:
    #             # print(row[string_column_name])
    #             if(row[string_column_name]=='Car'):
    #                 j_car[start // 5] += 1  
    #             else:
    #                 j_truck[start // 5] += 1  
                
    # print("hi")
    # f_in.seek(0)
    # for row in reader1:
    #     # while float(row['vehicle_insertion_time']) < end_time:
    #     for start, end in ranges:
    #         if start < (float(row['T at D=50m'])) < end:
    #             if(row[string_column_name]=='Car'):
    #                 k_car[start // 5] += 1  
    #             else:
    #                 k_truck[start // 5] += 1  

    f_in.seek(0)
    for row in reader2:
        # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=100m'])) < end:
                if(row[string_column_name]=='Car'):
                    l_car[start // 5] += 1  
                else:
                    l_truck[start // 5] += 1  

    f_in.seek(0)
    for row in reader3:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=200m'])) < end:
                if(row[string_column_name]=='Car'):
                    ma_car[start // 5] += 1  
                else:
                    ma_truck[start // 5] += 1  
    
    f_in.seek(0)
    for row in reader4:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=300m'])) < end:
                if(row[string_column_name]=='Car'):
                    n_car[start // 5] += 1  
                else:
                    n_truck[start // 5] += 1  

    f_in.seek(0)
    for row in reader5:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=400m'])) < end:
                if(row[string_column_name]=='Car'):
                    o_car[start // 5] += 1  
                else:
                    o_truck[start // 5] += 1  


    # print(l)
    rows_car = zip(ranges, j_car,k_car,l_car,ma_car,n_car,o_car)
    rows_truck = zip(ranges, j_truck,k_truck,l_truck,ma_truck,n_truck,o_truck)

    with open(r'D:\ITS-2023\Scenario\D_Veh_Flow_Car-5_Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 't@D=20m', 't@D=50m','t@D=100m' , 't@D=200m', 't@D=300m', 't@D=400m'])  # Write header row
        writer.writerows(rows_car)

    with open(r'D:\ITS-2023\Scenario\D_Veh_Flow_Truck-5_Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 't@D=20m', 't@D=50m','t@D=100m' , 't@D=200m', 't@D=300m', 't@D=400m'])  # Write header row
        writer.writerows(rows_truck)

