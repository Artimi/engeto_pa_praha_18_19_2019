import csv

SALARIES_PATH = 'salaries.csv'
SALARIES_SUMMARY_PATH = 'salaries_summary.csv'

with open(SALARIES_PATH) as file:
    reader = csv.reader(file)
    next(reader)
    salaries = [int(row[1]) for row in reader]

header = ['TYPE', 'SALARY']

with open(SALARIES_SUMMARY_PATH, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(['Minimum salary', min(salaries)])
    writer.writerow(['Maximum salary', max(salaries)])
    writer.writerow(['Average salary', int(sum(salaries) / len(salaries))])



