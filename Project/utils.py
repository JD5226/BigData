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

def do_search_simple(df,search_items):
    def score_row(row, search_terms):
        score = 0
        for column, search_value in search_terms.items():
            if column=='job_skills':
                for skill in search_value:
                    if skill.lower() in str(row[column]).lower():
                        score += 1
            elif search_value.lower() in str(row[column]).lower():
                score += 1
        return score
    
    df['score'] = df.apply(score_row, axis=1, args=(search_items,))
    
    df_searched = df[df['score']>0]

    # Sort the DataFrame based on the score
    sorted_df = df_searched.sort_values(by='score', ascending=False)
    
    return sorted_df[['job_link','job_title','company','job_location','job_type']]

# search page setting
def paginate_dataframe(df, page_size, page_num):
    start_index = page_size * (page_num - 1)
    end_index = start_index + page_size
    return df.iloc[start_index:end_index]





if __name__ == '__main__':
    test = load_skills('D:/0 NYU/BigData/Project/data/tag.json')
    print(test)
