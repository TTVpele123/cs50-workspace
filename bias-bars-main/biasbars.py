"""
File: biasbars.py
---------------------
Add your comments here
"""

import tkinter
import biasbarsdata
import biasbarsgui as gui


# Provided constants to load and plot the word frequency data
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FILENAME = "data/full-data.txt"

VERTICAL_MARGIN = 30
LEFT_MARGIN = 60
RIGHT_MARGIN = 30
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
LABEL_OFFSET = 10
BAR_WIDTH = 75
LINE_WIDTH = 2
TEXT_DX = 2
NUM_VERTICAL_DIVISIONS = 7
TICK_WIDTH = 15


def get_centered_x_coordinate(width, idx):
    """
    Given the width of the canvas and the index of the current review
    quality bucket to plot, returns the x coordinate of the centered
    location for the bars and label to be plotted relative to.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current label in the LABELS list
    Returns:
        x_coordinate (float): The centered x coordinate of the horizontal line
                              associated with the specified label.
    >>> round(get_centered_x_coordinate(1000, 0), 1)
    211.7
    >>> round(get_centered_x_coordinate(1000, 1), 1)
    515.0
    >>> round(get_centered_x_coordinate(1000, 2), 1)
    818.3
    """


    plotting_width = width - LEFT_MARGIN - RIGHT_MARGIN
    num_buckets = len(LABELS)
    spacing = plotting_width / num_buckets
    x_coordinate = LEFT_MARGIN + (idx + 0.5) * spacing
    return x_coordinate



def draw_fixed_content(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background border and x-axis labels on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing content from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    # add your code here
    #draw the plotting rectngle:
    canvas.create_rectangle(
        LEFT_MARGIN, VERTICAL_MARGIN,
        width - RIGHT_MARGIN, height - VERTICAL_MARGIN,
        width=LINE_WIDTH
    )

    #draw lables
    for idx, label in enumerate(LABELS):
        #loop through each label in LABELS to calculate and draw its centered position below the plot area
        x = get_centered_x_coordinate(width, idx)
        y = height - VERTICAL_MARGIN + LABEL_OFFSET
        canvas.create_text(x, y, text=label, anchor=tkinter.N)


def plot_word(canvas, word_data, word):
    """
    Given a dictionary of word frequency data and a single word, plots
    the distribution of the frequency of this word across gender and
    rating category.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        word_data (dictionary): Dictionary holding word frequency data
        word (str): The word whose frequency distribution you want to plot
    """

    draw_fixed_content(canvas,) #clears and redraes the contect
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    gender_data = word_data[word]
    max_frequency = max(max(gender_data["W"]), max(gender_data["M"]))

#drawing the y axis labkes and tijcs
    for i in range (NUM_VERTICAL_DIVISIONS + 1):
        y = VERTICAL_MARGIN + i * (height - 2 * VERTICAL_MARGIN) / NUM_VERTICAL_DIVISIONS #calculates the vertical positisn / y-coordinat of the current tick mark
        freq_label = round(max_frequency * (NUM_VERTICAL_DIVISIONS - i) / NUM_VERTICAL_DIVISIONS) #determise the frequency value corresponding to the current tic the higher the frequency the highter tick
        canvas.create_line(LEFT_MARGIN - TICK_WIDTH / 2, y, LEFT_MARGIN + TICK_WIDTH / 2, y) # start and end point fo the tick
        print(f"Label: {freq_label} at position ({LEFT_MARGIN - LABEL_OFFSET}, {y})")#display the frequency value as tect nd align the texts right center corner edge to the specified lo
#plot bars
    for idx in range(len(LABELS)):
        x = get_centered_x_coordinate(width, idx)
        bar_height_men = (gender_data["M"][idx] / max_frequency) * (height - 2 * VERTICAL_MARGIN)
        bar_height_women = (gender_data["W"][idx] / max_frequency) * (height - 2 * VERTICAL_MARGIN)

        #bar for womern
        canvas.create_rectangle(
            x - BAR_WIDTH / 2, height - VERTICAL_MARGIN - bar_height_men,
            x, height - VERTICAL_MARGIN,
            fill="dodgerblue"
        )
        canvas.create_text(
            x - BAR_WIDTH / 2 + TEXT_DX, height - VERTICAL_MARGIN - bar_height_women,
            text = "W"
        )
        #Men BAr
        canvas.create_rectangle(
            x - height - VERTICAL_MARGIN - bar_height_men,
            x, + BAR_WIDTH / 2, height - VERTICAL_MARGIN,
            fill="orange"
        )
        canvas.create_text(
            x + TEXT_DX, height - VERTICAL_MARGIN - bar_height_men,
            text = "M"
        )



    # Note: You find it helpful to use the KEY_WOMEN and KEY_MEN constants
    # defined in the biasbarsdata file. To see how to use these constants,
    # reference the example above.


def convert_counts_to_frequencies(word_data):
    """
    This code is provided to you!

    It converts a dictionary
    of word counts into a dictionary of word frequencies by
    dividing each count for a given gender by the total number
    of words found in reviews about professors of that gender.
    """
    K = 1000000
    total_words_men = sum([sum(counts[biasbarsdata.KEY_MEN]) for word, counts in word_data.items()])
    total_words_women = sum([sum(counts[biasbarsdata.KEY_WOMEN]) for word, counts in word_data.items()])
    for word in word_data:
        gender_data = word_data[word]
        for i in range(3):
            gender_data[biasbarsdata.KEY_MEN][i] *= K / total_words_men
            gender_data[biasbarsdata.KEY_WOMEN][i] *= K / total_words_women


# main() code is provided for you
def main():
    # (This function is provided for you)
    import sys
    FILENAME = "data/full-data.txt"
    from biasbarsdata import read_file, print_words  # Import functions from biasbarsdata
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
        for word, data in word_data.items():
            print(f"{word}: {data}")


if __name__ == '__main__':
    main()
