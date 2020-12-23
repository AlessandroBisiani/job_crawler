# Job_crawler
### A web crawler for collating python-job related information in Python with scrapy

<br>

### Includes:
* _environment.yml_: A conda environment file (the default environment name is "_job-crawler_")
* The scrapy file infrastructure

Find the crawlers under _job_crawler/spiders/_

### Requires
* Python <= 3.8.5
* scrapy
Use environment.yml to build the conda environment with:
conda env create -n YOUR_ENV_NAME —file environment.yml

<br>

## Use

```
scrapy crawl SPIDER_NAME -O OUTPUT_FILE.json
````

`-O` will overwrite the output file. Use `-o` to append.
<br>

Currently, only the stackoverflow spider is implemented. For example, use:

```shell
scrapy crawl stack_overflow_jobs -O stackoverflow.json
```

Directly specify `.csv`, `.json`, `.jsonlines`, or `.xml` files. <br>
For many more options, refer to the scrapy docs [here]('https://docs.scrapy.org/en/latest/topics/feed-exports.html#topics-feed-format-jsonlines).

<br>

## Output
A list of dictionaries of keys: job_title, company, link, and skills

#### Sample Output
{"job_title": "Data Engineer (m/f/d) Berlin/ Bielefeld/full-remote", "company": "Egoditor GmbH", "link": "/jobs/466444/data-engineer-m-f-d-berlin-bielefeld-full-egoditor-gmbh", "skills": ["sql", "python"]},<br>
{"job_title": "(Senior) Python Engineer (m/f/d) - Search & Ride Experience", "company": "TIER Mobility GmbH", "link": "/jobs/461175/senior-python-engineer-m-f-d-search-ride-tier-mobility-gmbh", "skills": ["python", "agile", "tdd", "walrus-operator"]},<br>
... <br>
... etc.

<br>
<br>
<br>

#### TODO
- Parse m-dashes, umläute, etc. ("Hacker \u2013 Spezialist f\u00fcr CNE-Operationen (m/w/d)")