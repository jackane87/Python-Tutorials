from csv import DictReader
with open('All Translations (Round 27).csv') as file:
    csv_reader = list(DictReader(file))
    for row in csv_reader:
        print(f'{Spanish} {English}')


'''from csv import reader
with open('All Translations (Round 27).csv') as file:
    csv_reader  = list(reader(file))
    print(csv_reader[-1])'''