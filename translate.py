from textblob import TextBlob

text = open("pride.txt").read() [0:2000]
en_blob = TextBlob(text)

print("Translating...")
blob = en_blob.translate(to="es").translate(from_lang="es", to="en").translate(to="sw").translate(from_lang="sw", to="en")
output = str(blob)

f = open("output_parts-of-speech.txt", "w")
f.write(output)
f.close()

print("Done!")
