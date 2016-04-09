# locality sensitive hashhing
# k = rb

class LSH:
    def __init__(self, b, k):
        self.b = b
        self.k = k
        self.r = k / b
        self.buckets = [{} for i in range(b)]

    # update
    def update(self, docid, sig):
        for i in range(self.b):
            hash_value = hash(tuple(sig[i*self.r:(i+1)*self.r]))
            if hash_value not in self.buckets[i]:
                self.buckets[i][hash_value] = set()
                self.buckets[i][hash_value].add(docid)
            else:
                self.buckets[i][hash_value].add(docid)
    # query
    def query(self, sig, docid):
        candidates = set()
        for i in range(self.b):
            hash_value = hash(tuple(sig[i*self.r:(i+1)*self.r]))
            if hash_value in self.buckets[i]:
                candidates.update(self.buckets[i][hash_value]);
        if docid in candidates:
            candidates.remove(docid)
        return candidates