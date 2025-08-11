# -*- coding: UTF-8 -*-
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, RDFS, DCTERMS, DC, FOAF, RDFS
import uuid
from rdflib.collection import Collection
import urllib.parse as urlparse
from urllib.parse import quote
from readFiles import readEntries as read

entries = read('category')

# readings = Namespace("http://readings.puyuwang.org/entry/")
# authors = Namespace("http://readings.puyuwang.org/authors/")
BIBO = Namespace("http://purl.org/ontology/bibo/")
READINGS = Namespace("http://readings.puyuwang.org/")

def makeLD(self):
    ''' 
    class for the entries of Readings
    read_date: date of reading the paper, dcterms:accessed
    title: title of the paper, dc:title
    link: link of the paper, dc:source
    authors: authors of the paper, dc:creator
    comments: comments on the paper, rdfs:comment
    date: date of the paper dc:date
    subject: subjects of the paper, dcterms:subject, this is a list
    '''

    g = Graph()
    g.bind("rdf", RDF) 
    g.bind("rdfs", RDFS)
    g.bind("dcterms", DCTERMS)
    g.bind("dc", DC)
    # let g has prefix "readings"
    g.bind("readings", READINGS)

    g.bind("foaf", FOAF)
    g.bind("bibo", BIBO)
    # function for making the linked open data
    # input is an oject of class Entry
    # output is a RDF graph
    
    

    inputEntries = self

    for entry in inputEntries:
        # get the URI for each entry
        entry_resource = URIRef(entry.uri)
        # define the type of the entry
        g.add((entry_resource, RDF.type, BIBO.AcademicArticle))
        # add the read_date to the graph
        g.add((entry_resource, READINGS.dateRead, Literal(entry.read_date)))
        # add the title to the graph
        g.add((entry_resource, DC.title, Literal(entry.title)))
        # add the link to the graph
        g.add((entry_resource, DC.source, Literal(entry.link)))
        # add the authors to the graph
        authorList = []
        for author in entry.authors:
            author_uri = READINGS[f"authors/{quote(author)}"]
            author_resource = URIRef(author_uri)
            # use BNode for the author, since the author is not a resource yet
            # and no need a URI for the author yet
            # uncomment below to use blank node instead of URI for the author
            # author_resource = BNode()   
            g.add((author_resource, RDF.type,  FOAF.Person))
            g.add((author_resource, FOAF.name, Literal(author)))
            g.add((entry_resource, DC.creator, author_resource))
            authorList.append(author_resource)
        
        if authorList:  # Only if there are authors
            author_collection = Collection(g, BNode(), authorList)
            g.add((entry_resource, BIBO.authorList, author_collection.uri))

        # add the comments to the graph
        if entry.comments is not None:
            g.add((entry_resource, RDFS.comment, Literal(entry.comments)))
        # add the date to the graph
        g.add((entry_resource, DC.date, Literal(entry.date)))
        # add the tags to the graph
        #for tag in entry.tags:
        #    g.add((entry_resource, DCTERMS.topic, Literal(tag)))
        if entry.subject is not None:
            for subject in entry.subject:
                g.add((entry_resource, DCTERMS.subject,Literal(subject)))

    
        
    return g


if __name__ == "__main__":
    g = makeLD(entries)
    g.serialize(destination="./RDFs/readings.ttl", format='turtle')
    g.serialize(destination="./RDFs/readings.jsonld", format='json-ld')
