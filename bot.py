import tweepy # for tweeting
import secrets # shhhh
import nltk # for sentence parsing
nltk.download('punkt')

def get_next_chunk():
  # open text file
  text_file = open('book.txt', 'r+')
  text_string = text_file.read()
  # separate the text into sentences
  tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = tokenizer.tokenize(text_string)
  # tweet the whole sentence if it's short enough
  if len(sentences[0]) <= 140:
    chunk = sentences[0]
  # otherwise just print the first 140 characters
  else:
    chunk = sentences[0][0:140]

  # delete what we just tweeted from the text file
  text_file.seek(0)
  text_file.write(text_string[len(chunk):len(text_string)])
  text_file.truncate()
  text_file.close()
  return chunk

def tweet(message):
  auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
  auth.set_access_token(secrets.access_token, secrets.access_token_secret)
  api = tweepy.API(auth)
  auth.secure = True
  print("Posting message {}".format(message))
  api.update_status(status=message)

tweet(get_next_chunk())