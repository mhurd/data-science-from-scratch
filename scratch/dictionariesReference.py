# Dictionaries
#
# Another fundamental data structure is a dictionary, which associates values with keys and allows you
# to quickly retrieve the value corresponding to a given key:

empty_dict = {}                         # Pythonic
empty_dict2 = dict()                    # less Pythonic
grades = { "Joel" : 80, "Tim" : 95 }    # dictionary literal

# You can look up the value for a key using square brackets:

joels_grade = grades["Joel"]            # equals 80

# But you'll get a KeyError if you ask for a key that's not in the dictionary:

try:
    kates_grade = grades["Kate"]
except KeyError:
    print "no grade for Kate!"

# You can check for the existence of a key using in:

joel_has_grade = "Joel" in grades     # True
kate_has_grade = "Kate" in grades     # False

# Dictionaries have a get method that returns a default value (instead of raising an exception)
# when you look up a key that's not in the dictionary:

joels_grade = grades.get("Joel", 0)   # equals 80
kates_grade = grades.get("Kate", 0)   # equals 0
no_ones_grade = grades.get("No One")  # default default is None

# You assign key-value pairs using the same square brackets:

grades["Tim"] = 99                    # replaces the old value
grades["Kate"] = 100                  # adds a third entry
num_students = len(grades)            # equals 3

# We will frequently use dictionaries as a simple way to represent structured data:

tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

# Besides looking for specific keys we can look at all of them:

tweet_keys   = tweet.keys()     # list of keys
tweet_values = tweet.values()   # list of values
tweet_items  = tweet.items()    # list of (key, value) tuples
foo = "user" in tweet_keys            # True, but uses a slow list in
foo = "user" in tweet                 # more Pythonic, uses faster dict in
foo = "joelgrus" in tweet_values      # True

# Dictionary keys must be immutable; in particular, you cannot use lists as keys.
# If you need a multipart key, you should use a tuple or figure out a way to turn the key into a string.

# defaultdict
#
# Imagine that you're trying to count the words in a document. An obvious approach is to create a
# dictionary in which the keys are words and the values are counts. As you check each word, you can increment its
# count if it's already in the dictionary and add it to the dictionary if it's not:

document = ["foo", "bar", "foobar"]

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# You could also use the "forgiveness is better than permission" approach and just handle the exception from
# trying to look up a missing key:

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# A third approach is to use get, which behaves gracefully for missing keys:

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# Every one of these is slightly unwieldy, which is why defaultdict is useful. A defaultdict is like a
# regular dictionary, except that when you try to look up a key it doesn't contain, it first adds a
# value for it using a zero-argument function you provided when you created it. In order to use
# defaultdicts, you have to import them from collections:

from collections import defaultdict

word_counts = defaultdict(int)          # int() produces 0
for word in document:
    word_counts[word] += 1

# They can also be useful with list or dict or even your own functions:
dd_list = defaultdict(list)             # list() produces an empty list
dd_list[2].append(1)                    # now dd_list contains {2: [1]}

dd_dict = defaultdict(dict)             # dict() produces an empty dict
dd_dict["Joel"]["City"] = "Seattle"     # { "Joel" : { "City" : Seattle"}}

dd_pair = defaultdict(lambda: [0, 0])
dd_pair[2][1] = 1                       # now dd_pair contains {2: [0,1]}

