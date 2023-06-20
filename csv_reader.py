import csv

def read_csv(filename):
    try:
        with open(filename, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for record in csv_reader:
                print(record)

    except Exception as e:
        print(e)
    
read_csv('market_cap.csv')