import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# stopwords is a collection of words that dont convey meaning. mostly pronouns such as he she etc.

#Generate Word Cloud
source_text = "Reporting directly to the Engineering Manager, you will dive in and take ownership of our existing codebase, helping extend and scale our bespoke recommendations engine, order management, inventory, shipping, and reporting components. This is a great opportunity to lead the engineering team of a startup that is already profitable, already a well-known brand for women, but is still growing fast even in COVID times. We need someone who can not only build our existing codebase, but also push the envelope, as we are developing some sophisticated data science capabilities, similar to Netflix, Amazon, and Stitch Fix.Founded in 2014, Nadine West sends personalized outfits to our customers’ doorsteps every month. We are based in Austin TX, but we are a remote-first company, so you can live and work anywhere."

#generate the wordcloud object, set the height and width, set the random_state parameter to ensure reproducibility of results and set the stopwords parameter so that the irrelevant words such as pronouns are discarded.

wordcloud = WordCloud(width=3000, height=2000, random_state=1, background_color="green", collocations=False, stopwords=STOPWORDS).generate(source_text)

# text is the input to the generate() method
#draw the figure
#Set figure size
plt.figure(figsize=(40, 30))
#Display image
plt.imshow(wordcloud)
#No axis
plt.axis("off")
plt.show()