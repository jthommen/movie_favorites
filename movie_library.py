import favorites
import movie


fightclub = movie.Movie("Fight Club",
                        "An insomniac office worker, looking for a way to change his life, "
                        "crosses paths with a devil-may-care soap maker, "
                        "forming an underground fight club that evolves into something much, much more.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNGM2NjQxZTAtMmU5My00YTk5LWFmOWMtYjZlYzk4YzMwNjFlXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=SUXWAEX2jlg")

gladiator = movie.Movie("Gladiator",
                        "When a Roman general is betrayed and his family murdered by an emperor's corrupt son, "
                        "he comes to Rome as a gladiator to seek revenge.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=uwTKRz-WmHU")

limitless = movie.Movie("Limitless",
                        "With the help of a mysterious pill that enables the user to access 100 percent of his brain abilities, "
                        "a struggling writer becomes a financial wizard, "
                        "but it also puts him in a new world with lots of dangers.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYmViZGM0MGItZTdiYi00ZDU4LWIxNDYtNTc1NWQ5Njc2N2YwXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_SY1000_CR0,0,692,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=jOLqNOfzus4")

threehundred = movie.Movie("300",
                           "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAzNTkzNjcxNl5BMl5BanBnXkFtZTYwNDA4NjE3._V1_.jpg",
                           "https://www.youtube.com/watch?v=UrIbxk7idYA")

thematrix = movie.Movie("The Matrix",
                        "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMDMyMmQ5YzgtYWMxOC00OTU0LWIwZjEtZWUwYTY5MjVkZjhhXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,723,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=Q8g9zL-JL8E")

inception = movie.Movie("Inception",
                        "A thief, who steals corporate secrets through use of dream-sharing technology, "
                        "is given the inverse task of planting an idea into the mind of a CEO.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

# creates an array with the instance names of the class Movie
movies = [fightclub, gladiator, limitless, threehundred, thematrix, inception]

# passes the array with the instance names to the function open_movies_page within the imported favorites library
favorites.open_movies_page(movies)
