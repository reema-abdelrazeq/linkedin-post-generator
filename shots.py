import json
import pandas as pd



class shotPosts:
    def __init__(self, file_path="processed_posts.json"):
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)

    def load_posts(self, file_path):
        with open(file_path, encoding="utf-8") as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)
            df["length"]=df["line_count"].apply(self.length)
            all_tags=df['tags'].apply(lambda x:x).sum()
            self.unique_tags=set(list(all_tags))
            self.df = df

    def length(self, line_count):
        if line_count <5:
            return "short"
        elif 5<=line_count <=10:
            return "medium"
        else:
            return "long"

    def get_tags(self):
        return self.unique_tags

    def get_filtered_posts(self,length,language,tag):
        df_filtered=self.df[
            (self.df['language']==language)&
            (self.df['length']==length)&
            (self.df['tags'].apply(lambda tags:tag in tags))
        ]
        return df_filtered.to_dict(orient="records")

if __name__ == "__main__":
    fs = shotPosts()
    posts=fs.get_filtered_posts("long","English","careeradvice")
    print(posts)