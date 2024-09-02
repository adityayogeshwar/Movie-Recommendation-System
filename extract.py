import ast
def covert_genres_keywords(obj):
    l = []
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l
def convert_cast(obj):
    l=[]
    for i in ast.literal_eval(obj)[:3]:
        l.append(i['name'])
    return l


def extract_director(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if (i['job'] == 'Director'):
            l.append(i['name'])
            break
    return l
def fetch_movies(new_df):
    return sorted(list(new_df['title'].values))
