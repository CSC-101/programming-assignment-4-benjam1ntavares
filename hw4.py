import sys
from logging import exception, error
from webbrowser import Error

import build_data, hw3_functions
import data
from hw3_functions import population_by_education, percent_by_education

# define the full dataset
full_data = build_data.get_data()

# retrieve a command line argument passed to python
# sys.argv[0] : name of script
# sys.argv[1] : first command-line argument passed to the script
operation = sys.argv[1]


# list used to store all counties returned by preforming the specific operations specified in the .ops file currently
# being processed
relevant_counties = []
# open the file in read format (automatically closing)
try:
    with open(operation, 'r') as open_file:

        # Iterate through the lines in the file that has been opened
        # separate the line into distinct parts,
        # perform the operation based off of specified inputs

        for line in open_file:
            current_line = line.strip()
            if not current_line:
                continue

            try:
                # Divide the input lines into more digestible pieces
                if ':' in current_line:
                    inputs = current_line.split(":")
                    if len(inputs) > 3:
                        raise ValueError(f'"{current_line}" not valid')

                    current_operation = inputs[0]
                    current_field = inputs[1] if len(inputs) > 1 else None
                    current_threshold = float(inputs[2]) if len(inputs) > 2 else  None
                    # Used in filter funcitons


                    field = current_field.split('.')[0].lower()

                    if '.' in current_field:
                        demographic = current_field.split('.')[1]


                else:
                    current_operation = current_line
                    current_field = None
                    current_threshold = None


                if current_operation == "display":
                    for county in relevant_counties:
                        # Header
                        print('*' * 50 + '\t' + f'{county.county}' + '\t' + '*' * 50 + '\n')

                        # Information
                        print('Age:')
                        for key, value in county.age.items():
                            print(f'\t{key}: {value}')
                        print()

                        print('Education:')
                        for key, value in county.education.items():
                            print(f'\t{key}: {value}')
                        print()

                        print('Ethnicity:')
                        for key, value in county.ethnicities.items():
                            print(f'\t{key}: {value}')
                        print()

                        print('Income:')
                        for key, value in county.income.items():
                            if 'Income' in key:
                                print(f'\t{key}: ${value}')
                            else:
                                print(f'\t{key}: {value}')
                        print()

                        print('Population:')
                        for key, value in county.population.items():
                            print(f'\t{key}: {value}')
                        print('\n' )



                # use the filter_by_state function defined in hw3_functions to filter the data
                elif current_operation == "filter-state":
                    filtered_counties = hw3_functions.filter_by_state(full_data,current_field)
                    relevant_counties = filtered_counties
                    print(f'Filter-{current_field}:{len(relevant_counties)} entries')

                # for -gt and -lt operations, the current field will have to be split agian so we can perform operations
                # using different parts.
                elif current_operation == "filter-gt":
                    if field == "education":
                        filtered_counties = hw3_functions.education_greater_than(full_data,demographic,current_threshold)
                    elif field == "ethnicities":
                        filtered_counties = hw3_functions.ethnicity_greater_than(full_data,demographic,current_threshold)
                    elif field == "income":
                        filtered_counties = hw3_functions.below_poverty_level_greater_than(full_data, current_threshold)
                    else:
                        print(f'Error:"{field}" invalid for operation "filter-gt"')

                    relevant_counties = filtered_counties
                    print(f'Filter: {field} GT {current_threshold} : {len(relevant_counties)} entries')



                elif current_operation == "filter-lt":
                    if field == "education":
                        filtered_counties = hw3_functions.education_less_than(full_data,demographic,current_threshold)
                    elif field == "ethnicities":
                        filtered_counties = hw3_functions.ethnicity_less_than(full_data,demographic,current_threshold)
                    elif field == "income":
                        filtered_counties = hw3_functions.below_poverty_level_less_than(full_data, current_threshold)
                    else:
                        print(f'Error:"{field}" invalid for operation "filter-lt"')

                    relevant_counties = filtered_counties
                    print(f'Filter: {field} LT {current_threshold} : {len(relevant_counties)} entries')


                elif current_operation == "population-total":
                    if len(relevant_counties) > 0:
                        total_pop = hw3_functions.population_total(relevant_counties)
                    else:
                        total_pop = hw3_functions.population_total(full_data)
                    print(f'Filter: 2014 Population: {total_pop}')


                # will return a subpopulation based off of a field passed to the operation
                elif current_operation == "population":
                    if field == "education":
                        population = population_by_education(full_data,demographic)
                    elif field == "ethnicities":
                        population = hw3_functions.population_by_ethnicity(full_data,demographic)
                    elif field == "income":
                        population = hw3_functions.population_below_poverty_level(full_data,demographic)
                    else:
                        print(f'Error:"{field}" invalid for operation "population"')

                    relevant_pop = population
                    print(f'2014 Population {demographic}: {relevant_pop}')

                elif current_operation == "percent":
                    if field == "education":
                        population = hw3_functions.percent_by_education(relevant_counties, demographic)
                    elif field == "ethnicities":
                        population = hw3_functions.percent_by_ethnicity(relevant_counties, demographic)
                    elif field == "income":
                        population = hw3_functions.percent_below_poverty_level(relevant_counties, demographic)
                    else:
                        print(f'Error:"{field}" invalid for operation "population"')

                    relevant_pop = population
                    print(f'2014 Percent {demographic}: {relevant_pop}')

                else:
                    print(f'error: "{current_operation}" is not a valid operation')

            except Exception as e:
                print(f'error: {e}')


except FileNotFoundError as fnf:
    print(f'error: {fnf}')










