import media
import fresh_tomatoes
 

funny_people = media.Movie("Funny People", "An aspiring comedian befriends a dying comedic star.",
                        "https://upload.wikimedia.org/wikipedia/en/2/26/PosterFunnyPeople.jpg",
                        "https://www.youtube.com/watch?v=G_1jjqKFYaY")



darjeeling_limited = media.Movie("The Darjeeling Limited",
                     "Three brothers go on a spiritual quest in India.",
                     "https://upload.wikimedia.org/wikipedia/en/1/1e/Darjeeling_Limited_Poster.jpg",
                     "https://www.youtube.com/watch?v=1rFesfI9mxM")
                     


no_country_for_old_men = media.Movie("No Country for Old Men",
                                     "A man finds a case full of money, setting off a violent series of events.",
                                     "https://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                                     "https://www.youtube.com/watch?v=A0oNrgumrlE")

grizzly_man = media.Movie("Grizzly Man",
                          "A man dedicates his life to bears by living with them in Alaska.",
                          "https://upload.wikimedia.org/wikipedia/en/e/e5/Grizzly_man_ver2.jpg",
                          "https://www.youtube.com/watch?v=uWA7GtDmNFU")

inglourious_basterds = media.Movie("Inglourious Basterds",
                                   "A group of rag-tag soldiers set out to assassinate Hitler.",
                                   "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",
                                   "https://www.youtube.com/watch?v=KnrRy6kSFF0")

fargo = media.Movie("Fargo",
                    "An incompetent man has his wife kidnapped.",
                    "https://upload.wikimedia.org/wikipedia/en/a/ac/Fargo.jpg",
                    "https://www.youtube.com/watch?v=bn7LOhWYtqE")

movie_list = [fargo, funny_people, darjeeling_limited, no_country_for_old_men, grizzly_man, inglourious_basterds]

fresh_tomatoes.open_movies_page(movie_list)
