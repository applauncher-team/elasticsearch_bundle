# Elasticsearch bundle for AppLauncher
Elasticsearch support for applauncher. This is a wrapper of the python standard library so there not any dependecies

Installation
-----------
```bash
pip install elasticsearch_bundle
```
Then add to your main.py
```python
import elasticsearch_bundle

bundle_list = [
    elasticsearch_bundle.ElasticsearchBundle(),
]
```

Configuration
-------------
```yml
elasticsearch:
   hosts:
     - localhost
   use_iam: False,
   iam_access_key: "",
   iam_secret_key: "",
   iam_region: "",
```
To use Amazon IAM for authentication, put "use_iam" to True and fill the other fields

Using the bundle
-----------------
Just inject the instance

```python
import inject
from elasticsearch import Elasticsearch
es = inject.instance(Elasticsearch)
print(es)
```
