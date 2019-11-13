# before we know json module we rather store the dict in the program
employees = {
    'X12345': {
        'ID': 'X12345',
        'full_name': 'Jack Frank',
        'birthdate': '1.1.1970',
        'job_title': 'welder',
        'position_from': '1.5.2015',
        'contract_start': '1.2.2013',
        'contract_end': '31.12.2020',
        'salary': 123456
    },
    'X54321': {
        'ID': 'X54321',
        'full_name': 'Bob Doe',
        'birthdate': '8.8.1971',
        'job_title': 'machinist',
        'position_from': '1.8.2016',
        'contract_start': '1.8.2014',
        'contract_end': '31.12.2021',
        'salary': 23451
    }
}

SALARY_CHANGE_PATH = 'salary_change.txt'
JOB_CHANGE_PATH = 'job_change.txt'
CONTRACT_PROLONGATION_PATH = 'contract_prolongation.txt'

TEMPLATE_PATHS = [SALARY_CHANGE_PATH, JOB_CHANGE_PATH, CONTRACT_PROLONGATION_PATH]

print('Please select the option number of action you want to perform:')
print('0. salary change')
print('1. job change')
print('2. contract_prolongation')
selection = input('')

if selection not in ('0', '1', '2'):
    print('Unknown template number:', selection)
    exit()

template_path = TEMPLATE_PATHS[int(selection)]
with open(template_path) as file:
    template = file.read()

for employee_id, record in employees.items():
    print(f'Creating contract for {employee_id} ...')
    filled_template = template.format(**record)
    with open(f'{employee_id}_{template_path}', 'w') as file:
        file.write(filled_template)
print('Contract have been generated')
