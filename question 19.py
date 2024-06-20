def remove_punctuation(input_string):
    # Create a translation table to remove punctuation
    translator = str.maketrans("", "", string.punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string
