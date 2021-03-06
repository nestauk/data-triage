Data source: github-eu-covid
============================

This is to study the contributions to GitHub in the context of the covid-19 pandemic, specifically within the EU.

At time of writing, there were nearly 12,000 repositories tagged with one 231 covid-related topics on GitHub. Of these, 20 topics explicitly mention EU countries. The geographic distribution of the repositories is, of course, blurred by the contribution of global or general packages.

Core entities within the dataset are: repositories, organisations, contributors and topics. From inspection, repositories are broadly:

* Data journalism
* Epidemiological modelling
* Epidemiological measurement
* New technologies with applications to covid (e.g. tracing apps)

The dataset would cost around \$40 to collect, with potentially up to an additional \$400 to collect a counterfactual sample of data. The data collection time would be between 2 hours and 1 day, and data storage costs would be neglible.

Temporal coverage is good, from March 2020 onwards (noting that the number of new repos relating to covid has plateaued since that time).

Unless extensions are required (e.g. in-depth analysis of the codebase), then development will likely take one week. There are uncertainties, since the collection will be batched it could be temperamental. The number of required collections could be significantly higher, but it is difficult to calculate this properly in advance.

Questions from Juan \[unanswered\]:
-----------------------------------

About GitHub

* How does the topic expansion work? I assumed that you are extracting topics that appear in repos with the C19 related topics.
* What do we know about the topic generation process? Do users label their projects with topics to make them easier to find? How confident are we about coverage? (NB last time I collected data from GitHub I used the search api but querying project descriptions with C1. One downside of this is that it only returns the top 1000 relevant results (by number of stars). Maybe we could implement both approaches to improve coverage?
* The location data in user and organisation profiles are very messy. We could standardise it ourselves or use the standard country information in the ghtorrent database available from GoogleBigQuery. Note that only a minority of users provide geo information so this is likely to be biased.
* project descriptions: Your preliminary exploration of the data suggests quite a few interesting topics. How can we classify repos into application domains automatically? I previously collected READMEs from repo master branches but the text was quite messy with markdown syntax, banners etc.
