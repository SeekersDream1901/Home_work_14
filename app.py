
#                              ██████╗░░█████╗░██████╗░░█████╗░██╗░░██╗ 🄱🅈 🄿🅁🄾🄹🄴🄲🅃
#                              ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░░██║
#                              ██████╦╝██║░░██║██████╔╝██║░░██║███████║
#                              ██╔══██╗██║░░██║██╔═══╝░██║░░██║██╔══██║
#                              ██████╦╝╚█████╔╝██║░░░░░╚█████╔╝██║░░██║
#                              ╚═════╝░░╚════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
from flask import Flask

from functions import get_movie_or_TV_show_by_title

app = Flask(__name__)

@app.route('/movie/<title>')
def movie_or_TV_show_page(title):
    return f"{get_movie_or_TV_show_by_title(title)}"


if __name__ == '__main__':
    app.run()