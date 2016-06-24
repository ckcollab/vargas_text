# Import random text generator
import markovify

comment_text = open("comments.txt", 'r', encoding='utf8').read()
text_model = markovify.Text(comment_text)

# Print five randomly-generated sentences
for i in range(5):
    print(text_model.make_sentence())
