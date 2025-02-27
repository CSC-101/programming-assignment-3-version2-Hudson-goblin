from typing import List
from data import CountyDemographics
#part 1
def population_total(counties: list[CountyDemographics]) -> int: #input is a list of stings for county attributs whilst the output is a jnteger
    return sum(county.population.get('2014 Population', 0) for county in counties)

#part 2
def filter_by_state(counties: list[CountyDemographics], state_abbr: str) -> list[CountyDemographics]:
    return [county for county in counties if county.state == state_abbr]
#takes in a list of countydemographics and the two letter state abbreviation and returns countydemographic objects that match the state
#part 3
#population_by_education
def population_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = 0.0
    for county in counties:
        if education_key in county.education and "2014 Population" in county.population:
            percent = county.education[education_key] / 100  # Convert percentage to decimal
            total_population += percent * county.population["2014 Population"]
    return total_population #takes in a list of countydemoggraphics with a string key to match with and returns an integer
 #  population_by_ethnicity
def population_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = 0.0

    for county in counties:
        if ethnicity_key in county.ethnicities:
            percentage = county.ethnicities[ethnicity_key] / 100
            total_population += percentage * county.population['2014 Population']

    return total_population
#takes in a list of countydemoggraphics with a string key to match with and returns an integer
#  population_below_poverty_level
def population_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = 0.0

    for county in counties:
        if 'Persons Below Poverty Level' in county.income:
            percentage = county.income['Persons Below Poverty Level'] / 100
            total_population += percentage * county.population['2014 Population']

    return total_population
#takes in a list of countydemoggraphics with a string key to match with and returns an integer

# part 4

# percent_by_education
def percent_by_education(counties: list[CountyDemographics], education_key: str) -> float:
    total_population = sum(county.population.get('2014 Population', 0) for county in counties)

    if total_population == 0:
        return 0.0  # Prevent division by zero

    education_population = population_by_education(counties, education_key)

    return (education_population / total_population) * 100
#  percent_by_ethnicity
def percent_by_ethnicity(counties: list[CountyDemographics], ethnicity_key: str) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0

    ethnicity_population = population_by_ethnicity(counties, ethnicity_key)
    return (ethnicity_population / total_population) * 100
#  percent_below_poverty_level
def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = population_total(counties)
    if total_population == 0:
        return 0

    poverty_population = population_below_poverty_level(counties)
    return (poverty_population / total_population) * 100

#part 5

#  education_greater_than
def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) > threshold]
#  education_less_than
def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.education.get(key, 0) < threshold]
#  ethnicity_greater_than
def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) > threshold]
#  ethnicity_less_than
def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.ethnicities.get(key, 0) < threshold]
#  below_poverty_level_greater_than
def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) > threshold]
#  below_poverty_level_less_than
def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    return [county for county in counties if county.income.get('Persons Below Poverty Level', 0) < threshold]