
from urlextract import URLExtract
from wordcloud import WordCloud
extract = URLExtract()

def fetch_stats(selected_user,df):

    if selected_user != "overall":
        df =df[df['user'] == selected_user]
    # 1. fetch the number of messages
    num_messages = df.shape[0]

    # 2, fetch number of words
    word = []
    for messages in df['message']:
       word.extend(messages.split())

    # 3. Fetch number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # 4. fetch links

    links = []
    for messages in df['message']:
        links.extend(extract.find_urls(messages))

    return num_messages,len(word),num_media_messages,len(links)


def fetch_most_busy_user(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percent'})
    return x,df

def create_word_cloud(selected_user,df):
    if selected_user != 'overall':
        df = df[df['user']== selected_user]
    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc






