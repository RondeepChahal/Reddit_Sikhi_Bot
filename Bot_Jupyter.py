
# coding: utf-8

# In[31]:

import praw
import pdb
import re
import os


# In[23]:

reddit = praw.Reddit('bot1')


# In[24]:

subreddit = reddit.subreddit('sikh')


# In[26]:

for submission in subreddit.hot(limit=7):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------\n")


# In[28]:

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to =[]
else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None,posts_replied_to))


# In[30]:

subreddit = reddit.subreddit('sikh')
for submission in subreddit.hot(limit=5):
        if submission.id not in posts_replied_to:
            if re.search("sikhism", submission.title, re.IGNORECASE):
                submission.reply("Thank you for your post. Its 'Sikhi', not 'Sikhism.'")
                print("Bot replying to : ", submission.title)
                posts_replied_to.append(submission.id)


# In[19]:

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

