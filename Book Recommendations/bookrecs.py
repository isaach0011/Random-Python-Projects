"""
Bookrecs.py
Created by: Isaac Hill
Created on: 01/22/2021
Last updated on: 03/15/2021

This program will grab data from ratings.txt and create a dictionary with names and ratings. It also grabs data from booklist.txt and creates
a list of tuples with the author and title. It will ask the user to give them a reader name. If the reader name isn't on the reader_ratings dictionary
it will exit. If it is, it then will run the function recommend which will return a list of books that their friends or the person who has the highest
affinity score has rated high. It will print these book to show the recommended books that the reader should read and hasn't read.

Function available:
    friends(reader)
    dotprod(reader, other)
    recommend(reader)

I declare that the following source code was written solely by me. I understand that copying any source code, in whole or in part,
constitutes cheating, and that I will receive a zero on this project if I am found in violation of this policy. 
I also understand future CS classes and jobs will be more difficult as a result of not doing my own work.
"""

from operator import itemgetter
from heapq import nlargest

reader_ratings = {}
book_data = []

#Grabs data from ratings.txt
with open('ratings.txt') as ratingsFile:
    ratingContent = ratingsFile.readlines()
    #First line is key, set key to 1
    key = 1

    #For each line if it is a key create a key in the dictionary that is that line in lower case.
    for line in range(len(ratingContent)):
        #If it is a key create an item in the dictionary whose key is the line in lower case.
        if key == 1:
            reader_ratings[ratingContent[line].strip().lower()] = ''
            key = 0
        #If it is not a key set the value of the last key made to the line.
        else:
            reader_ratings[ratingContent[line - 1].strip().lower()] = ratingContent[line].strip()
            key = 1 

#Grabs data from booklist.txt
with open('booklist.txt') as bookFile:
    booklistContent = bookFile.readlines()

    #For each line create a tuple with author and title and add it to a list.
    for line in booklistContent:
        author_title = tuple(line.strip().split(','))
        book_data.append(author_title)        

def friends(reader):
    """
    This function start with created a list of the keys from reader_ratings. Those will then have each name from reader_rating_keys
    run dotprod function with reader. If the name and the reader are the same it won't run dotprod. Then it finds the two people
    with the highest affinity score compared with reader to a list and returns it.

    Parameters:
    reader (str): Person who will have their two highest affinity friends returned.

    Returns:
    friends (list): List of two people with the highest affinity score with reader
    """
    reader = reader.lower()
    friends_list = []
    scores = {}

    #For each person in reader_rating_keys run dotprod with them and the reader.
    for person in reader_ratings.keys():
        #If the person is the reader it wont run dotprod. (Can't compare yourself to yourself!)
        if person != reader:
            scores[person] = dotprod(reader, person)

    #Add the two people with the highest affinity score to a list and sorts it alphabetically
    friends_list = [i[0] for i in nlargest(2,scores.items(),key=itemgetter(1))]
    friends_list.sort()

    return friends_list

def dotprod(reader, other):
    """
    This function takes parameter reader and other, and grabs their ratings from reader_ratings. Then it will split it and 
    make the values integers. Then it will pair the items in each index with the corrosponding item and idex and make those a tuple
    Then multiply each item in the tuple and add them to affinity to get the affinity score.

    Parameters:
    reader (str): Person who will be compared to other for affinity score.
    other (str): Person who will be compared to reader for affinity score

    Returns:
    affinity (int): Affinity score for reader and other
    """
    reader = reader.lower()
    other = other.lower()
    affinity = 0

    #Create a list, paired_scores, of tuples that are paired with the first item in each list of ratings, then the second item in each list of ratings, and so on...
    paired_scores = list(zip([int(i) for i in reader_ratings[reader].split()], [int(i) for i in reader_ratings[other].split()]))

    #For each tuple in the list paired_scores, multiply the first item by the second item, then add them to affinity to get score.
    for pair in paired_scores:
        affinity += pair[0] * pair[1]

    return affinity

def recommend(reader):
    """
    This function takes parameter reader and runs friends with it to see who their top friends are. It then grabs the reader and their
    two friends ratings for books and puts them into lists. Then it will compare the readers ratings to their friends ratings and if
    the reader has a 0 (has not read it) and their friends have rated it 3 and higher it will then add the index of that rating 
    and add it to recommended_book_indexes. Then grab the books that have the index of the rating and add it to recommeneded_books.
    Finally takes recommended_books and the tuples inside and makes another list recommneded_books_three_items which has tuples separted
    and sorts it by last name, first name, and book title then returns it.

    Parameters:
    reader (str): The person who is going to have their recommended books returned

    Returns:
    recommended_book_three_items (list): Recommended books for reader which has three item tuples sorted by last name, first name, and book title.
    """
    reader = reader.lower()
    recommended_book_indexes = []
    recommended_books = []

    #Runs friends to see who the reader's top friends are.
    top_friends = friends(reader)

    #Grab friends and reader ratings from reader_ratings and split the values up and convert them into integers.
    friend1_ratings = [int(i) for i in reader_ratings[top_friends[0]].split()]
    friend2_ratings = [int(i) for i in reader_ratings[top_friends[1]].split()]
    reader_book_ratings = [int(i) for i in reader_ratings[reader].split()]

    #Compare the reader ratings to their friends ratings if friend has rated a book higher than 3 and the reader has a 0 rating add it to a list.
    for rating_index in range(len(reader_book_ratings)):
        if reader_book_ratings[rating_index] == 0:
            if friend1_ratings[rating_index] > 2 or friend2_ratings[rating_index] > 2:
                recommended_book_indexes.append(rating_index)

    #Add book tuple from book_data to recommended_books based on the indexs in the index list.
    for index in recommended_book_indexes:
        recommended_books.append(book_data[index])

    #Create a new list of tuples called recommended_books_three_items that has the author last and first name and title separated so that it can be sorted
    recommended_books_three_items = []
    for item in recommended_books:
        first_last = item[0].rsplit(" ", 1)
        first_last.append(item[1])
        #If after split there is still two items in list add empty string at index 0
        if len(first_last) == 2:
            first_last.insert(0,'')
        recommended_books_three_items.append(tuple(first_last))

    #Sort recommended books by last name, first name, then book title.
    sorted(recommended_books_three_items, key=itemgetter(1,0,2))

    return recommended_books_three_items

def main():
    #Get reader name
    reader_name = input("Enter a reader's name: ")

    try:
        print(f"Recommendations for {reader_name} from {friends(reader_name)[0]} and {friends(reader_name)[1]}:")
        for book in recommend(reader_name):
            print(f"\t{book[0]} {book[1]}, {book[2]}")
    #If the reader_name isn't in the reader_ratings and gives a KeyError, print message.
    except KeyError:
        print(f"No such reader {reader_name}")

if __name__ == "__main__":
    main()