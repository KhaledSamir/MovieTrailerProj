import media
import fresh_tomatoes

TOYSTORY = media.Movie('Toy Story',
                       'A Story of Toy like a boy!',
                       'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                       'https://www.youtube.com/watch?v=NTdKQzVFeis')

AVATAR = media.Movie('Avatar',
                     'A Marine on an alient planet',
                     'http://www.impawards.com/2009/posters/avatar_xlg.jpg',
                     'https://www.youtube.com/watch?v=5PSNL1qE6VY')

WHITEFANG = media.Movie('White Fang',
                        'A story of half dog and half wolf',
                        'http://www.impawards.com/1991/posters/white_fang_xlg.jpg',
                        'https://www.youtube.com/watch?v=u6rpsATIqes')

TITANIC = media.Movie('Titanic',
                      'A sink ship on 1914',
                      'https://www.movieposter.com/posters/archive/main/142/MPW-71146',
                      'https://www.youtube.com/watch?v=zCy5WQ9S4c0')

THEMASK = media.Movie('The Mask',
                      'Bank clerk Stanley Ipkiss is transformed into' +
                      'a manic superhero when he wears a mysterious mask.',
                      'https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5NDU3NTYzM15BMl5BanBnXkFtZTYwMzYxMjQ5._V1_.jpg',
                      'https://www.youtube.com/watch?v=hOqVRwGVUkA')

TERMINATOR = media.Movie('The Terminator',
                         'A cyborg, identical to the one who failed to kill Sarah Connor,' +
                         'must now protect her ten year old son, John Connor, from a more advanced cyborg.',
                         'https://s-media-cache-ak0.pinimg.com/236x/92/ed/43/92ed43c0eb8ef6126a5bd02170476a4a--terminator-poster-the-terminator.jpg',
                         'https://www.youtube.com/watch?v=c4Jo8QoOTQ4')

# Movies List to be send to the front page to view them.
MOVIES = [THEMASK, TOYSTORY, AVATAR, WHITEFANG, TITANIC, TERMINATOR]
fresh_tomatoes.open_movies_page(MOVIES)
