import data
import build_data
import unittest
from hw3 import population_total, filter_by_state, population_by_education, population_by_ethnicity, population_below_poverty_level, percent_by_education, percent_by_ethnicity, percent_below_poverty_level, education_less_than, education_greater_than, ethnicity_greater_than, ethnicity_less_than, below_poverty_level_greater_than, below_poverty_level_less_than
from data import CountyDemographics
# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

reduced_data = [
    data.CountyDemographics(
        {'Percent 65 and Older': 13.8,
         'Percent Under 18 Years': 25.2,
         'Percent Under 5 Years': 6.0},
        'Autauga County',
        {"Bachelor's Degree or Higher": 20.9,
         'High School or Higher': 85.6},
        {'American Indian and Alaska Native Alone': 0.5,
         'Asian Alone': 1.1,
         'Black Alone': 18.7,
         'Hispanic or Latino': 2.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 1.8,
         'White Alone': 77.9,
         'White Alone, not Hispanic or Latino': 75.6},
        {'Per Capita Income': 24571,
         'Persons Below Poverty Level': 12.1,
         'Median Household Income': 53682},
        {'2010 Population': 54571,
         '2014 Population': 55395,
         'Population Percent Change': 1.5,
         'Population per Square Mile': 91.8},
        'AL'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.0},
        'Crawford County',
        {"Bachelor's Degree or Higher": 14.3,
         'High School or Higher': 82.2},
        {'American Indian and Alaska Native Alone': 2.5,
         'Asian Alone': 1.6,
         'Black Alone': 1.6,
         'Hispanic or Latino': 6.7,
         'Native Hawaiian and Other Pacific Islander Alone': 0.1,
         'Two or More Races': 2.8,
         'White Alone': 91.5,
         'White Alone, not Hispanic or Latino': 85.6},
        {'Per Capita Income': 19477,
         'Persons Below Poverty Level': 20.2,
         'Median Household Income': 39479},
        {'2010 Population': 61948,
         '2014 Population': 61697,
         'Population Percent Change': -0.4,
         'Population per Square Mile': 104.4},
        'AR'),
    data.CountyDemographics(
        {'Percent 65 and Older': 17.5,
         'Percent Under 18 Years': 18.1,
         'Percent Under 5 Years': 4.8},
        'San Luis Obispo County',
        {"Bachelor's Degree or Higher": 31.5,
         'High School or Higher': 89.6},
        {'American Indian and Alaska Native Alone': 1.4,
         'Asian Alone': 3.8,
         'Black Alone': 2.2,
         'Hispanic or Latino': 22.0,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 3.4,
         'White Alone': 89.0,
         'White Alone, not Hispanic or Latino': 69.5},
        {'Per Capita Income': 29954,
         'Persons Below Poverty Level': 14.3,
         'Median Household Income': 58697},
        {'2010 Population': 269637,
         '2014 Population': 279083,
         'Population Percent Change': 3.5,
         'Population per Square Mile': 81.7},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 11.5,
         'Percent Under 18 Years': 21.7,
         'Percent Under 5 Years': 5.8},
        'Yolo County',
        {"Bachelor's Degree or Higher": 37.9,
         'High School or Higher': 84.3},
        {'American Indian and Alaska Native Alone': 1.8,
         'Asian Alone': 13.8,
         'Black Alone': 3.0,
         'Hispanic or Latino': 31.5,
         'Native Hawaiian and Other Pacific Islander Alone': 0.6,
         'Two or More Races': 5.0,
         'White Alone': 75.9,
         'White Alone, not Hispanic or Latino': 48.3},
        {'Per Capita Income': 27730,
         'Persons Below Poverty Level': 19.1,
         'Median Household Income': 55918},
        {'2010 Population': 200849,
         '2014 Population': 207590,
         'Population Percent Change': 3.4,
         'Population per Square Mile': 197.9},
        'CA'),
    data.CountyDemographics(
        {'Percent 65 and Older': 19.6,
         'Percent Under 18 Years': 25.6,
         'Percent Under 5 Years': 4.9},
        'Butte County',
        {"Bachelor's Degree or Higher": 17.9,
         'High School or Higher': 89.2},
        {'American Indian and Alaska Native Alone': 1.0,
         'Asian Alone': 0.3,
         'Black Alone': 0.2,
         'Hispanic or Latino': 5.8,
         'Native Hawaiian and Other Pacific Islander Alone': 0.2,
         'Two or More Races': 2.3,
         'White Alone': 96.1,
         'White Alone, not Hispanic or Latino': 90.6},
        {'Per Capita Income': 20995,
         'Persons Below Poverty Level': 15.7,
         'Median Household Income': 41131},
        {'2010 Population': 2891,
         '2014 Population': 2622,
         'Population Percent Change': -9.4,
         'Population per Square Mile': 1.3},
        'ID'),
    data.CountyDemographics(
        {'Percent 65 and Older': 15.3,
         'Percent Under 18 Years': 25.1,
         'Percent Under 5 Years': 6.9},
        'Pettis County',
        {"Bachelor's Degree or Higher": 15.2,
         'High School or Higher': 81.8},
        {'American Indian and Alaska Native Alone': 0.7,
         'Asian Alone': 0.7,
         'Black Alone': 3.4,
         'Hispanic or Latino': 8.3,
         'Native Hawaiian and Other Pacific Islander Alone': 0.3,
         'Two or More Races': 1.9,
         'White Alone': 92.9,
         'White Alone, not Hispanic or Latino': 85.5},
        {'Per Capita Income': 19709,
         'Persons Below Poverty Level': 18.4,
         'Median Household Income': 38580},
        {'2010 Population': 42201,
         '2014 Population': 42225,
         'Population Percent Change': 0.1,
         'Population per Square Mile': 61.9},
        'MO'),
    data.CountyDemographics(
        {'Percent 65 and Older': 18.1,
         'Percent Under 18 Years': 21.6,
         'Percent Under 5 Years': 6.5},
        'Weston County',
        {"Bachelor's Degree or Higher": 17.2,
         'High School or Higher': 90.2},
        {'American Indian and Alaska Native Alone': 1.7,
         'Asian Alone': 0.4,
         'Black Alone': 0.7,
         'Hispanic or Latino': 4.2,
         'Native Hawaiian and Other Pacific Islander Alone': 0.0,
         'Two or More Races': 2.2,
         'White Alone': 95.0,
         'White Alone, not Hispanic or Latino': 91.5},
        {'Per Capita Income': 28764,
         'Persons Below Poverty Level': 11.2,
         'Median Household Income': 55461},
        {'2010 Population': 7208,
         '2014 Population': 7201,
         'Population Percent Change': -0.1,
         'Population per Square Mile': 3.0},
        'WY')
    ]

class TestCases(unittest.TestCase):
    pass

    # Part 1
    def test_population_total_reduced(self):
        expected_population = 655813  # Sum of 2014 Population
        self.assertEqual(population_total(reduced_data), expected_population)
    def test_population_total_full(self):
        expected_population = 318857056  # Sum of 2014 Population
        self.assertEqual(population_total(build_data.get_data()), expected_population)

    # test population_total

    # Part 2
    def setUp(self):
        self.test_data = [
            CountyDemographics({}, "Autauga County", {}, {}, {}, {}, "AL"),
            CountyDemographics({}, "Crawford County", {}, {}, {}, {}, "AR"),
            CountyDemographics({}, "San Luis Obispo County", {}, {}, {}, {}, "CA"),
            CountyDemographics({}, "Yolo County", {}, {}, {}, {}, "CA"),
            CountyDemographics({}, "Butte County", {}, {}, {}, {}, "ID"),
            CountyDemographics({}, "Pettis County", {}, {}, {}, {}, "MO"),
        ]

    def test_filter_by_state(self):
        # Filtering by 'CA' should return two counties
        result = filter_by_state(self.test_data, "CA")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].county, "San Luis Obispo County")
        self.assertEqual(result[1].county, "Yolo County")
    def test_filter_by_state_full(self):
        #
        result = filter_by_state(build_data.get_data(), "CA")
        self.assertEqual(len(result), 58)

    # test filter_by_state




    # Part 3
    # test population_by_education
    def test_population_by_education_reduced(self):
        # Testing "Bachelor's Degree or Higher"
        result = population_by_education(reduced_data, "Bachelor's Degree or Higher")
        expected = 195114.091
        self.assertAlmostEqual(result, expected, places=3)
    def test_population_by_education_ex(self):
        # Testing "Bachelor's Degree or Higher"
        result = population_by_education([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'White Alone': 89.0, 'Black Alone': 2.2, 'Hispanic or Latino': 22.0},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5, 'Population per Square Mile': 81.7},
                'CA'
            )
        ], "Bachelor's Degree or Higher")
        expected = 87911.145
        self.assertAlmostEqual(result, expected, places=3)
    # test population_by_ethnicity
    def test_population_by_ethnicity_two_or_more_races(self):
        # Testing "Two or More Races"
        result = population_by_ethnicity([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'White Alone': 89.0, 'Black Alone': 2.2, 'Hispanic or Latino': 22.0, 'Two or More Races': 3.4},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5, 'Population per Square Mile': 81.7},
                'CA'
            )
        ], "Two or More Races")
        expected = (3.4 / 100) * 279083  # 3.4% of 2014 Population
        self.assertAlmostEqual(result, expected, places=3)
    def test_population_by_ethnicity_two_or_more_races2(self):
        result = population_by_ethnicity(reduced_data, "Two or More Races")
        expected = 23613.951
        self.assertAlmostEqual(result, expected, places=3)
    # test population_below_poverty_level
    def test_population_below_poverty_level_reduced(self):
        result = population_below_poverty_level([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5,
                 'Population per Square Mile': 81.7},
                'CA')
        ])
        expected_result = 39908.869
        self.assertAlmostEqual(result, expected_result, places=3)
    def test_population_below_poverty_level_reduced2(self):
        result = population_below_poverty_level(reduced_data)
        expected_result = 107711.714
        self.assertAlmostEqual(result, expected_result, places=3)




    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        result = percent_by_education([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2010 Population': 269637, '2014 Population': 279083, 'Population Percent Change': 3.5,
                 'Population per Square Mile': 81.7},
                'CA')
        ], "Bachelor's Degree or Higher")
        # Expected % calculation: (31.5% of 279083) / 279083 * 100 = 31.5
        expected_result = 31.5
        self.assertAlmostEqual(result, expected_result, places=1)
    def test_percent_by_education_reduced(self):
        result = percent_by_education(reduced_data, 'High School or Higher')
        expected_result = 86.391
        self.assertAlmostEqual(result, expected_result, places=1)
    # test percent_by_ethnicity
    def test_percent_by_ethnicity(self):
        result = percent_by_ethnicity([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ]
, 'Hispanic or Latino')
        # Expected % calculation: (22.0% of 279083) / 279083 * 100 = 22.0
        expected_result = 22.0
        self.assertAlmostEqual(result, expected_result, places=1)

    def test_percent_by_ethnicity2(self):
        result = percent_by_ethnicity(reduced_data, 'Hispanic or Latino')
        # Expected % calculation: avg percent * total pop 2014/ total pop 2014
        expected_result = 20.8
        self.assertAlmostEqual(result, expected_result, places=1)

    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        result = percent_below_poverty_level([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')])
        # Expected % calculation: (14.3% of 279083) / 279083 * 100 = 14.3
        expected_result = 14.3
        self.assertAlmostEqual(result, expected_result, places=1)
    def test_percent_below_poverty_level2(self):
        result = percent_below_poverty_level(reduced_data)
        # Expected % calculation: 16.4
        expected_result = 16.4
        self.assertAlmostEqual(result, expected_result, places=1)







    # Part 5
# test education_greater_than
    def test_education_greater_than(self):
        result = education_greater_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], "Bachelor's Degree or Higher", 30.0)
        self.assertEqual(len(result), 1)  # Since 31.5 > 30.0, the list should contain 1 county
    def test_education_greater_than2(self):
        result_empty = education_greater_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], "Bachelor's Degree or Higher", 40.0)
        self.assertEqual(len(result_empty), 0)  # 31.5 is not > 40.0, so the list should be empty

    # test education_less_than
    def test_education_less_than(self):
        result = education_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], "Bachelor's Degree or Higher", 40.0)
        self.assertEqual(len(result), 1)  # Since 31.5 < 40.0, the list should contain 1 county
    def test_education_less_than(self):
        result_empty = education_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ]
, "Bachelor's Degree or Higher", 20.0)
        self.assertEqual(len(result_empty), 0)  # 31.5 is not < 20.0, so the list should be empty

    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        result = ethnicity_greater_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 'Hispanic or Latino', 20.0)
        self.assertEqual(len(result), 1)  # 22.0 > 20.0, 1 county returned

    def test_ethnicity_greater_than2(self):
        result_empty = ethnicity_greater_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ]
, 'Hispanic or Latino', 30.0)
        self.assertEqual(len(result_empty), 0)  # 22.0 not > 30.0, so the list should be empty

# test ethnicity_less_than
    def test_ethnicity_less_than(self):
        result = ethnicity_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 'Hispanic or Latino', 30.0)
        self.assertEqual(len(result), 1)  # 22.0 < 30.0, so 1 county should be returned
    def test_ethnicity_less_than2(self):
        result_empty = ethnicity_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 'Hispanic or Latino', 15.0)
        self.assertEqual(len(result_empty), 0)  # 22.0 not < 15.0, list is empty

# test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        result = below_poverty_level_greater_than([CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 10.0)
        self.assertEqual(len(result), 1)  # 14.3 > 10.0, so 1 county should be returned

    def test_below_poverty_level_greater_than2(self):
        result_empty = below_poverty_level_greater_than([CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 20.0)
        self.assertEqual(len(result_empty), 0)  # 14.3 not > 20.0, so the list should be empty


# test below_poverty_level_less_than
    def test_below_poverty_level_less_than(self):
        result = below_poverty_level_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 20.0)
        self.assertEqual(len(result), 1)  # 14.3 < 20.0, so 1 county should be returned

    def test_below_poverty_level_less_than2(self):
        result = below_poverty_level_less_than([
            CountyDemographics(
                {'Percent 65 and Older': 17.5, 'Percent Under 18 Years': 18.1, 'Percent Under 5 Years': 4.8},
                'San Luis Obispo County',
                {"Bachelor's Degree or Higher": 31.5, 'High School or Higher': 89.6},
                {'American Indian and Alaska Native Alone': 1.4, 'Asian Alone': 3.8, 'Black Alone': 2.2,
                 'Hispanic or Latino': 22.0, 'Native Hawaiian and Other Pacific Islander Alone': 0.2,
                 'Two or More Races': 3.4, 'White Alone': 89.0, 'White Alone, not Hispanic or Latino': 69.5},
                {'Per Capita Income': 29954, 'Persons Below Poverty Level': 14.3, 'Median Household Income': 58697},
                {'2014 Population': 279083},
                'CA')
        ], 20.0)
        self.assertEqual(len(result), 1)  # 14.3 < 20.0, so 1 county should be returned


if __name__ == '__main__':
    unittest.main()
