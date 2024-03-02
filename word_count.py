"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load word files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #

    filenames = glob.glob(f"{input_directory}/*.txt")

    dataframes = [
        pd.read_csv(filename, sep="\t", header=None, names=["word"])
        for filename in filenames
    ]

    concatenated_df = pd.concat(dataframes, ignore_index=True)

    return concatenated_df


def clean_text(dataframe):
    """word cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #

    dataframe = dataframe.copy()
    dataframe["word"] = dataframe["word"].str.lower()
    dataframe["word"] = dataframe["word"].str.replace(".", "")
    dataframe["word"] = dataframe["word"].str.replace(",", "")

    return dataframe


def count_words(dataframe):
    """Word count"""

    dataframe = dataframe.copy()
    dataframe["word"] = dataframe["word"].str.split()
    dataframe = dataframe.explode("word")
    dataframe["count"] = 1

    dataframe = dataframe.groupby("word").agg({"count": "sum"})

    return dataframe


def count_words_(dataframe):
    """Word count"""

    dataframe = dataframe.copy()
    dataframe["word"] = dataframe["word"].str.split()
    dataframe = dataframe.explode("word")
    dataframe = dataframe["word"].value_counts()

    return dataframe


def save_output(dataframe, output_filename):
    """Save output to a file."""

    dataframe.to_csv(output_filename, sep="\t", index=True, header=False)


df = load_input("input")
df = clean_text(df)
df = count_words_(df)
save_output(df, "output.txt")
print(df)


# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    df = load_input(input_directory)
    df = clean_text(df)
    df = count_words_(df)
    save_output(df, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
