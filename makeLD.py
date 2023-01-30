# -*- coding: UTF-8 -*-
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, RDF, RDFS, XSD, DCMI
import uuid
class entry():
    # class for the entries of Readings
    # read_day: day of reading
    # title: title of the paper
    # link: link of the paper
    # authors: authors of the paper
    # comments: comments on the paper
    # date: date of the paper
    # tags: tags of the paper
    def __init__(self, read_day, title, link, authors, comments,date, tags):
        self.read_day = read_day
        self.title = title
        self.link = link
        self.authors = authors
        self.comments = comments
        self.date = date
        self.tags = tags
    
g = Graph()
g.bind("foaf", FOAF)
g.bind("rdf", RDF) 
g.bind("rdfs", RDFS) 
g.bind("xsd", XSD) 
g.bind("dcmi", DCMI)

book = URIRef("http://example.org/people/Bob")


bob = URIRef("http://example.org/people/Bob")
linda = URIRef("http://example.org/people/Linda")
testClass = URIRef("http://example.org/class/testClass")



if __name__ == "__main__":
    g.serialize(destination="./RDFs/test.ttl")
