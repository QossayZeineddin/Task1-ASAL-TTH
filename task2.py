

def read_from_file(name):
    import pandas as pd
    try:
        df = pd.read_csv(name)

        # Check if dataframe is empty
        if df.empty:
            print("File is empty")
            return False
        else:
            #print(df.head())
            return df

    except FileNotFoundError:
        print("File not found")
        return False


def filtering_by_partition(df , x1 , x2):
    df = df[(df['partition'] >= int(x1)) & (df['partition'] <= int(x2)) ]
    #df.to_csv('shit.csv')
    return df

def filtering_by_gender(df , gender):
    if gender.lower() != 'male' and gender.lower() != 'female' :
        return False
    else:
        df = df[ df['gender'].str.lower() == gender.lower() ]
        return df

def search_by_name(df , name):
    df = df[ df['name'].str.contains(name)]
    df.to_csv('shit.csv')
    return df

if __name__ == '__main__':

    name = input("Plz enter the name of the file! : ")
    while len(name) == 0:
        print("plz enter a the name ")
        name = input("Plz enter the name of the file! : ")

    df = read_from_file(name)
    if df == False:
        print("py")
        exit(0)

    else:
        print("filter by partition")
        x1 = input("plz enter the fisrt number to filter (enter 'q' to quit)")
        if x1 != 'q' :
            x2 = input("plz enter the secand number to filter (enter 'q' to quit)")
        if x1 != 'q' and x2 != 'q':
            df = filtering_by_partition(df , x1 , x2)

        gender = input("plz enter the gender to filter (enter 'q' to quit) ")
        if gender != 'q' :
            if gender.lower() != 'male' and gender.lower() != 'female':
                print("invald gender")
            else:
                df = filtering_by_gender(df , gender)

        userName = input("Search by part name , plz enter name  (enter 'q' to quit)")
        if userName != 'q' :
            df = search_by_name( df , userName)

        print("result is: ")
        print(df.head(50))
        df.to_csv('test.csv')


