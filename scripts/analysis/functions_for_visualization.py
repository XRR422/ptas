import os, sys
sys.path.append(os.getcwd())
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from setting.variables_config import *


words_to_remove = set(Chatbot_accessibility_words_ls + ['YES', 'YES\n', 'YES,', 'THERE', 'THERE,', 'IS', 'IS\n', 'IS,'])
FIG_SIZE=(5.8*2.5, 3*2)
def plot_word_cloud(df_column, ax):
    # Convert the DataFrame column to a single string
    text = ' '.join(df_column.dropna().astype(str))  # Drop NA values and convert to string
    
    # Generate a word cloud image
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the generated image using the provided Axes object:
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")  # Hide axis on the specific subplot

def filter_words(text):
    return ' '.join([word for word in text.split() if word not in words_to_remove])

def plot_keyword_counts(directory, positive_list, negative_list, horizontal=False):
    # Dictionary to store keyword counts
    keyword_counts = {}

    # Loop over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # Extract the keyword from the filename using regex
            match = re.search(r'keyword-(\w+).csv', filename)
            if match:
                keyword = match.group(1)
                if keyword not in keyword_counts:
                    keyword_counts[keyword] = 0

                # Read the CSV file
                df = pd.read_csv(os.path.join(directory, filename))

                # Remove duplicate rows based on the 'Sentence' column
                df = df.drop_duplicates(subset=['Sentence'])

                # Update keyword count
                keyword_counts[keyword] += len(df)

    # Convert the dictionary to a DataFrame for plotting
    data = pd.DataFrame(list(keyword_counts.items()), columns=['Keywords', 'Count'])

    # Assign colors based on keyword classification
    data['Color'] = data['Keywords'].apply(lambda x: 'blue' if x in positive_list else 'red' if x in negative_list else 'gray')
    color_palette = dict(zip(data['Keywords'], data['Color']))  # Create a color mapping dictionary

    # Determine the plot type based on the horizontal flag
    if horizontal:
        # Create a horizontal bar plot
        plt.figure(figsize=FIG_SIZE)
        bar_plot = sns.barplot(x='Count', y='Keywords', data=data, palette=color_palette)
        plt.title('Counts of Accessibility Keywords on DRPS, 23-24 Year')
        plt.xlabel('Count')
        plt.ylabel('Keywords')
    else:
        # Create the vertical bar plot
        plt.figure(figsize=FIG_SIZE)
        bar_plot = sns.barplot(x='Keywords', y='Count', data=data, palette=color_palette)
        plt.title('Counts of Accessibility Keywords on DRPS, 23-24 Year')
        plt.xlabel('Keywords')
        plt.ylabel('Count')
        plt.xticks(rotation=90)  # Rotate labels to 90 degrees for better readability
    handles = [plt.Line2D([0], [0], color='blue', lw=4, label='Positive to accessibility'),
           plt.Line2D([0], [0], color='red', lw=4, label='Negative to accessibility'),
           plt.Line2D([0], [0], color='grey', lw=4, label='Neutral to accessibility')]

    plt.legend(handles=handles)
    
    plt.grid()
    plt.tight_layout()  # Adjust layout to make room for label rotation
    plt.show()
    return bar_plot