import extract
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

cv = CountVectorizer(max_features=6000, stop_words='english')

def stem(text):
    l=[]
    for i in text.split():
        l.append(ps.stem(i))
    return " ".join(l)
def preprocess(movies, cr):
    # Create copies of DataFrames to avoid SettingWithCopyWarning
    movies_copy = movies.copy()
    cr_copy = cr.copy()

    # Merge DataFrames
    df = movies_copy.merge(cr_copy, on='title')

    # Select desired columns
    df = df[['id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    # Drop rows with missing values
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Apply transformations
    df['genres'] = df['genres'].apply(extract.covert_genres_keywords)
    df['keywords'] = df['keywords'].apply(extract.covert_genres_keywords)
    df['cast'] = df['cast'].apply(extract.convert_cast)
    df['Director'] = df['crew'].apply(extract.extract_director)
    df.drop(columns=['crew'], axis=1, inplace=True)
    df.overview = df.overview.apply(lambda x: x.split())

    # Remove spaces between categories and concatenate into a single column
    df['genres'] = df['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
    df['keywords'] = df['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
    df['cast'] = df['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
    df['Director'] = df['Director'].apply(lambda x: [i.replace(" ", "") for i in x])
    df['tags'] = df['overview'] + df['keywords'] + df['cast'] + df['Director']
    df = df[['id', 'title', 'tags']]

    # Combine lists into strings
    df['tags'] = df['tags'].apply(lambda x: " ".join(x))
    df['tags'] = df['tags'].str.lower()

    # Stemming and vectorization
    df['tags'] = df['tags'].apply(stem)
    vectors = cv.fit_transform(df['tags'])
    similarity = cosine_similarity(vectors)

    return similarity,df

