import csv

def csv_writer(filename, header, data):
    try:
        with open(filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)
            csv_writer.writerows(data)
    except Exception as e:
        print(e)

csv_writer('test.csv', ['name','age','gender'], [['Richard', 32, 'M'], ['Peter', 21, 'M'], ['Mary', 25, 'F']])
