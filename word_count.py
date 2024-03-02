"""Taller evaluable"""





import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    filenames = glob.glob(f"{input_directory}/*.txt")

    dataframe = [
        pd.read_csv(filename, sep="\t", header=None, names=['text']) for filename in filenames
    ]
    concadenate = pd.concat(dataframe , ignore_index=True)
    
    return concadenate
    





def clean_text(dataframe):
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.lower()
    dataframe['text'] = dataframe['text'].str.replace(",","")
    dataframe['text'] = dataframe['text'].str.replace(".","")
    
    return dataframe





    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #

def count_words(dataframe):
    dataframe = dataframe.copy()
    dataframe['text'] = dataframe['text'].str.split()
    dataframe = dataframe.explode('text')
    count = dataframe['text'].value_counts() 
    return count

 



def save_output(dataframe, output_filename):
    dataframe = dataframe.copy()
    dataframe.to_csv(output_filename, sep= "\t", index=True, header=False)








# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    df=load_input(input_directory)
    df=clean_text(df)
    df=count_words(df)
    save_output(df,output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
