from Minhash import Minhash
from LSH import LSH

# Jaccard similarity
def Jaccard_sim(doc1, doc2):
    if len(doc1 | doc2) == 0:
        return 1
    return len(doc1 & doc2) * 1.0 / len(doc1 | doc2)

# filtering for word count >= 5 and form bag_of_words set for each document

f = open('./docword.nips.txt','rb')
i = -1
doc = {}
for line in f:
    i += 1
    if i < 3:
        continue
    tokens = [int(x) for x in line.strip().split(' ')]
    # bag of words
    doc_id = tokens[0]
    word_id = tokens[1]
    count = tokens[2]
    if doc.get(doc_id) is None:
        doc[doc_id] = set()
    elif count > 4:
        doc[doc_id].add(word_id)

# calculate minhash signature for all documents
mh_sig = {}
minhash = Minhash(40)
for doc_id in doc:
    words = doc[doc_id]
    mh_sig[doc_id] = minhash.cal(words)

#update the lsh
lsh = LSH(20, 40)
for key, value in mh_sig.iteritems():
    lsh.update(key,value)

# An example
key = 86
candidates = lsh.query(mh_sig[key], key)
for can in candidates:
    print can, ':',Jaccard_sim(doc[key],doc[can])