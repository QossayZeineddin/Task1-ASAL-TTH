# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    return

def read_from_file(name):
    try:
        with open(name , "r") as file:
            contents = file.read()
            if len(contents) == 0:
                print("file is empty!!")
                return False
            #print(contents)
            return contents

    except FileNotFoundError:
        print("file not found")
        return False


def individual_words(text):
    #import nltk
    #nltk.download('punkt')
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    print(f"The data is: {tokens}")
    return tokens


def overall_sentiment_score(tokens):
    from textblob import TextBlob
    tb_sentiments = [TextBlob(word).sentiment.polarity for word in tokens]
    print(f"the sentiments is: {tb_sentiments}")
    avg = sum(tb_sentiments) / len(tb_sentiments)
    return  round(avg , 4)
    #print(f"The avarge of sentiments in the list is : {avg} ")


if __name__ == '__main__':


    name = input("Plz enter the name of the file! : ")
    if len(name) == 0:
        print("plz enter a the name ")
        name = input("Plz enter the name of the file! : ")

    data_from_file = read_from_file(name)
    if data_from_file == False:
        print("py")
        exec
    else:
        # print(data_from_file)
        tokens = individual_words(data_from_file)
        print("***************************************************************************")
        avarge = overall_sentiment_score(tokens)
        print(f"\nThe sentiment score of the text is {avarge}")
        if avarge > 0 :
            print(" which means that the text is positive")
        elif avarge < 0 :
            print(" which means that the text is negative ")
        else:
            print(" which means that the text is normal")
        print("\n^_^ salam")
