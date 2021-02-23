## Write a function that uses the wget module to download an image from a link.
## The URL you use should be inside a variable (another function will feed you the URL)
## This page shows you how: (https://likegeeks.com/downloading-files-using-python/#Using-wget)
## PASS/FAIL- whether or not your function downloads a pokemon PNG image to home/student/mycode/ from a link like https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png

import wget

# url = "https://www.python.org/static/img/python-logo@2x.png"
# get.download(url, 'c:/users/LikeGeeks/downloads/pythonLogo.png')


def wget_pic(imagelink):
    # code goes here!
    wget.download(imagelink, '/home/student/mycode/')
    # image must be saved to /home/student/mycode

wget_pic("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png")


