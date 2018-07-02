# Random PubMed

Get a random NCBI PubMed article.

## Usage

Clone the repo:

```bash
git clone https://github.com/cyclecycle/random_pubmed.git
```

Go:

```python

from random_pubmed import random_pubmed

rand_art = random_pubmed.RandomArticle()
rand_art.email = 'a.n.other@example.com'  # Tell NCBI who you are
article = rand_art.get()  # Python dict of parsed article

```

## Requirements

- Biopython, for querying NCBI's API and parsing results