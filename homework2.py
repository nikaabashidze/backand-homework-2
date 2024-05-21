
#  HOMEWORK 1



best_movies = {
    "The Shawshank Redemption": 1994,
    "The Godfather": 1972,
    "The Godfather: Part II": 1974,
    "The Dark Knight": 2008,
    "12 Angry Men": 1957,
    "Schindler's List": 1993,
    "The Lord of the Rings: The Return of the King": 2003,
    "Pulp Fiction": 1994,
    "The Good, the Bad and the Ugly": 1966,
    "Fight Club": 1999,
    "Forrest Gump": 1994,
    "Inception": 2010,
    "The Lord of the Rings: The Fellowship of the Ring": 2001,
    "Star Wars: Episode V - The Empire Strikes Back": 1980,
    "The Matrix": 1999,
    "Goodfellas": 1990,
    "One Flew Over the Cuckoo's Nest": 1975,
    "Seven Samurai": 1954,
    "City of God": 2002,
    "Se7en": 1995
}



def find_min_value(data):
    numeric_values = [value for value in data.values() ]
    
    return min(numeric_values) 




min_value = find_min_value(best_movies)
print ( "The minimal date is" ,  min_value)  



# ////////////////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////////////////



# HOMEWORK 2 


def factorial(n):
    
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print (factorial(6))





