import csv
# import pandas as pd

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

    j = [0] * int(tme)
    k = [0] * int(tme)
    l = [0] * int(tme)
    ma = [0] * int(tme)
    n = [0] * int(tme)
    o = [0] * int(tme)

    vl = [0] * int(tme)
    vma = [0] * int(tme)
    vn = [0] * int(tme)
    vo = [0] * int(tme)

    vvl = [0] * int(tme)
    vvma = [0] * int(tme)
    vvn = [0] * int(tme)
    vvo = [0] * int(tme)


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

    # for row in reader:
    #     # while float(row['vehicle_insertion_time']) < end_time:
    #     for start, end in ranges:
    #         if start < (float(row['T at D=20m'])) < end:
    #             j[start // 5] += 1
                

    
    # f_in.seek(0)
    # # field =next(reader1)
    # for row in reader1:
    #  # while float(row['vehicle_insertion_time']) < end_time:
    #     for start, end in ranges:
    #         if start < (float(row['T at D=50m'])) < end:
    #             k[start // 5] += 1
    
    
    # for row in reader1:
    #     for col in row:
    #         print(col)
        
        
        
        # print(type(row['T at D=50m']))
        # for value in range(len(row['T at D=50m'])):
            # print(row['T at D=50m'])

        # for start, end in ranges:
        #     velocity = []
                        # for value in range(len(row['T at D=50m'])):
            #     if(start <= float(row['T at D=50m']) and end>=float(row['T at D=50m'])):
            #         velocity.append(row['meanXVelocity'][value])
                    
            #     print(velocity)
            # with open(r'D:\ITS-2023\Scenario\temporary.csv', 'w', newline='') as f_out:
            #     writer = csv.writer(f_out)
            #     writer.writerow(['value'])  # Write header row
            #     writer.writerows(velocity)        

            # if start < (float(row['T at D=50m'])) < end:
            #     k[start // 5] += 1
    # dataframe = pd.read_csv(r'D:\\ITS-2023\\Scenario\\1. Right.csv')
    # print(dataframe)



    # f_in.seek(0)
    for row in reader2:
        # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=100m'])) < end:
                l[start // 5] += 1
                vl[start // 5] +=  (float(row['meanXVelocity']))

    f_in.seek(0)
    for row in reader3:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=200m'])) < end:
                ma[start // 5] += 1
                vma[start // 5] += (float(row['meanXVelocity']))
    
    f_in.seek(0)
    for row in reader4:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=300m'])) < end:
                n[start // 5] += 1
                vn[start // 5] += (float(row['meanXVelocity']))

    f_in.seek(0)
    for row in reader5:
    # while float(row['vehicle_insertion_time']) < end_time:
        for start, end in ranges:
            if start < (float(row['T at D=400m'])) < end:
                o[start // 5] += 1
                vo[start // 5] += (float(row['meanXVelocity']))

    for ms in range(len(vl)):
        vvl[ms] = vl[ms] / l[ms] 

    # for ms in range(len(vma)):
        vvma[ms] = vma[ms] / ma[ms] 

    # for ms in range(len(vn)):
        vvn[ms] = vn[ms] / n[ms] 

    # for ms in range(len(vo)):
        vvo[ms] = vo[ms] / o[ms] 
    
    
    # print(l)

    rows = zip(ranges, j,k,l,vvl,ma,vvma,n,vvn,o,vvo)

    with open(r'D:\ITS-2023\Scenario\D_Veh_Flow_Total-5_Right.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['Interval', 't@D=20m', 't@D=50m','t@D=100m' ,'v@D=100', 't@D=200m','v@D=200m','t@D=300m','v@D=300m', 't@D=400m','v@D=400m'])  # Write header row
        writer.writerows(rows)


