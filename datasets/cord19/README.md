Data source: cord19
=========================
The [Semantic Scholar](https://www.semanticscholar.org/cord19) team at the Allen Institute for AI has partnered with leading research groups to provide CORD-19.

The dataset contains all COVID-19 and coronavirus-related research (this means pre-2020 research too) from the following sources:

- PubMed's PMC open access corpus using this query (COVID-19 and coronavirus research)
- Additional COVID-19 research articles from a corpus maintained by the WHO
- bioRxiv and medRxiv pre-prints using the same query as PMC (COVID-19 and coronavirus research)

Semantic Scholar provides **daily** data dumps. You can find a detailed description (and data dictionary) for each file of the data dump [here](https://github.com/allenai/cord19#overview). Briefly:
- `metadata.csv`: The core dataset. Semantic Scholar recommends working with it.
- `cord_19_embeddings.tar.gz`: A CSV (when unzipped) containing an embedding for each paper.
- `document_parses/`: Directory with the full text of each paper. 

## Notes
- The Semantic Scholar team recommends to _primarily use metadata.csv & augment data when needed with full text in document_parses/_.
- CORD19 contains duplicates which can be filtered out using the `cord_uuid` field. Read here [why](https://github.com/allenai/cord19#why-can-the-same-cord_uid-appear-in-multiple-rows).
- We would need to map CORD19 with MAG in order to get the author affiliations, geocode them and focus on EU-related research. You can find the mapping [here](https://github.com/microsoft/mag-covid19-research-examples/blob/master/src/data/releases.md#current-and-past-releases).
- [CORD19 FAQ](https://github.com/allenai/cord19#questions-about-cord-19)