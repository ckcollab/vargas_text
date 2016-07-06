# Import reddit module
import praw


# Connect to reddit as our generator (reddit requires 
# you to specify user agent, apparently)
reddit = praw.Reddit(user_agent='Vargas Markov Generator')
user = reddit.get_redditor('_vargas_')

with open('comments.txt', 'w', encoding='utf8') as output:
    for comment in user.get_comments(limit=None):
        
        comment_text = comment.body + "\n"
        output.write(comment_text)
