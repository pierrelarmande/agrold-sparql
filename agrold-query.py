from SPARQLWrapper import SPARQLWrapper, JSON, XML, RDFXML
#
# sparql = SPARQLWrapper("http://dbpedia.org/sparql")
# sparql.setQuery("""
#     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#     SELECT ?label
#     WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
# """)

sparql = SPARQLWrapper("http://volvestre.cirad.fr:8890/sparql")
# sparql.setQuery("""
#     BASE <http://www.southgreen.fr/agrold/>
# PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
#
# SELECT distinct ?graph
# WHERE {
#  GRAPH ?graph {
#    ?subject ?predicate ?object.
#  }
#  filter(REGEX(?graph, "^http://www.southgreen.fr/agrold/"))
# }
# """)
#
# sparql.setQuery("""
# select distinct ?Concept where {[] a ?Concept} LIMIT 100
# """)
# sparql1.setReturnFormat(JSON)
# results = sparql1.query().convert()
#
# for result in results["results"]["bindings"]:
#     print('%s: %s' % (result["label"]["xml:lang"], result["label"]["value"]))

#
# graphs = ['http://www.southgreen.fr/agrold/sio',
# 'http://www.southgreen.fr/agrold/so',
# 'http://www.southgreen.fr/agrold/go',
# 'http://www.southgreen.fr/agrold/eco',
# 'http://www.southgreen.fr/agrold/pato',
# 'http://www.southgreen.fr/agrold/po',
# 'http://www.southgreen.fr/agrold/to',
# 'http://www.southgreen.fr/agrold/uniprot.plants',
# 'http://www.southgreen.fr/agrold/gramene.genes',
# 'http://www.southgreen.fr/agrold/rap.msu',
# 'http://www.southgreen.fr/agrold/vocabulary',
# 'http://www.southgreen.fr/agrold/orygenesdb.o.s.indica',
# 'http://www.southgreen.fr/agrold/gramene.cyc',
# 'http://www.southgreen.fr/agrold/orygenesdb.o.s.japonica',
# 'http://www.southgreen.fr/agrold/orygenesdb.a.thaliana',
# 'http://www.southgreen.fr/agrold/gramene.qtl',
# 'http://www.southgreen.fr/agrold/tropgenedb',
# 'http://www.southgreen.fr/agrold/gene.annotations',
# 'http://www.southgreen.fr/agrold/protein.annotations',
# 'http://www.southgreen.fr/agrold/qtl.annotations',
# 'http://www.southgreen.fr/agrold/rapdb.mrna',
# 'http://www.southgreen.fr/agrold/msu.genes',
# 'http://www.southgreen.fr/agrold/qtaro.genes',
# 'http://www.southgreen.fr/agrold/qtaro.qtl',]
graphs = ['http://www.southgreen.fr/agrold/qtaro.genes']
for graph in graphs:
    print(graph)
    sparql.setQuery("""
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
    PREFIX graph:<""" + graph + """>
    SELECT distinct ?subject ?label
    WHERE { 
        GRAPH graph: { 
         ?subject ?relation ?object .
        ?subject rdfs:label ?label .
        } 
        } 
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        print('%s: %s' % (result["subject"]["value"], result["label"]["value"]))