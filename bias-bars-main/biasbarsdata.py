"""
File: biasbarsdata.py
------------------
Add your comments here
"""

KEY_WOMEN = "W"
KEY_MEN = "M"

FILENAME = "data/full-data.txt"

def convert_rating_to_index(rating):
    """
    Converts the specified numerical rating into a "bucket"
    index for the three groups of review buckets (low reviews,
    medium reviews, and high reviews). The rules for this
    conversion are specified in the assignment handout.

    Input:
        rating (float): The numerical rating associated with
                        a review

    Output:
        bucket_index (int): The index of the "bucket" into which
                          the review falls

    >>> convert_rating_to_index(1.0)
    0
    >>> convert_rating_to_index(1.5)
    0
    >>> convert_rating_to_index(3.0)
    1
    >>> convert_rating_to_index(3.5)
    1
    >>> convert_rating_to_index(4.0)
    2
    >>> convert_rating_to_index(5.5)
    2
    """
    if rating < 2.5:
        return 0
    elif rating <= 3.5:
        return 1
    else:
        return 2


def add_data_for_word(word_data, word, gender, rating):
    """
    Updates the word_data dictionary to log an occurence of the
    specified word in a review with the given rating about a professor
    of the specified gender.

    Input:
        word_data (dictionary): dict holding word frequency data
        word (string): the word for which frequency data is being updated
        gender (string): the gender label for the specified comment in which
                         this word was seen
        rating (float): the numerical rating of the review in which this word
                         was seen

    >>> word_data = {}
    >>> add_data_for_word(word_data, "good", "M", 5.0)
    >>> word_data
    {'good': {'W': [0, 0, 0], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "good", "W", 4.5)
    >>> word_data
    {'good': {'W': [0, 0, 1], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "good", "W", 3.0)
    >>> word_data
    {'good': {'W': [0, 1, 1], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "bad", "M", 1.5)
    >>> word_data
    {'good': {'W': [0, 1, 1], 'M': [0, 0, 1]}, 'bad': {'W': [0, 0, 0], 'M': [1, 0, 0]}}
    """

    if word not in word_data:
        word_data[word] = {"W": [0, 0, 0], "M": [0, 0, 0]}
    bucket_index = convert_rating_to_index(rating)
    word_data[word][gender][bucket_index] += 1


def read_file(filename):
    """
    Reads the information from the specified file and builds a new
    word_data dictionary with the data found in the file. Returns the
    newly created dictionary.

    Input:
        filename (str): name of the file holding professor review data

    >>> read_file('data/small-one.txt')
    {'okay': {'W': [0, 0, 0], 'M': [0, 1, 0]}, 'best': {'W': [0, 0, 1], 'M': [0, 0, 0]}}
    >>> read_file('data/small-two.txt')
    {'awesome': {'W': [0, 0, 2], 'M': [0, 0, 1]}, 'teacher': {'W': [0, 0, 1], 'M': [0, 0, 1]}, 'class': {'W': [0, 0, 1], 'M': [0, 0, 0]}}
    >>> read_file('data/small-three.txt')
    {'average': {'W': [0, 0, 0], 'M': [1, 3, 0]}, 'best': {'W': [0, 0, 3], 'M': [1, 0, 0]}, 'not': {'W': [0, 0, 0], 'M': [2, 0, 0]}}
    """
    word_data = {}
    file = open(filename, 'r')
    next(file) #skips the header
    for line in file:
        parts = line.strip().split(',', 2)
        if len(parts) == 3:
            rating_str, gender, comment = parts
            rating = float(rating_str)
            words = comment.split()
        for word in words:
            add_data_for_word(word_data, word, gender, rating)
    file.close
    return word_data



def search_words(word_data, target):
    """
    Given a word_data dictionary that stores word frequency information and a target string,
    returns a list of all words in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        word_data (dictionary): a dictionary containing word frequency data
        target (str): a string to look for in the names contained within word_data

    Returns:
        matching_words (List[str]): a list of all words from word_data that contain
                                    the target string
    """
    # lowercase the target so we search case-insensitively
    target = target.lower()
    # make our list of words
    matching_words = []

    for word in word_data:
        # if the target is in our current word, add it to the list
        if target in word:
            matching_words.append(word)

    return matching_words



def search_words(word_data, target):
    """
    Given a word_data dictionary that stores word frequency information and a target string,
    returns a list of all words in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        word_data (dictionary): a dictionary containing word frequency data
        target (str): a string to look for in the names contained within word_data

    Returns:
        matching_words (List[str]): a list of all words from word_data that contain
                                    the target string
    """
    # lowercase the target so we search case-insensitively
    target = target.lower()
    # make our list of words
    matching_words = []

    for word in word_data:
        # if the target is in our current word, add it to the list
        if target in word:
            matching_words.append(word)

    return matching_words



def main():
    # (This function is provided for you)
    import sys
    args = sys.argv[1:]

    if len(args) == 0:
        return
    # Two command line forms
    # 1. data_file
    # 2. -search target data_file

    # Assume no search, so filename to read
    # is the first argument
    filename = args[0]

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filename = args[2]  # Update filename to skip first 2 args

    # Read in the data from the file name
    word_data = read_file(filename)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_words(word_data, target)
        for word in search_results:
            print(word)
    else:
        print_words(word_data)


if __name__ == '__main__':
    main()
