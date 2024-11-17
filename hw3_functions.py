import build_data
import data
from data import CountyDemographics

# Part 1: population_total
########################################################################################################################
# input : list_county demographics
# output : int (total population of input demographics) in this case, for the total 2014 population

# in this case we use thin input of full_data, which is a list of CountyDemographics objects.
# to return the total population we will:
#   - iterate through each CountyDemographics object
#   - for each object, find its population, then use the get() method for dictionaries to acess the '2014 Population'
#   - append the population for each county to a list
#   - return a sum of all county populations in the list

def population_total(demographics: list[CountyDemographics]) -> int:
    county_populations = []
    for county in range(len(demographics)):
        county_populations.append(demographics[county].population.get('2014 Population'))
    return sum(county_populations)

# Part 2:  filter_by_state
########################################################################################################################
# input: demographics: list[CountyDemographics], state_ab: str
# output: list[CountyDemographics] (reduced or filtered)

# the filter_by_state function will take the input list of county demographics, and it will filter the data to only
# return the county demographics from a specific state specified by the state abbreviation i.e CA
def filter_by_state(demographics: list[CountyDemographics], state_ab: str) -> list[CountyDemographics]:
    filtered_demographics = []
    for county in demographics:
        if county.state == state_ab.upper():
            filtered_demographics.append(county)
    return filtered_demographics

# Part 3
########################################################################################################################
# population_by_education
########################################################################################################################
# input: demographics: list[CountyDemographics],str
# output: int (Population of people with a certain degree of education)

# the population by education function will take the input list of county demographics, and it will use the percentage
# of people with a certain degree of eduction, alongside the total population to calculate the population of people in a
# given county that have said level of education

# note that the percent educated value is the percentage out of every 100 people so we must divide this number by 100
# before we multiply  it by the total population

def population_by_education(counties: list[CountyDemographics], education_level: str) -> int:
    for county in counties:
        if f'{education_level}' in county.education:
            percent_educated = county.education.get(education_level)
            return (percent_educated * 10**-2) * population_total(counties)
        else:
            return 0


# population_by_ethnicity
########################################################################################################################
# inputs: list[CountyDemographics],str
# outputs: float

# similar functionality to population_by_education

def population_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> int:
    for county in counties:
        if f'{ethnicity}' in county.ethnicities:
            ethnicity_percentage = county.ethnicities.get(ethnicity)
            return (ethnicity_percentage * 10**-2) * population_total(counties)
        else:
            return 0


# population_below_poverty
########################################################################################################################
# inputs: list[CountyDemographics]
# outputs: int
# (1) iterate through each county (2)access the percentage of people below the poverty level (3) multiply 2014 population
# by percentage below poverty level. (4) add this number to accumulator (5) Return accumulated value

def population_below_poverty_level(counties: list[CountyDemographics], demographic: str) -> float:
    pop_below = 0
    for county in counties:
        percent_below = county.income.get(f'{demographic}')/100
        pop_below += percent_below * county.population.get('2014 Population')
    return pop_below




# Part 4
########################################################################################################################

#percent_by_education
########################################################################################################################
# percent_by_education will take two parameters, a list of county demographics, and a key to determine the percentage of
# people out of the total population of the counties, the function will utilize the total population funciton and the
# population by eduction functions defined above

def percent_by_education(counties: list[CountyDemographics], education_level: str) -> float:
    total_pop = population_total(counties)
    educated_pop = population_by_education(counties, education_level)
    if total_pop > 0:
        return (educated_pop / total_pop) * 100
    else:
        return 0


# percent_by_ethnicity
#######################################################################################################################
# the percent by ethnicity function will use the total population function, and the population by ethnicity functions to
# return a percentage of the population that is a certain ethnicity.

def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity: str) -> float:
    total_pop = population_total(counties)
    ethnicity_pop = population_by_ethnicity(counties, ethnicity)
    if total_pop > 0:
        return (ethnicity_pop / total_pop) * 100
    else:
        return 0


# percent_below_poverty_level
########################################################################################################################
# the percent below poverty level function will use pre-defined functions to find the total population of the list,
# and the total population of people below the poverty level. it will then divide the two and return the result as a
# percentage

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_pop = population_total(counties)
    impoverished_pop = population_below_poverty_level(counties)
    if total_pop > 0:
        return (impoverished_pop / total_pop) * 100
    else:
        return 0


# Part 5
#######################################################################################################################

#education_greater_than
########################################################################################################################
# inputs: counties: list[CountyDemographics, key: str (education_level), threshold: float (target Percentage)
# outputs: list[CountyDemographics]

# this function will iterate through all of the county demographics objects, and return the counties whose key education
# level is greater than that of the threshold

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.education.get(key):
            if county.education.get(key) > threshold:
                filtered_counties.append(county)
    return filtered_counties

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.education.get(key):
            if county.education.get(key) < threshold:
                filtered_counties.append(county)
    return filtered_counties

# helper funciton to list the names of the counties in filtered county lists to simplify testing
# will return a list of county names
def county_list_names(counties: list[CountyDemographics]) -> list[str]:
    county_names = []
    for county in counties:
        county_names.append(county.county)
    return county_names


# ethnicity_greater_than
#######################################################################################################################
# inputs: counties: list[CountyDemographics, key: str (ethnicity), threshold: float (target Percentage)
# outputs: list[CountyDemographics]
# same funcitonality as education greater than, however now the input key should be an ethnicity

# again I will use the county_list_names for ease of testing

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.ethnicities.get(key):
            if county.ethnicities.get(key) > threshold:
                filtered_counties.append(county)
    return filtered_counties

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.ethnicities.get(key):
            if county.ethnicities.get(key) < threshold:
                filtered_counties.append(county)
    return filtered_counties


# below_poverty_level_greater_than
########################################################################################################################
# inputs: counties: list[CountyDemographics, threshold: float (target Percentage)
# outputs: list[CountyDemographics]
# similar functionality to education greater than, however now there should be no input key.

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.income.get('Persons Below Poverty Level'):
            if county.income.get('Persons Below Poverty Level') > threshold:
                filtered_counties.append(county)
    return filtered_counties

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    filtered_counties = []
    for county in counties:
        if county.income.get('Persons Below Poverty Level'):
            if county.income.get('Persons Below Poverty Level') < threshold:
                filtered_counties.append(county)
    return filtered_counties










