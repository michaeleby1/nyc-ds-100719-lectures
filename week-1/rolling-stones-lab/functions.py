import matplotlib.pyplot as plt
import csv
with open('data.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)

def find_name(string, data):
    for item in data:
        if string == item['album']:
            return item
    return None

def find_rank(string, data):
    for item in data:
        if string == item['number']:
            return item
    return None

def find_year(string, data):
    year = []
    for item in data:
        if string == item['year']:
            year.append(item)
    return year

def find_by_years(start_year, end_year, data):
    years = []
    for year in range(start_year, end_year+1):
        years.append(find_year(str(year)))
    return years

def find_by_ranks(start_rank, end_rank, data):
    ranks = []
    for rank in range(start_rank, end_rank+1):
        ranks.append(find_rank(str(rank)))
    return ranks

def all_titles(data):
    titles = []
    for item in data:
        titles.append(item['album'])
    return titles

def all_artists(data):
    artists = []
    for item in data:
        artists.append(item['artist'])
    return artists

def most_albums(data):
    frequency_dict = {}
    
    for item in data:
        if item['artist'] not in frequency_dict:
            frequency_dict[item['artist']] = 1
        else: 
            frequency_dict[item['artist']] += 1
    
    highest = {}
    
    highest_album_count = max(frequency_dict.values())
    for key, val in frequency_dict.items():
        if val == highest_album_count:
            highest[key] = val
    
    return highest

def most_popular_word(data):
    titles = all_titles()
    words = []
    for title in titles:
        for word in title.split():
            words.append(word)
            
    frequency_dict = {}
    
    for word in words:
        if word not in frequency_dict:
            frequency_dict[word] = 1
        else: 
            frequency_dict[word] += 1
    
    highest = {}
    
    highest_album_count = max(frequency_dict.values())
    for key, val in frequency_dict.items():
        if val == highest_album_count:
            highest[key] = val
    return highest

def hist_albums(data):
    album_years = []
    for item in data:
        album_years.append(int(item['year']))
    hist_min = (min(album_years)//10)*10
    hist_max = (max(album_years)//10+1)*10
    hist_bins = int((hist_max - hist_min)/10)
    
    plt.hist(album_years, range=(hist_min, hist_max), bins=hist_bins)

def hist_genres(data):
    genres = []
    for item in data:
        genres.append(item['genre'])
    
    split_genres = []
    for genre in genres:
        for word in genre.split(", "):
            split_genres.append(word)
                
    genre_counts = {}
    
    for genre in split_genres:
        if genre not in genre_counts:
            genre_counts[genre] = 1
        else: 
            genre_counts[genre] += 1
    x = genre_counts.keys()
    y = genre_counts.values()
    plt.xticks(rotation='vertical')
    plt.bar(x,y)

text_file = open('top-500-songs.txt', 'r')
lines = text_file.readlines()

def string_to_list(string):
    list_from_string = []
    for item in string.split("\t"):
        list_from_string.append(item)
    return list_from_string

def list_to_dict(song):
    song_dict = {'rank': song[0], 
                 'name': song[1], 
                 "artist": song[2], 
                 "year": song[3].strip('\n')}
    return song_dict

def list_of_songs(data):
    song_dicts = []
    for line in lines:
        list = string_to_list(line)
        song_dicts.append(list_to_dict(list))
    return song_dicts

songs = list_of_songs(lines)

import json

file = open('track_data.json', 'r')
json_data = json.load(file)
albums = json_data

def albumWithMostTopSongs(album_data, song_data):

    song_names = []
    for song in song_data:
        song_names.append(song['name'])
    
    album_count = {} 
    for album in album_data:
        for track in album['tracks']:
            if track in song_names:
                
                if album['album'] not in album_count.keys():
                    album_count[album['album']] = 1
                else:
                    album_count[album['album']] += 1
                               
    highest_album_count = max(album_count.values())

    highest = {}
    
    for key, val in album_count.items():
        if val == highest_album_count:
            highest[key] = val
    return highest                
    
def albumWithTopSongs(album_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])
    
    top_albums = [] 
    for album in album_data:
        for track in album['tracks']:
            if track in song_names:
                top_albums.append(album['album'])
               
    return set(top_albums)

def songsThatAreOnTopAlbums(album_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])

    top_songs = []
    for album in album_data:
        for track in album['tracks']:
            if track in song_names:
                top_songs.append(track)
                    
    return top_songs

def top10AlbumsByTopSongs(album_data, song_data):
    song_names = []
    for song in song_data:
        song_names.append(song['name'])
    
    album_count = {} 
    for album in album_data:
        for track in album['tracks']:
            if track in song_names:
                
                if album['album'] not in album_count.keys():
                    album_count[album['album']] = 1
                else:
                    album_count[album['album']] += 1
    
    sorted_albums = sorted(album_count.values(), reverse=True)[:10]
    #this is just a list of values without keys
    
    top_ten = {}
    #while len(top_ten) < 10:
    for key, val in album_count.items():
        if val in sorted_albums:
            top_ten[key] = val
                
    
    x = top_ten.keys()
    y = top_ten.values() 
    plt.xticks(rotation='vertical')
    plt.bar(x,y)  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


