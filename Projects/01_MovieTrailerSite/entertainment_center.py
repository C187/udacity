import fresh_tomatoes
import media

# Creates instances of my favorite movies with the Movie object
children_of_men = media.Movie(
    "Children of Men",
    "http://www.gstatic.com/tv/thumb/movieposters/"
    "159796/p159796_p_v8_ag.jpg",
    "https://www.youtube.com/watch?v=2VT2apoX90o")

the_martian = media.Movie(
    "The Martian",
    "http://t2.gstatic.com/images?q=tbn:"
    "ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC"
    "_Okgxi1eX6diuOT3xKWXQ",
    "https://www.youtube.com/watch?v=ej3ioOneTy8")

star_trek_fc = media.Movie(
    "Star Trek: First Contact",
    "http://t2.gstatic.com/images?q=tbn:ANd9GcQqKE15E"
    "vuPYXqFa5X1PWPlljp1pu5Ss1UUNS98qp8RkJnSBSUU",
    "https://www.youtube.com/watch?v=YQ1eiEvefKI")

bttf = media.Movie(
    "Back to the Future",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcT9d_lBBx"
    "0xxB7_d4RP82MlRcK82lzT2W1ZavxhV39SSTZOofDX",
    "https://www.youtube.com/watch?v=qvsgGtivCgs")

hackers = media.Movie(
    "Hackers",
    "http://www.gstatic.com/tv/thumb/movieposters/"
    "17164/p17164_p_v8_ab.jpg",
    "https://www.youtube.com/watch?v=Rn2cf_wJ4f4")

armitage = media.Movie(
    "Armitage III: Poly-Matrix",
    "http://movie-gazette.com/images/gallery/"
    "albums/A//armitage-iii-polymatrix.jpg",
    "https://www.youtube.com/watch?v=iXKAsybyIRw")

blade_runner = media.Movie(
    "Blade Runner",
    "https://upload.wikimedia.org/wikipedia/"
    "en/5/53/Blade_Runner_poster.jpg",
    "https://www.youtube.com/watch?v=eogpIG53Cis")

network = media.Movie(
    "Network",
    "http://t3.gstatic.com/images?q=tbn:ANd9GcRb2hVTyo4nNmB"
    "-UTxDvDnZBOHgeDPq9Wl-sOaM5-sVDNghePg6",
    "https://www.youtube.com/watch?v=1cSGvqQHpjs")

tmfe = media.Movie(
    "The Man from Earth",
    "http://www.gstatic.com/tv/thumb/dvdboxart/"
    "174565/p174565_d_v8_aa.jpg",
    "https://www.youtube.com/watch?v=9mOIxyRTY5I")

# Stores movie object in a list
movies = [children_of_men,
          the_martian,
          star_trek_fc,
          bttf,
          hackers,
          armitage,
          blade_runner,
          network,
          tmfe]

# Generates the movie list page with the movies in the list
fresh_tomatoes.open_movies_page(movies)
