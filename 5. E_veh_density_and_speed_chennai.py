import csv

with open(r'D:\\ITS-2023\\Scenario\\fcd_export-2.csv', 'r') as f_in:
    reader = csv.DictReader(f_in)

    num_vehicles=[]
    moped = []
    car = []
    bus = []
    rickshaw = []
    time = []

    mean_speed = []
    car_speed = []
    moped_speed = []
    bus_speed = []
    rickshaw_speed = []

    prev = 1800

    count = 0
    car_count = 0
    bus_count = 0
    moped_count = 0
    rickshaw_count = 0

    speed_sum = 0
    car_speed_sum = 0
    bus_speed_sum = 0
    moped_speed_sum = 0
    rickshaw_speed_sum = 0

    for row in reader:
        if float(row['time']) >= 1800 and float(row['time'] ) <= 3600 and float(row['pos']) > 245 and float(row['pos']) <= 490:
            next = float(row['time'])
            if prev == next:
                count += 1
                speed_sum += float(row['speed'])
                if row['type'] == 'car':
                    car_count += 1
                    car_speed_sum  += float(row['speed'])
                elif row['type'] == 'bus':
                    bus_count += 1
                    bus_speed_sum  += float(row['speed'])
                elif row['type'] == 'moped':
                    moped_count += 1
                    moped_speed_sum  += float(row['speed'])
                elif row['type'] == 'rickshaw':
                    rickshaw_count += 1
                    rickshaw_speed_sum  += float(row['speed'])
            else:
                time.append(int(float(row['time']))-1)
                num_vehicles.append(count)
                car.append(car_count)
                bus.append(bus_count)
                moped.append(moped_count)
                rickshaw.append(rickshaw_count)

                m_speed = speed_sum / count
                mean_speed.append(m_speed)

                if car_count != 0:
                    m_car_speed = car_speed_sum / car_count
                    car_speed.append(m_car_speed)
                else:
                    car_speed.append(0)

                if bus_count != 0:
                    m_bus_speed = bus_speed_sum / bus_count
                    bus_speed.append(m_bus_speed)
                else:
                    bus_speed.append(0)

                if moped_count != 0:
                    m_moped_speed = moped_speed_sum / moped_count
                    moped_speed.append(m_moped_speed)
                else:
                    moped_speed.append(0)

                if rickshaw_count != 0:
                    m_rickshaw_speed = rickshaw_speed_sum / rickshaw_count
                    rickshaw_speed.append(m_rickshaw_speed)
                else:
                    rickshaw_speed.append(0)

                count = 1
                if row['type'] == 'car':
                    car_count = 1
                else:
                    car_count = 0
                if row['type'] == 'bus':
                    bus_count = 1
                else:
                    bus_count = 0
                if row['type'] == 'moped':
                    moped_count = 1
                else:
                    moped_count = 0
                if row['type'] == 'rickshaw':
                    rickshaw_count = 1
                else:
                    rickshaw_count = 0

                speed_sum = float(row['speed'])
                if row['type'] == 'car':
                    car_speed_sum = float(row['speed'])
                else:
                    car_speed_sum = 0
                if row['type'] == 'bus':
                    bus_speed_sum = float(row['speed'])
                else:
                    bus_speed_sum = 0
                if row['type'] == 'moped':
                    moped_speed_sum = float(row['speed'])
                else:
                    moped_speed_sum = 0
                if row['type'] == 'rickshaw':
                    rickshaw_speed_sum = float(row['speed'])
                else:
                    rickshaw_speed_sum = 0

                prev = float(row['time'])


    rows = zip(time, num_vehicles, mean_speed, car, car_speed, bus, bus_speed, moped, moped_speed, rickshaw, rickshaw_speed)

    with open(r'Chennai-Analyis.csv', 'w', newline='') as f_out:
        writer = csv.writer(f_out)
        writer.writerow(['time', 'num_vehicles', 'mean_speed', 'car', 'car_speed','bus', 'bus_speed', 'moped', 'moped_speed', 'rickshaw', 'rickshaw_speed'])  # Write header row
        writer.writerows(rows)