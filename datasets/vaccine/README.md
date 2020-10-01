Data source: Vaccine
====================

This data triage investigates the Elsevier's journals "Vaccine" and it's open access sister journal "Vaccine: X", though the results are applicable to any of Elsevier's open and closed journals.

Firstly, a procedure has been found to extract basic paper metadata (abstracts, title, year of print, topics, links to tweets) for all papers on Elsevier, which requires no API keys and is therefore more "sustainable" than using MAG, which currently requires a careful use of tricks to avoid paying a hefty fee. For Elsevier's open papers, this procedure could be trivially extended to access the full-text as well - which is something we might choose to look into in the future. We should note though that the number of Elsevier open papers may be relatively low (compared to open "xiv"s), however they might still be of academic interest since they still meet Elsevier's "gold standard" for peer-review.

Despite the above finding, MAG is still found to be beneficial for the core task of extracting "Vaccine" and "Vaccine:X" metadata, since the pipeline for enrichment already exists. The papers have coverage from the year 2000 and are (in principle) global in coverage. It is unclear at this stage how representative the journals are of topic distribution (in terms of social importance), although the journal is said to cover "basic and clinical research, vaccine manufacturing, history, public policy, behavioral science and ethics, social sciences, safety, and many other related areas".

There are over 25,000 articles in "Vaccine" and "Vaccine: X". The total disk space required is negligible (compared to our existing data). The data could be collected and processed in around a day.