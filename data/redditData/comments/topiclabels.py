"""
To add topic label to comments by searching for the parent submission topic
"""

import pandas as pd
import numpy as np
import os 
if os.path.exists(dir:="data/redditData"): os.chdir(dir)

comments: pd.DataFrame = pd.read_pickle('./topic_only_submission_comments_df.pkl')
submissions: pd.DataFrame = pd.read_pickle('./topic_only_submission_df.pkl')

comments = comments.where(~comments.body.isin(['[deleted]','[removed]'])).dropna()
comments = comments.drop_duplicates(subset=['id'])
comments = comments.sort_values(by=['parent_id','id'])
comments = comments.reset_index(drop=True)
comments['topic'] = ''

# comments = comments.head(500)

def label_topic(row:pd.core.series.Series) -> pd.core.series.Series:
    # print('processing: ',row.id)
    pid = row.parent_id
    if str(pid).startswith('t3'):
        parent = submissions.loc[submissions.id == pid[3:]]
        if parent.empty: return row
        row.topic = parent.iloc[0].topic
    elif str(pid).startswith('t1'):
        parent = comments.loc[comments.id == pid[3:]]
        if parent.empty: return row
        parent = label_topic(parent.iloc[0])
        if type(parent) is str: return row
        row.topic = parent.topic
    else:
        return row
    return row

comments = comments.apply(label_topic,axis='columns')

comments.topic = comments.topic.where(comments.topic!='',other='misc')
comments.topic = comments.topic.str.lower()

comments.to_pickle('comments-topic-labelled.pkl')

print('end')
