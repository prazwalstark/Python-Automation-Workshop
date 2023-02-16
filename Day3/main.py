import openpxyl

try:
    html=requests.get("https://www.imdb.com/chart/top/")
    html.raise_for_statues()
except Exception as e:
    print(e)

#initialize BeautifulSoup for parsing HTML and XML documents
soup = BeautifulSoup(html.text,'html.parser')


#We now link all the data linked to movies_data_variable (parsing) imdb data
movies = soup.find("tbody",class_="lister-list").find_all("tr")

moviesDataTitle=['Rank','Name','Year of Release','Rating']

moviesData=[]

for movie in movies:
    name = movie.find('td',class_="titlecolumn").a.text
    rank = movie.find('td',class_="titlecolumn").get_text(strip=True).split('.')[0]
    year=movie.find('td',class_="titlecolumn").span.text.strip('()')
    rating = movie.find('td',class="ratingColumn imdbRating").strong.text

    moviesData.append([rank,name,year,rating])
    
