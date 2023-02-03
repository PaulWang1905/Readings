# -*- coding: UTF-8 -*-
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, RDFS, DCTERMS, DC, FOAF
import uuid
import urllib.parse as urlparse
from readFiles import readEntries as read

entries = read('category')

readings = Namespace("http://readings.puyu.live/entry/")
authors = Namespace("http://readings.puyu.live/authors/")

def makeLD(self):
    g = Graph()
    g.bind("rdf", RDF) 
    g.bind("rdfs", RDFS)
    g.bind("dcterms", DCTERMS)
    g.bind("dc", DC)
    # let g has prefix "readings"
    g.bind("readings", readings)
    g.bind("authors", authors)
    g.bind("foaf", FOAF)
    # function for making the linked open data
    # input is an oject of class Entry
    # output is a RDF graph
    inputEntries = self
    # class for the entries of Readings
    # read_date: date of reading the paper, dc:available
    # title: title of the paper, dc:title
    # link: link of the paper, dc:source
    # authors: authors of the paper, dc:creator
    # comments: comments on the paper, dc:description
    # date: date of the paper dc:date
    # tags: tags of the paper --- not used for the moment
    # future work: add tags, dc:topic 
    
    for entry in inputEntries:
        # get the URI for each entry
        entry_resource = URIRef(entry.uri)
        # define the type of the entry
        g.add((entry_resource, RDF.type, DCTERMS.BibliographicResource))
        # add the read_date to the graph
        g.add((entry_resource, DCTERMS.available, Literal(entry.read_date)))
        # add the title to the graph
        g.add((entry_resource, DC.title, Literal(entry.title)))
        # add the link to the graph
        g.add((entry_resource, DC.source, Literal(entry.link)))
        # add the authors to the graph
        for author in entry.authors:
            
            # use BNode for the author, since the author is not a resource yet
            # and no need a URI for the author yet
            # uncomment below to use URI for the author
            """
            author_uri = authors[urlparse.quote(author)]
            author_resource = URIRef(author_uri)
            """
            author_resource = BNode()
            g.add((author_resource, RDF.type,  FOAF.Person))
            g.add((author_resource, FOAF.name, Literal(author)))
            g.add((entry_resource, DC.creator, author_resource))
        # add the comments to the graph
        if entry.comments != None:
            g.add((entry_resource, DC.description, Literal(entry.comments)))
        # add the date to the graph
        g.add((entry_resource, DC.date, Literal(entry.date)))
        # add the tags to the graph
        #for tag in entry.tags:
        #    g.add((entry_resource, DCTERMS.topic, Literal(tag)))
        
    return g


if __name__ == "__main__":
    g = makeLD(entries)
    g.serialize(destination="./RDFs/readings.ttl", format='turtle')
    g.serialize(destination="./RDFs/readings.json", format='json-ld')
