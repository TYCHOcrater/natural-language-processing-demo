from textblob import TextBlob
import random

pride_blob = TextBlob(open("pride.txt").read())

pos = "NN"

parts = []
print("Finding all the parts...")
for word, tag in pride_blob.tags:
    if tag == pos:
        parts.append(word)

output = ""
print ("Replacing all the parts...")
for line in open("manifesto.txt").readlines():
    for word, tag in TextBlob(line.tags:
            if tag == pos:
                line = line.replace(word, random.choice(parts))
        output += line

    f = open("output_compare.txt", "w")
    f.write(output)
    f.close()

print("Done!")
