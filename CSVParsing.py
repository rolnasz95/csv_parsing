import csv


def main():

    # Open file
    with open('covid19cases_test.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')

        # Skip header line
        header = next(reader)

        highest_case_cc = 0.0
        highest_case_state = 0.0
        counter = 0
        highest_date_cc = ''
        highest_date_state = ''
        highest_county_state = ''

        for row in reader:
            positive_test = row[10]
            county = row[1]

            # Skip row if positive_test is an empty string
            if positive_test == '':
                continue
            # Convert positive_test field to float
            positive_test = float(positive_test)
            # Skip row if positive_test is a negative value
            if positive_test < 0:
                continue
            # Update highest case and date variables for CC county
            if positive_test > highest_case_cc and county == 'Contra Costa':
                highest_case_cc = positive_test
                highest_date_cc = row[0]
            # Add one to the counter variable each iteration to calculate average
            if county == 'Contra Costa':
                counter += 1
            # Get highest case count, county and date over all counties
            # Exclude data specific to California State
            if positive_test > highest_case_state and county != 'California':
                highest_case_state = positive_test
                highest_date_state = row[0]
                highest_county_state = county

        # Calculate average case counts over the period of counted days for Contra Costa county
        average = 100 * (highest_case_cc / counter)

        # Print out final results
        print("Highest new case count for Contra Costa County: " + str(int(highest_case_cc)) + " on " + highest_date_cc)
        print("Average daily new case count for Contra Costa County: " + str(round(average, 2)))
        print("The highest day for new cases was in " + highest_county_state + " with a count of "
              + str(int(highest_case_state)) + " on " + highest_date_state)


main()
