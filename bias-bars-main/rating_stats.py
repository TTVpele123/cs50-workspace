"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data.
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    # Open the file and read all lines
    with open(filename, 'r') as file:
        # Skip the header
        header = file.readline()


        # Initialize counters
        total_reviews = 0
        high_ratings = 0


        # Loop through each line in the file
        for line in file:
            total_reviews += 1
            rating = float(line.strip).split(",")[-1]
            if rating >=4.0:
                high_rating +=1


    high_rating_percentage = (high_ratings / total_reviews) * 100

    print(f"Total reviews: {total_reviews}") # Total number of reviews in the file
    print(f"High rating (>=4.0): {high ratings}") # Number of reviews with ratings >= 4.0
    print(f"High rating percentage: {high_rating_percentage:.2f}%")  # Percentage formatted to 2 decimals



def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
