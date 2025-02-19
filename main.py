from serial import Serial
import datetime

# 000 - CO2
# 001 - CO
# 002 - NO2
# 003 - O2
# 004 - air quality PMS5003
# 005 - NOx Sensiron

if __name__ == '__main__':

    for filename in ["data_000.txt", "data_001.txt", "data_002.txt", "data_003.txt", "data_004.txt", "data_005.txt", "data_unknown.txt"]:
        open(filename, "w").close()

    serialReceived = Serial('COM7', 115200, timeout=1)

    while True:
        data = serialReceived.readline().decode('utf-8').strip()
        if data:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            id_data = data[:3]
            filtered_data = data[3:].strip()
            log_entry = f"{timestamp}   {filtered_data}"
            print(log_entry)

            if id_data == "000":
                filename = "data_000.txt"
            elif id_data == "001":
                filename = "data_001.txt"
            elif id_data == "002":
                filename = "data_002.txt"
            elif id_data == "003":
                filename = "data_003.txt"
            elif id_data == "004":
                filename = "data_004.txt"
            elif id_data == "005":
                filename = "data_005.txt"
            else:
                filename = "data_unknown.txt"

            with open(filename, "a", buffering=1) as file:
                file.write(log_entry + "\n")