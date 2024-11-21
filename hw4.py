import sys
import build_data, hw3_functions

# Load the full dataset
full_data = build_data.get_data()

# Retrieve the operation to be performed from the command-line arguments
operation = sys.argv[1]

# Initialize the list to store relevant counties
relevant_counties = []
# Ensure relevant_counties is not empty


# Ask in class how to fix this, works for everything except for errors, becasue it displays all information
# this will cause issues in 'some errors' to see propper error handling remove the display function. at the end of the
# 'some errors' file
while len(relevant_counties) == 0:
    relevant_counties = full_data

# Methodology: I have attempted to handle all of the inputs at the beginning of the program, so any


try:
    # Open the operations file specified in the command-line arguments (this format will automatically close it when done)
    with open(operation, 'r') as open_file:

# This section handles the input file line by line
# You will noice a nested try except block, originally I attempted to use one try except block, however I ran into the
# issue that when an error was raised, the program would stop running. Using the nested try-except made it so the program
# would print the error message, but it would continue to iterate through the rest of the lines.
########################################################################################################################
        # Iterate through each line in the file
        for line in open_file:
            current_line = line.strip()

            # handles empty lines when iterating line by line through the file
            if not current_line:
                continue

            try:
                #  Extract the operation and parameters from the current line
                if ':' in current_line:
                    inputs = current_line.split(":")

                    # Because of 'some errors' when there are more than 2 ':'
                    if len(inputs) > 3:
                        raise ValueError(f'"{current_line}" not valid')

                    current_operation = inputs[0]
                    current_field = inputs[1] if len(inputs) > 1 else None
                    current_threshold = float(inputs[2]) if len(inputs) > 2 else None
                    # used to find the specified field in filter-lt/gt and population operations such operations require
                    # being split again at their ('.')
                    field = current_field.split('.')[0].lower()
                    if '.' in current_field:
                        demographic = current_field.split('.')[1]

                else:
                    current_operation = current_line
                    current_field = None
                    current_threshold = None

########################################################################################################################

                # Handle display operation
                if current_operation == "display":
                    for county in relevant_counties:
                        # Print county header and information in readable format
                        print('*' * 50 + '\t' + f'{county.county}' + '\t' + '*' * 50 + '\n')
                        print(f'State: {county.state}\n')
                        print('Age:\n')
                        for key, value in county.age.items():
                            print(f'\t{key}: {value}')
                        print('\nEducation:\n')
                        for key, value in county.education.items():
                            print(f'\t{key}: {value}')
                        print('\nEthnicity:\n')
                        for key, value in county.ethnicities.items():
                            print(f'\t{key}: {value}')
                        print('\nIncome:\n')
                        for key, value in county.income.items():
                            if 'Income' in key:
                                print(f'\t{key}: ${value}')
                            else:
                                print(f'\t{key}: {value}')
                        print('\nPopulation:\n')
                        for key, value in county.population.items():
                            print(f'\t{key}: {value}')
                        print('\n')

                # Handle filter by state
                elif current_operation == "filter-state":
                    filtered_counties = hw3_functions.filter_by_state(full_data, current_field)
                    relevant_counties = filtered_counties
                    print(f'Filter-{current_field}:{len(relevant_counties)} entries')

                # Handle greater-than filter
                elif current_operation == "filter-gt":
                    if field == "education":
                        filtered_counties = hw3_functions.education_greater_than(full_data, demographic,
                                                                                 current_threshold)
                    elif field == "ethnicities":
                        filtered_counties = hw3_functions.ethnicity_greater_than(full_data, demographic,
                                                                                 current_threshold)
                    elif field == "income":
                        filtered_counties = hw3_functions.below_poverty_level_greater_than(full_data, current_threshold)
                    else:
                        print(f'Error:"{field}" invalid for operation "filter-gt"')
                    relevant_counties = filtered_counties
                    print(f'Filter: {demographic} GT {current_threshold} : {len(relevant_counties)} entries')

                # Handle less-than filter
                elif current_operation == "filter-lt":
                    if field == "education":
                        filtered_counties = hw3_functions.education_less_than(full_data, demographic, current_threshold)
                    elif field == "ethnicities":
                        filtered_counties = hw3_functions.ethnicity_less_than(full_data, demographic, current_threshold)
                    elif field == "income":
                        filtered_counties = hw3_functions.below_poverty_level_less_than(full_data, current_threshold)
                    else:
                        print(f'Error:"{field}" invalid for operation "filter-lt"')
                    relevant_counties = filtered_counties
                    print(f'Filter: {field} LT {current_threshold} : {len(relevant_counties)} entries')

                # Handle population total calculation
                elif current_operation == "population-total":
                    total_pop = hw3_functions.population_total(relevant_counties if relevant_counties else full_data)
                    print(f'Filter: 2014 Population: {total_pop}')

                # Handle subpopulation calculation based on a field
                elif current_operation == "population":
                    if field == "education":
                        population = hw3_functions.population_by_education(full_data, demographic)
                    elif field == "ethnicities":
                        population = hw3_functions.population_by_ethnicity(full_data, demographic)
                    elif field == "income":
                        population = hw3_functions.population_below_poverty_level(full_data, demographic)
                    else:
                        print(f'Error:"{field}" invalid for operation "population"')
                    relevant_pop = population
                    print(f'2014 Population {demographic}: {relevant_pop}')

                # Handle percentage calculation based on a field
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



