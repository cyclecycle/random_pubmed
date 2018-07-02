# Random pubmed

Get a random NCBI PubMed article.

## Usage

```python

from random_pubmed import random_pubmed

rand_art = random_pubmed.RandomArticle()

rand_art.email = 'a.n.other@example.com'  # Tell NCBI who you are
article = rand_art.get()  # Python dict of parsed medline format

```

## Requirements

- Biopython, for querying NCBI's API