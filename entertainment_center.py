# Lesson 3.4: Make Classes# Mini-Project: Movies Website# In this file, you will define instances of the class Movie defined
# in media.py. Make some instances of your own!
# After you run this code, open the file fresh_tomatoes.html to# see your webpage!
# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

fifty_shades_of_grey = media.Movie("Fifty Shades of Grey",                        
  "When college senior Anastasia Steele (Dakota Johnson) steps in for her sick roommate to interview prominent businessman Christian Grey (Jamie Dornan) for their campus paper, little does she realize the path her life will take. Christian, as enigmatic as he is rich and powerful, finds himself strangely drawn to Ana, and she to him. Though sexually inexperienced, Ana plunges headlong into an affair -- and learns that Christian's true sexual proclivities push the boundaries of pain and pleasure.",
  "https://en.wikipedia.org/wiki/Fifty_Shades_of_Grey_(film)#/media/File:Fifty-Gray-poster.jpg",                        
  "https://www.youtube.com/watch?v=SfZWFDs0LxA")    

up = media.Movie("Up",                    
  "By tying thousands of balloons to his home, 78-year-old Carl sets out to fulfill his dream to see the wilds of South America and to complete a promise made to his late wife, Ellie.",                    
  "https://en.wikipedia.org/wiki/Up_(2009_film)#/media/File:Up_(2009_film).jpg",                    
  "https://www.youtube.com/watch?v=pkqzFUhGPJg")

gattaca = media.Movie("GATTACA",
  "A biopunk vision of a future society driven by eugenics where potential children are conceived through genetic manipulation to ensure they possess the best hereditary traits of their parents.[3] The film centers on Vincent Freeman, played by Hawke, who was conceived outside the eugenics program and struggles to overcome genetic discrimination to realize his dream of traveling into space.",
  "https://en.wikipedia.org/wiki/Gattaca#/media/File:Gataca_Movie_Poster_B.jpg",
  "https://www.youtube.com/watch?v=hWjlUj7Czlk")#print(up.storyline)

movies = [fifty_shades_of_gray, up, gattaca]
fresh_tomatoes.open_movies_page(movies)
