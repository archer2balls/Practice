import csv

with open('GOOG.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        print(line['Open'])

    # with open('new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')

    #     for line in csv_reader:
    #         csv_writer.writerow(line)
