# Kibana - Elasticsearch

Firstly we need download and run kibana and elasticsearch. Then we will have Elasticsearch in http://localhost:9200 and Kibana in http://localhost:5601

You can follow the next instructions https://www.elastic.co/start to install all of them.

In linux line commands you can do:

```pip install elasticsearch```


```
{
  "name" : "hqCq4M8",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "9bPQA",
  "version" : {
    "number" : "5.5.0",
    "build_hash" : "26038d",
    "build_date" : "2017-06-30T23:16:05.735Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.0"
  },
  "tagline" : "You Know, for Search"
}
```

Document sent to Elastic Search:

![ES](doc_elastic.png)

Now we create a new index in Kibana for the document that we sent to Elastic Search:

![ES](c_index.png)

![ES](n_index.png)


The next step is create each visualization to add them to a new dashboard.

![ES](visualize.png)

![ES](weather.png)

![ES](dashboard.png)

