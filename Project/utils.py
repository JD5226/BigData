import pandas as pd
import json

def load_skills(dir):
    skill_tag_list = []
    with open(dir,'r') as file:
        skill_tag_list = json.load(file)['skill_tags']
    
    return skill_tag_list

def do_search(df):
    # return the neccessary dataframe columns
    
    return df[['job_link','job_title','company','job_location','job_type']] # for debug

# search page setting
def paginate_dataframe(df, page_size, page_num):
    start_index = page_size * (page_num - 1)
    end_index = start_index + page_size
    return df.iloc[start_index:end_index]



if __name__ == '__main__':
    test = load_skills('D:/0 NYU/BigData/Project/data/tag.json')
    print(test)
