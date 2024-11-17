import sample_data
import build_data
import unittest
import hw3_functions


# These two values are defined to support testing below. The
# data within these structures should not be modified. Doing
# so will affect later tests.
#
# The data is defined here for visibility purposes in the context
# of this course.
full_data = build_data.get_data()

class TestCases(unittest.TestCase):


    # Part 1
    # test population_total
    def test_population_total(self):
        input_demographics = full_data
        expected = 318857056
        actual = hw3_functions.population_total(input_demographics)
        self.assertEqual(expected, actual)

    def test_population_total_reduced(self):
        input_demographics = sample_data.reduced_data
        expected = 655813
        actual = hw3_functions.population_total(input_demographics)
        self.assertEqual(expected, actual)

    # Part 2
    # test filter_by_state

    # to test filter by state, we are told that there are 58 counties in the full set of data that should be in CA,
    # so, to verify that the function works, we will be checking the length of
    def test_filter_by_state(self):
        input_demographics = full_data
        expected = 58
        actual = len(hw3_functions.filter_by_state(input_demographics, 'CA'))
        self.assertEqual(expected, actual)


    # we are also told in the description that the counties would have a total population of 38802500 so we will use the
    # population total function to find the total population of the counties returned by this function.
    def test_filter_by_state2_population(self):
        input_demographics = full_data
        expected = 38802500
        actual = hw3_functions.population_total(hw3_functions.filter_by_state(input_demographics, 'CA'))
        self.assertEqual(expected, actual)

    # Part 3


    # test population_by_education
    # since we wer provided that 87911.145 people in slo county have a bachelors degree or higher we will use this
    # information as a testing point.

    def test_population_by_education(self):
        input_demographics = sample_data.slo_data
        expected = 87911.145 # number based off of data, can not have .145 people
        actual = hw3_functions.population_by_education(input_demographics, 'Bachelor\'s Degree or Higher')
        self.assertEqual(expected, actual)

    # test case when the input education is not a valid level of education
    def test_population_by_education2(self):
        input_demographics = sample_data.slo_data
        expected = 0
        actual = hw3_functions.population_by_education(input_demographics, '1st Degree Burn')
        self.assertEqual(expected, actual)


    # test population_by_ethnicity using sample_data.slo_data
    # ethnicity is in ethnicities
    def test_population_by_ethnicity(self):
        input_demographics = sample_data.slo_data
        expected = 10605.154
        actual = hw3_functions.population_by_ethnicity(input_demographics, 'Asian Alone')
        self.assertEqual(expected, actual)
    # ethnicity not in ethnicities
    def test_population_by_ethnicity2(self):
        input_demographics = sample_data.slo_data
        expected = 0
        actual = hw3_functions.population_by_ethnicity(input_demographics, 'Hippo')
        self.assertEqual(expected, actual)

    # test population_below_poverty_level
    def test_population_below_poverty_level1(self):
        input_demographics = sample_data.slo_data
        expected = 39908.869
        actual = hw3_functions.population_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual)

    # test with reduced data
    def test_population_below_poverty_level(self):
        input_demographics = sample_data.reduced_data
        expected = 107711.714
        actual = hw3_functions.population_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual)


    # Part 4
    # test percent_by_education
    def test_percent_by_education(self):
        input_demographics = sample_data.slo_data
        education = "Bachelor's Degree or Higher"
        expected = 31.5
        actual = hw3_functions.percent_by_education(input_demographics,education)
        self.assertEqual(expected, actual)

    def test_percent_by_education2(self):
        input_demographics = sample_data.reduced_data
        education = "Bachelor's Degree or Higher"
        expected = 20.9
        actual = hw3_functions.percent_by_education(input_demographics,education)
        self.assertAlmostEqual(expected, actual)

    def test_percent_by_education3(self):
        input_demographics = full_data
        education = "Bachelor's Degree or Higher"
        expected = 20.9
        actual = hw3_functions.percent_by_education(input_demographics,education)
        self.assertAlmostEqual(expected, actual)



    # test percent_by_ethnicity

    def test_percent_by_ethnicity(self):
        input_demographics = sample_data.slo_data
        ethnicity = 'Asian Alone'
        expected = 3.8
        actual = hw3_functions.percent_by_ethnicity(input_demographics,ethnicity)
        self.assertEqual(expected, actual)

    def test_percent_by_ethnicity2(self):
        input_demographics = full_data
        ethnicity = 'Asian Alone'
        expected = 1.1
        actual = hw3_functions.percent_by_ethnicity(input_demographics,ethnicity)
        self.assertAlmostEqual(expected, actual)


    # test percent_below_poverty_level
    def test_percent_below_poverty_level(self):
        input_demographics = sample_data.slo_data
        expected = 14.3
        actual = hw3_functions.percent_below_poverty_level(input_demographics)
        self.assertEqual(expected, actual)

    def test_percent_below_poverty_level2(self):
        input_demographics = sample_data.reduced_data
        expected = 16.42
        actual = hw3_functions.percent_below_poverty_level(input_demographics)
        self.assertAlmostEqual(expected, actual, places=2)

    # Part 5

    # test education_greater_than
    def test_education_greater_than(self):
        counties = sample_data.slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 7
        expected = ['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_education_greater_than2(self):
        counties = sample_data.slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 50
        expected = []
        actual = hw3_functions.county_list_names(hw3_functions.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    # test education_less_than
    def test_education_less_than(self):
        counties = sample_data.slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 50
        expected = ['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.education_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    def test_education_less_than2(self):
        counties = sample_data.slo_data
        key = "Bachelor's Degree or Higher"
        threshold = 7
        expected = []
        actual = hw3_functions.county_list_names(hw3_functions.education_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test education greater than with a full set of data, since both are essentially the same function, no need to do
    # this twice

    # all reduced data counties should be in this range
    def test_education_greater_than3(self):
        counties = sample_data.reduced_data
        key = "Bachelor's Degree or Higher"
        threshold = 9
        expected = ['Autauga County','Crawford County', 'San Luis Obispo County','Yolo County','Butte County',
                    'Pettis County','Weston County']
        actual = hw3_functions.county_list_names(hw3_functions.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    # some reduced data counties will not be in this range

    def test_education_greater_than4(self):
        counties = sample_data.reduced_data
        key = "Bachelor's Degree or Higher"
        threshold = 17
        expected = ['Autauga County','San Luis Obispo County','Yolo County', 'Butte County', 'Weston County']
        actual = hw3_functions.county_list_names(hw3_functions.education_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test ethnicity_greater_than
    def test_ethnicity_greater_than(self):
        counties = sample_data.slo_data
        key = "Asian Alone"
        threshold = 2.1
        expected = ['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.ethnicity_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_ethnicity_greater_than2(self):
        counties = sample_data.slo_data
        key = "Asian Alone"
        threshold = 4
        expected = []
        actual = hw3_functions.county_list_names(hw3_functions.ethnicity_greater_than(counties, key, threshold))
        self.assertEqual(expected, actual)


    # test ethnicity_less_than
    def test_ethnicity_less_than(self):
        counties = sample_data.slo_data
        key = "Asian Alone"
        threshold = 4
        expected = ['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.ethnicity_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)

    def test_ethnicity_less_than2(self):
        counties = sample_data.slo_data
        key = 'Asian Alone'
        threshold = 1.1
        expected = []
        actual = hw3_functions.county_list_names(hw3_functions.ethnicity_less_than(counties, key, threshold))
        self.assertEqual(expected, actual)



    # test below_poverty_level_greater_than
    def test_below_poverty_level_greater_than(self):
        counties = sample_data.slo_data
        threshold = 13
        expected = ['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.below_poverty_level_greater_than(counties, threshold))
        self.assertEqual(expected, actual)

    def test_below_poverty_level_greater_than2(self):
        counties = sample_data.slo_data
        threshold = 20
        expected =[]
        actual = hw3_functions.county_list_names(hw3_functions.below_poverty_level_greater_than(counties, threshold))
        self.assertEqual(expected, actual)

    # test below_poverty_level_less_than

    def test_below_poverty_level_less_than(self):
        counties = sample_data.slo_data
        threshold = 13
        expected = []
        actual = hw3_functions.county_list_names(hw3_functions.below_poverty_level_less_than(counties, threshold))
        self.assertEqual(expected, actual)

    def test_below_poverty_level_less_than2(self):
        counties = sample_data.slo_data
        threshold = 20
        expected =['San Luis Obispo County']
        actual = hw3_functions.county_list_names(hw3_functions.below_poverty_level_less_than(counties, threshold))
        self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
