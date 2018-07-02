from random import randint
from Bio import Entrez, Medline


SOURCES = {'pubmed', 'medline'}
MAX_TRIES = 20


class RandomArticle():

    def __init__(self, email=None, source=None):
        self.email = email
        self.source = source
        if source:
            self.check_source()


    def check_source(self):
        assert self.source in SOURCES, '\'source\' must be in {}'.format(str(SOURCES))


    def get(self):
        self.check_source()
        if self.source == 'pubmed':
            return self.get_rand_pubmed()
        if self.source == 'medline':
            return self.get_rand_medline()


    def get_rand_pubmed(self):
        self.check_source()
        Entrez.email = self.email
        for i in range(MAX_TRIES):
            uid = randint(1, 99999999)
            handle = Entrez.efetch(db='pubmed', id=[str(uid)], rettype='medline', retmode='text')
            records = Medline.parse(handle)
            record = list(records)[0]
            if not 'id:' in record:  # Signals error in the return dict
                return record


    def get_rand_medline():
        pass


if __name__ == '__main__':

    rand_art = RandomArticle(email='nick.morley@hotmail.com', source='pubmed')
    article = rand_art.get()
    print(article)
