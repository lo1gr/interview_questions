## The classic "Tell me about a project":

#### Japanese Restaurant project
Goal was to predict the number of customers expected for restaurants
~ SIZE DATA?

Time series forecasting problem essentially.

input:
 restaurant id, time reservation was made, time for reservation, number visitors for resa
 type restaurants (korean bbq, sushi (abt 15 categories)), area name, latitude & longitude of area
 day of visit, number of visitors on that Day

 Have to forecast for in the future.


Key of the project lay in the Feature Engineering performed:
Transformation of variables + exogenous components to try an test whether the day was going to bring more customers or not:
variables introduced included the following:
- holiday: cross check to see if the day was a holiday or not (0 or 1)
- Golden week (april 5 to May 2): big holiday in Japan: (0 or 1)
- days preceding holiday lag: (0 or 1)
- period of the month (beginning, middle, end) (japanese typically paid 25th or end of month): thinking is that at beginning of the month people
- difference between number of people resa made at and number showed up -> inconclusive
- difference between time reseravation placed and when it was -> the thinking was that the highest, the more likely it was that it was a known restaurant


Used XgBoost
Since XGBoost does not provide specialization for categorical features;
And our data contained categorical features, had to one-hot encode them increasing the dimension of our dataset.
We had 15 categories (and we grouped some together: eg: more entertainment like karaoke and other, bars...)


#### Grocery Sales
Corporacion Favorita Grocery sales

#### Amazon time series correction

#### Computer vision Eleven
Goal of the project was to recognize digits from a gas pump. Picture was taken by truck drivers and then sent on their ipad,
so that management knew the consumption of the trucks.

~ around 1000 images
Used openCv:
Step 1: modify the image to make it more readable, some images too dark, others too light...
Step 2: find the contours of the screen: used cornerharris (hard because sometimes shadow can be thought of as corner, just like thumb in pic) => took the most outer corners
Step 3: crop the image to keep the quadrant
Step 4: Thought of different methods to cut the numbers, none was really working until we split the screen into 4 equal parts. Then it is easier
Step5: Run pre trained neural net (Used Pre-Trained neural net on handwritten digits (MNIST)) on the single digit
Step6: combine output to get the number on the pump

#### NLP project Quinten
Challenge was to cluster medical documents together using NLP.
We had the abstract of the document, plus a title and finally the abstract id.
We wanted to cluster documents together, and output labels for the documents
~ around 8000 documents

packages: gensim (embedding)

1) Remove stopwords, not only choose the regular stopwords, but stopwords useful for medical stopwords,
using more extended versions of stopwords
2) Lemmatization of the words, and not stemming because lemmatization keeps the meaning
3) Word embedding of the words, trying different embeddings. Word embedding means mapping a vector to each word.
Word2Vec is trained on Google News, and therefore might not have been appropriate for our medical corpus.
king-man+woman = queen. 2 models: CBOW model for predicting blank word, The Skip-gram model takes the input as each word in the corpus, sends them to a hidden layer (embedding layer) and from there it predicts the context words. Once trained, the embedding for a particular word is obtained by feeding the word as input and taking the hidden layer value as the final embedding vector.
Glove is to reduce dimensionality of dataset: Glove is based on matrix factorization techniques on the word-context matrix. It first constructs a large matrix of (words x context) co-occurrence information, i.e. for each “word” (the rows), you count how frequently we see this word in some “context” (the columns) in a large corpus.  The number of “contexts” is of course large, since it is essentially combinatorial in size. So then we factorize this matrix to yield a lower-dimensional (word x features) matrix, where each row now yields a vector representation for each word. In general, this is done by minimizing a “reconstruction loss”. This loss tries to find the lower-dimensional representations which can explain most of the variance in the high-dimensional data.
Settled more on Biowordvec: provides fastText word embeddings trained using PubMed and MeSH. fastText is another word embedding method that is an extension of the word2vec model. Instead of learning vectors for words directly, fastText represents each word as an n-gram of characters.

Also tried sentence embedding with BioSentVec.

4) Then summed the vectors (embeddings of the words) to obtain the embeddings of the documents

5) Performed clustering methods on those ()
6) selected label based on clustering methods
7) output label for docs
