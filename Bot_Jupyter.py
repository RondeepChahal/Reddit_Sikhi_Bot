
# coding: utf-8

# In[1]:

# praw = python reddit api wrapper, re = regular expression
import praw
import pdb
import re
import os


# In[2]:

reddit = praw.Reddit('bot1')


# In[3]:

subreddit = reddit.subreddit('sikh')


# In[4]:

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to =[]
else:
    with open("posts_replied_to.txt","r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None,posts_replied_to))


# In[19]:

subreddit = reddit.subreddit('sikh')
for submission in subreddit.hot(limit=10):
        if submission.id not in posts_replied_to:
            if re.search("sikhism", str([submission.selftext, submission.title]), re.IGNORECASE):
                if re.search("sikhi\s", str([submission.selftext, submission.title]), re.IGNORECASE):
                    pass
                else:
                    submission.reply("Thank you for your post. It's 'Sikhi', not 'Sikhism'.")
                    print("Bot replying to : ", submission.title)
                    posts_replied_to.append(submission.id)


# In[20]:

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

