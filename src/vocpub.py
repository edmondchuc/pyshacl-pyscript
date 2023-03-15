shapes = """
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX reg: <http://purl.org/linked-data/registry#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX sdo: <https://schema.org/>
PREFIX sh: <http://www.w3.org/ns/shacl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
BASE <https://w3id.org/profile/vocpub/validator/>


<https://w3id.org/profile/vocpub/validator>
    a owl:Ontology ;
    skos:prefLabel "VocPub Validator"@en ;
    skos:definition "SHACL validator for the VocPub Profile"@en ;
    dcterms:creator <https://orcid.org/0000-0002-8742-7730> ;
    dcterms:publisher <https://linked.data.gov.au/org/agldwg> ;
    dcterms:created "2020-06-14"^^xsd:date ;
    dcterms:modified "2023-02-24"^^xsd:date ;
    owl:versionIRI <https://w3id.org/profile/vocpub/validator/3.0> ;
    owl:versionInfo "3.0: Removed Requirement-2.3.5 (identifiers) as these are auto-generated in systems like VocPrez; Added Requirement-2.1.10 & 2.1.11 and sub parts to test for qualifiedDerivation and status of a ConceptScheme" ;
.

<https://linked.data.gov.au/org/agldwg> a sdo:Organization ;
    sdo:name "Australian Government Linked Data Working Group" ;
    sdo:url "https://www.linked.data.gov.au"^^xsd:anyURI ;
.

<https://orcid.org/0000-0002-8742-7730> a sdo:Person ;
    sdo:name "Nicholas J. Car" ;
    sdo:email "nicholas.car@anu.edu.au"^^xsd:anyURI ;
    sdo:identifier "https://orcid.org/0000-0002-8742-7730"^^xsd:anyURI ;
.

#
#   ConceptScheme
#
# Requirement-2.1.1 so far un-implemented in SHACL

# Requirement-2.1.2 included below

<Requirement-2.1.2+3>
    a sh:NodeShape ;
    sh:targetNode skos:ConceptScheme ;
    sh:property [
        sh:path [ sh:inversePath rdf:type ] ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:message "Requirement 2.1.2 Each vocabulary _MUST_ be presented as a single skos:ConceptScheme object & Requirment 2.1.3 Each vocabulary MUST be presented in a single file which does not contain information other than that which is directly part of the vocabulary and the file is considered the point-of-truth" ;
    ] ;
.

<Requirement-2.1.4a>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
        sh:message "Requirement 2.1.4 Each vocabulary _MUST_ have one and only one title, a text literal, indicated using the skos:prefLabel predicate" ;
        sh:property [
        sh:path skos:prefLabel ;
        sh:minCount 1 ;
        sh:uniqueLang true ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.1.4b>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
        sh:message "Requirement 2.1.4 Each vocabulary _MUST_ have one and only one definition, a text literal text, indicated using the skos:definition predicate" ;
        sh:property [
        sh:path skos:definition ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.1.5>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
        sh:property [
        sh:path dcterms:created ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:or (
            [
                sh:datatype xsd:dateTime ;
            ]
            [
                sh:datatype xsd:date ;
            ]
            [
                sh:datatype xsd:dateTimeStamp ;
            ]
        ) ;
        sh:message "Requirement 2.1.5 Each vocabulary _MUST_ have one and only one created date indicated using the dcterms:created predicate that must be either an `xsd:date`, `xsd:dateTime` or `xsd:dateTimeStamp` literal value" ;
    ] ;
    sh:property [
        sh:path dcterms:modified ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:or (
            [
                sh:datatype xsd:dateTime ;
            ]
            [
                sh:datatype xsd:date ;
            ]
            [
                sh:datatype xsd:dateTimeStamp ;
            ]
        ) ;
        sh:message "Requirement 2.1.5 Each vocabulary _MUST_ have one and only one modified date indicated using the dcterms:modified predicate that must be either an `xsd:date`, `xsd:dateTime or `xsd:dateTimeStamp` literal value" ;
    ] ;
.

<Requirement-2.1.6a>
	a sh:NodeShape ;
	sh:property [
	    sh:path dcterms:creator ;
            sh:minCount 1 ;
	    sh:description "Requirement 2.1.6 Each creator agent associated with a vocabulary _MUST_ be typed as an `sdo:Person`, `sdo:Organization` or `sdo:GovernmentOrganization`" ;
	    sh:or (
	        [ sh:class sdo:GovernmentOrganization ]
		[ sh:class sdo:Organization ]
		[ sh:class sdo:Person ]
	    ) ;
	] ;
.

<Requirement-2.1.6b>
	a sh:NodeShape ;
	sh:property [
	    sh:path dcterms:publisher ;
            sh:minCount 1 ;
	    sh:description "Requirement 2.1.6 Each publisher agent associated with a vocabulary _MUST_ be typed as an sdo:Person, sdo:Organization or sdo:GovernmentOrganization" ;
            sh:or (
                [ sh:class sdo:GovernmentOrganization ]
                [ sh:class sdo:Organization ]
                [ sh:class sdo:Person ]
            ) ;
	] ;
.

<Requirement-2.1.7a>
    a sh:NodeShape ;
    sh:message "Requirement 2.1.7 Provenance for a ConceptScheme _MUST_ be indicated by at least one of the following properties: dcterms:provenance, dcterms:source or prov:wasDerivedFrom." ;
    sh:or (
        [
            sh:minCount 1 ;
            sh:path prov:wasDerivedFrom ;
            sh:message "This is a message about prov:wasDerivedFrom" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:source ;
            sh:message "This is a message about dcterms:source" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:provenance ;
            sh:message "This is a message about dcterms:provenance" ;
        ]
    ) ;
    sh:targetClass skos:ConceptScheme ;
.

<Requirement-2.1.7b>
    a sh:NodeShape ;
    sh:targetSubjectsOf dcterms:provenance ;
    sh:property [
        a sh:PropertyShape ;
        sh:maxCount 1 ;
        sh:path dcterms:provenance ;
        sh:message "You _MUST NOT_ use dcterms:provenance predicate more than once on any object." ;
    ] ;
.

<Requirement-2.1.7c>
    a sh:NodeShape ;
    sh:targetSubjectsOf dcterms:source ;
    sh:property [
        a sh:PropertyShape ;
        sh:maxCount 1 ;
        sh:path dcterms:source ;
        sh:message "You _MUST NOT_ use dcterms:source predicate more than once on any object." ;
    ] ;
.

<Requirement-2.1.7d>
    a sh:NodeShape ;
    sh:targetSubjectsOf prov:wasDerivedFrom ;
    sh:property [
        a sh:PropertyShape ;
        sh:maxCount 1 ;
        sh:path prov:wasDerivedFrom ;
        sh:message "You _MUST NOT_ use prov:wasDerivedFrom predicate more than once on any object." ;
    ] ;
.

<Requirement-2.1.7e>
    a sh:NodeShape ;
    sh:targetSubjectsOf dcterms:source ;
    sh:property [
        a sh:PropertyShape ;
        sh:path dcterms:source ;
        sh:datatype xsd:anyURI ;
        sh:message "Whenever dcterms:source is used, it must be a datatype predicate indicating an object of type xsd:anyURI" ;
    ] ;
.

<Requirement-2.1.7f>
    a sh:NodeShape ;
    sh:targetSubjectsOf dcterms:provenance ;
    sh:property [
        a sh:PropertyShape ;
        sh:path dcterms:provenance ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
        sh:message "Whenever dcterms:provenance is used, it must be a datatype predicate indicating an object of type xsd:string or rdf:LangString" ;
    ] ;
.

<Requirement-2.1.7g>
    a sh:NodeShape ;
    sh:targetSubjectsOf prov:wasDerivedFrom ;
    sh:property [
        a sh:PropertyShape ;
        sh:path prov:wasDerivedFrom ;
        sh:nodeKind sh:IRI ;
        sh:message "Whenever prov:wasDerivedFrom is used, it must be an object predicate indicating an IRI" ;
    ] ;
.


# Requirement-2.1.8 so far un-implemented in SHACL

<Requirement-2.1.9>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
    sh:property [
        sh:path skos:hasTopConcept ;
        sh:minCount 1 ;
        sh:nodeKind sh:IRI ;
    ] ;
    sh:message "Requirement 2.1.9 Each vocabulary's skos:ConceptScheme _MUST_ link to at least one skos:Concept within the vocabulary as with the predicate skos:hasTopConcept" ;
.

<Requirement-2.1.10>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
    sh:property [
        sh:path prov:qualifiedDerivation ;
        sh:nodeKind sh:BlankNodeOrIRI ;
    ] ;
    sh:message "Requirement 2.1.10 Each vocabulary's skos:ConceptScheme _MAY_ indicate a qualified derivation from another vocabulary" ;
.

<Requirement-2.1.10b>
	a sh:NodeShape ;
	sh:targetObjectsOf prov:qualifiedDerivation ;
    sh:property [
        sh:path prov:entity ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:message "Requirement 2.1.10b IF a skos:ConceptScheme indicates that it is derived from another object via use of the prov:qualifiedDerivation predicate, it must then indicate a prov:Entity for that derivation by use of the predicate prov:entity" ;
.

<Requirement-2.1.10c>
	a sh:NodeShape ;
	sh:targetObjectsOf prov:qualifiedDerivation ;
    sh:property [
        sh:path dcat:hadRole ;
        sh:nodeKind sh:IRI ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
    ] ;
    sh:message "Requirement 2.1.10c IF a skos:ConceptScheme indicates that it is derived from another object via use of the prov:qualifiedDerivation predicate, it must then indicate a role for the derivation by use of the predicate dcat:hadRole" ;
.

<Requirement-2.1.11>
	a sh:NodeShape ;
	sh:targetClass skos:ConceptScheme ;
    sh:property [
        sh:path reg:status ;
        sh:nodeKind sh:IRI ;
    ] ;
    sh:message "Requirement 2.1.11 Each vocabulary's skos:ConceptScheme _MAY_ indicate a status with respect to its existence in a register and, if it does it MUST do so by referencing an IRI for a skos:Concept with the reg:status predicate" ;
.

#
#   Collections
#
<Requirement-2.2.1a>
	a sh:NodeShape ;
	sh:targetClass skos:Collection ;
    sh:message "Requirement 2.2.1 Each skos:Collection instance _MUST_ have one and only one title indicated using the skos:prefLabel predicate that must be a text literal value" ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:minCount 1 ;
        sh:uniqueLang true ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.2.1b>
	a sh:NodeShape ;
	sh:targetClass skos:Collection ;
    sh:message "Requirement 2.2.1 Each skos:Collection instance _MUST_ have one and only one definition indicated using the skos:definition predicate that must be a text literal value" ;
    sh:property [
        sh:path skos:definition ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.2.2>
    a sh:NodeShape ;
    sh:message "Requirement 2.1.7 Provenance for a Collection _SHOULD_ be indicated by at least one of the following properties: dcterms:provenance, dcterms:source or prov:wasDerivedFrom." ;
    sh:or (
        [
            sh:minCount 1 ;
            sh:path prov:wasDerivedFrom ;
            sh:message "This is a message about prov:wasDerivedFrom" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:source ;
            sh:message "This is a message about dcterms:source" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:provenance ;
            sh:message "This is a message about dcterms:provenance" ;
        ]
    ) ;
    sh:targetClass skos:Collection ;
    sh:severity sh:Warning ;
.

#
#   Concept
#
<Requirement-2.3.1a>
	a sh:NodeShape ;
	sh:targetClass skos:Concept ;
    sh:message "Requirement 2.3.1 Each skos:Concept instance _MUST_ have one and only one title indicated using the `skos:prefLabel` predicate that must be a text literal value" ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:minCount 1 ;
        sh:uniqueLang true ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.3.1b>
	a sh:NodeShape ;
	sh:targetClass skos:Concept ;
    sh:message "Requirement 2.3.1 Each skos:Concept instance _MUST_ have one and only one definition indicated using the `skos:definition` predicate that must be a text literal value" ;
    sh:property [
        sh:path skos:definition ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:or ( [ sh:datatype xsd:string ] [ sh:datatype rdf:langString ] ) ;
    ]
.

<Requirement-2.3.2>
	a sh:NodeShape ;
	sh:targetClass skos:Concept ;
    sh:message "Requirement 2.3.2 Each skos:Concept in a vocabulary _MAY_ indicate the vocabulary that defines it by use of the `rdfs:isDefinedBy` predicate indicating a `skos:ConceptScheme` instance" ;
    sh:property [
        sh:path rdfs:isDefinedBy ;
        sh:minCount 0 ;
        sh:maxCount 1 ;
        sh:nodeKind sh:IRI ;
    ]
.

<Requirement-2.3.3>
	a sh:NodeShape ;
	sh:targetClass skos:Concept ;
        sh:or (
            [
                sh:property [
                sh:path skos:inScheme ;
                sh:minCount 1 ;
                sh:class skos:ConceptScheme ;
            ] ;
        ]
        [
            sh:property [
                sh:path skos:topConceptOf ;
                sh:minCount 1 ;
                sh:class skos:ConceptScheme ;
            ] ;
        ]
    ) ;
    sh:message "Requirement 2.3.3 Each skos:Concept in a vocabulary _MUST_ indicate that it appears within that vocabulary's hierarchy of terms by use of either or both `skos:inScheme` and `skos:topConceptOf` properties" ;
.

<Requirement-2.3.4>
    a sh:NodeShape ;
    sh:message "Requirement 2.1.7 Provenance for a Concept _SHOULD_ be indicated by at least one of the following properties: dcterms:provenance, dcterms:source or prov:wasDerivedFrom." ;
    sh:or (
        [
            sh:minCount 1 ;
            sh:path prov:wasDerivedFrom ;
            sh:message "This is a message about prov:wasDerivedFrom" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:source ;
            sh:message "This is a message about dcterms:source" ;
        ]
        [
            sh:minCount 1 ;
            sh:path dcterms:provenance ;
            sh:message "This is a message about dcterms:provenance" ;
        ]
    ) ;
    sh:targetClass skos:Concept ;
    sh:severity sh:Warning ;
.

#
#   Agent
#
# Requirement 2.4.1 is tested by the shape for Requirement 2.1.6a & 2.1.6b

<Requirement-2.4.1>
	a sh:NodeShape ;
	sh:targetClass sdo:Organization , sdo:Person ;
        sh:property [
            sh:path sdo:name ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:datatype xsd:string ;
            sh:message "Requirement 2.4.2 Each agent _MUST_ indicate at least one name predicate with the `sdo:name` predicate that must be a text literal value"
        ] ;
.

<Requirement-2.4.3a>
	a sh:NodeShape ;
	sh:targetClass sdo:Organization ;
        sh:property [
            sh:path sdo:url ;
            sh:minCount 1 ;
            sh:datatype xsd:anyURI ;
        ] ;
        sh:message "Requirement 2.4.3 Each agent _MUST_ indicate either a `sdo:url` (for organizations) or a `sdo:email` (for people) predicate with a URL or email value"
.

<Requirement-2.4.3b>
	a sh:NodeShape ;
	sh:targetClass sdo:Person ;
        sh:property [
            sh:path sdo:email ;
            sh:minCount 1 ;
            sh:datatype xsd:anyURI ;
        ] ;
        sh:message "Requirement 2.4.3 Each agent _MUST_ indicate either a sdo:url (for organizations) or a sdo:email (for people) predicate with a URL or email value"
.
"""

valid = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://linked.data.gov.au/def/placenametype/AF>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Landing Area" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Landing Area" ;
.

<https://linked.data.gov.au/def/placenametype/ANCH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Anchorage" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Anchorage" ;
.

<https://linked.data.gov.au/def/placenametype/BANK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Bank - Marine" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Bank - Marine" ;
.

<https://linked.data.gov.au/def/placenametype/BAR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Bar" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Bar" ;
.

<https://linked.data.gov.au/def/placenametype/BAY>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Bay" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Bay" ;
.

<https://linked.data.gov.au/def/placenametype/BCH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Beach" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Beach" ;
.

<https://linked.data.gov.au/def/placenametype/BORE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Bore" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Bore" ;
.

<https://linked.data.gov.au/def/placenametype/BRKW>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Breakwater" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Breakwater" ;
.

<https://linked.data.gov.au/def/placenametype/CAPE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Cape" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Cape" ;
.

<https://linked.data.gov.au/def/placenametype/CAVE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Cave" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Cave" ;
.

<https://linked.data.gov.au/def/placenametype/CAY>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Cay" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Cay" ;
.

<https://linked.data.gov.au/def/placenametype/CHAN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Channel" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Channel" ;
.

<https://linked.data.gov.au/def/placenametype/CLIF>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Cliff" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Cliff" ;
.

<https://linked.data.gov.au/def/placenametype/CNR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Corner" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Corner" ;
.

<https://linked.data.gov.au/def/placenametype/CNTY>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "County" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "County" ;
.

<https://linked.data.gov.au/def/placenametype/COVE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Cove, Inlet" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Cove, Inlet" ;
.

<https://linked.data.gov.au/def/placenametype/CRAT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Crater" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Crater" ;
.

<https://linked.data.gov.au/def/placenametype/DAM>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Dam wall" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Dam wall" ;
.

<https://linked.data.gov.au/def/placenametype/DEEP>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Marine" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Marine" ;
.

<https://linked.data.gov.au/def/placenametype/DI>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "District" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "District" ;
.

<https://linked.data.gov.au/def/placenametype/DRN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Drain" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Drain" ;
.

<https://linked.data.gov.au/def/placenametype/DSRT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Desert" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Desert" ;
.

<https://linked.data.gov.au/def/placenametype/DUNE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Dune" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Dune" ;
.

<https://linked.data.gov.au/def/placenametype/ENTR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Entrance" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Entrance" ;
.

<https://linked.data.gov.au/def/placenametype/FORD>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Ford" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Ford" ;
.

<https://linked.data.gov.au/def/placenametype/FRST>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "State Forest" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "State Forest" ;
.

<https://linked.data.gov.au/def/placenametype/GATE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Gate" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Gate" ;
.

<https://linked.data.gov.au/def/placenametype/GORG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Gorge" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Gorge" ;
.

<https://linked.data.gov.au/def/placenametype/GULF>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Gulf" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Gulf" ;
.

<https://linked.data.gov.au/def/placenametype/HBR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Harbour" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Harbour" ;
.

<https://linked.data.gov.au/def/placenametype/HILL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Hill" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Hill" ;
.

<https://linked.data.gov.au/def/placenametype/HMSD>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Homestead" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Homestead" ;
.

<https://linked.data.gov.au/def/placenametype/INLT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Inlet" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Inlet" ;
.

<https://linked.data.gov.au/def/placenametype/IS>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Island" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Island" ;
.

<https://linked.data.gov.au/def/placenametype/ISG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Island group" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Island group" ;
.

<https://linked.data.gov.au/def/placenametype/ISTH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Isthmus" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Isthmus" ;
.

<https://linked.data.gov.au/def/placenametype/ISX>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Island - feature appears absent" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Island - feature appears absent" ;
.

<https://linked.data.gov.au/def/placenametype/JUNC>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Junction" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Junction" ;
.

<https://linked.data.gov.au/def/placenametype/LAGN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Lagoon" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Lagoon" ;
.

<https://linked.data.gov.au/def/placenametype/LAKE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Lake" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Lake" ;
.

<https://linked.data.gov.au/def/placenametype/LNDG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Landing Place" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Landing Place" ;
.

<https://linked.data.gov.au/def/placenametype/LOCB>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Locality Bounded" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Locality Bounded" ;
.

<https://linked.data.gov.au/def/placenametype/LOCU>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Locality Unbounded" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Locality Unbounded" ;
.

<https://linked.data.gov.au/def/placenametype/LOOK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Lookout" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Lookout" ;
.

<https://linked.data.gov.au/def/placenametype/MT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Mountain" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Mountain" ;
.

<https://linked.data.gov.au/def/placenametype/MTS>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Range" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Range" ;
.

<https://linked.data.gov.au/def/placenametype/MTX>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Mountain - Feature no longer exists" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Mountain - Feature no longer exists" ;
.

<https://linked.data.gov.au/def/placenametype/NBHD>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Neighbourhood" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Neighbourhood" ;
.

<https://linked.data.gov.au/def/placenametype/OSTN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Outstation" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Outstation" ;
.

<https://linked.data.gov.au/def/placenametype/PAN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Pan" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Pan" ;
.

<https://linked.data.gov.au/def/placenametype/PAR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Park" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Park" ;
.

<https://linked.data.gov.au/def/placenametype/PARK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "National Park,Resources Reserve,Conservation Park" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "National Park,Resources Reserve,Conservation Park" ;
.

<https://linked.data.gov.au/def/placenametype/PASG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Passage" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Passage" ;
.

<https://linked.data.gov.au/def/placenametype/PASS>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Pass" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Pass" ;
.

<https://linked.data.gov.au/def/placenametype/PAST>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Pastoral district" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Pastoral district" ;
.

<https://linked.data.gov.au/def/placenametype/PEAK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Peak" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Peak" ;
.

<https://linked.data.gov.au/def/placenametype/PEAX>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Peak - Feature no longer exists" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Peak - Feature no longer exists" ;
.

<https://linked.data.gov.au/def/placenametype/PEN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Peninsula" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Peninsula" ;
.

<https://linked.data.gov.au/def/placenametype/PL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Plateau" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Plateau" ;
.

<https://linked.data.gov.au/def/placenametype/PLAT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Plateau - Marine" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Plateau - Marine" ;
.

<https://linked.data.gov.au/def/placenametype/PLN>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Plain" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Plain" ;
.

<https://linked.data.gov.au/def/placenametype/PLNA>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Place Name" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Place Name" ;
.

<https://linked.data.gov.au/def/placenametype/POCK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Pocket" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Pocket" ;
.

<https://linked.data.gov.au/def/placenametype/POPL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Population centre" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Population centre" ;
.

<https://linked.data.gov.au/def/placenametype/POPX>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Population centre - feature appears absent" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Population centre - feature appears absent" ;
.

<https://linked.data.gov.au/def/placenametype/PORT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Port" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Port" ;
.

<https://linked.data.gov.au/def/placenametype/PRSH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Parish" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Parish" ;
.

<https://linked.data.gov.au/def/placenametype/PT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Point" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Point" ;
.

<https://linked.data.gov.au/def/placenametype/RAP>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Rapids" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Rapids" ;
.

<https://linked.data.gov.au/def/placenametype/RCH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Reach" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Reach" ;
.

<https://linked.data.gov.au/def/placenametype/RDGE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Ridge" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Ridge" ;
.

<https://linked.data.gov.au/def/placenametype/REEF>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Reef" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Reef" ;
.

<https://linked.data.gov.au/def/placenametype/RES>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Reservoir" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Reservoir" ;
.

<https://linked.data.gov.au/def/placenametype/RESV>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Reserve" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Reserve" ;
.

<https://linked.data.gov.au/def/placenametype/RH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Rockhole" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Rockhole" ;
.

<https://linked.data.gov.au/def/placenametype/RIDG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Ridge - Marine" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Ridge - Marine" ;
.

<https://linked.data.gov.au/def/placenametype/ROCK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Rock" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Rock" ;
.

<https://linked.data.gov.au/def/placenametype/RSID>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Siding" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Siding" ;
.

<https://linked.data.gov.au/def/placenametype/RSTA>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Rail Station" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Rail Station" ;
.

<https://linked.data.gov.au/def/placenametype/RSTX>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Rail Station - Feature no longer exists" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Rail Station - Feature no longer exists" ;
.

<https://linked.data.gov.au/def/placenametype/SCH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "School" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "School" ;
.

<https://linked.data.gov.au/def/placenametype/SCRB>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Scrub" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Scrub" ;
.

<https://linked.data.gov.au/def/placenametype/SHLF>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Shelf - Marine" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Shelf - Marine" ;
.

<https://linked.data.gov.au/def/placenametype/SHOL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Shoal" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Shoal" ;
.

<https://linked.data.gov.au/def/placenametype/SITE>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Historic Site" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Historic Site" ;
.

<https://linked.data.gov.au/def/placenametype/SND>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Sound" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Sound" ;
.

<https://linked.data.gov.au/def/placenametype/SOAK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Soak" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Soak" ;
.

<https://linked.data.gov.au/def/placenametype/SPIT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Spit" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Spit" ;
.

<https://linked.data.gov.au/def/placenametype/SPRG>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Spring" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Spring" ;
.

<https://linked.data.gov.au/def/placenametype/SPUR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Spur" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Spur" ;
.

<https://linked.data.gov.au/def/placenametype/STAT>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "State" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "State" ;
.

<https://linked.data.gov.au/def/placenametype/STR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Strait" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Strait" ;
.

<https://linked.data.gov.au/def/placenametype/STRM>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Watercourse" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Watercourse" ;
.

<https://linked.data.gov.au/def/placenametype/SUB>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Suburb" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Suburb" ;
.

<https://linked.data.gov.au/def/placenametype/SWP>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Wetland" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Wetland" ;
.

<https://linked.data.gov.au/def/placenametype/TANK>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Water tank" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Water tank" ;
.

<https://linked.data.gov.au/def/placenametype/VAL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Valley" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Valley" ;
.

<https://linked.data.gov.au/def/placenametype/WEIR>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Weir" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Weir" ;
.

<https://linked.data.gov.au/def/placenametype/WELL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Well" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Well" ;
.

<https://linked.data.gov.au/def/placenametype/WOOD>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Forest" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Forest" ;
.

<https://linked.data.gov.au/def/placenametype/WRFL>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Waterfall" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Waterfall" ;
.

<https://linked.data.gov.au/def/placenametype/WTRH>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Waterhole" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Waterhole" ;
.

<https://linked.data.gov.au/def/placenametype/YD>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Stockyard" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "Stockyard" ;
.

<https://linked.data.gov.au/def/placenametype/Z>
    a skos:Concept ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "ignore - test record" ;
    skos:inScheme <https://linked.data.gov.au/def/placenametype> ;
    skos:prefLabel "ignore - test record" ;
.

<https://linked.data.gov.au/def/placenametype>
    a skos:ConceptScheme ;
    dcterms:created "2023-03-15T12:49:40.837553"^^xsd:date ;
    dcterms:modified "2023-03-15T12:49:40.837584"^^xsd:date ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:definition "Place name types." ;
    skos:hasTopConcept
        <https://linked.data.gov.au/def/placenametype/AF> ,
        <https://linked.data.gov.au/def/placenametype/ANCH> ,
        <https://linked.data.gov.au/def/placenametype/BANK> ,
        <https://linked.data.gov.au/def/placenametype/BAR> ,
        <https://linked.data.gov.au/def/placenametype/BAY> ,
        <https://linked.data.gov.au/def/placenametype/BCH> ,
        <https://linked.data.gov.au/def/placenametype/BORE> ,
        <https://linked.data.gov.au/def/placenametype/BRKW> ,
        <https://linked.data.gov.au/def/placenametype/CAPE> ,
        <https://linked.data.gov.au/def/placenametype/CAVE> ,
        <https://linked.data.gov.au/def/placenametype/CAY> ,
        <https://linked.data.gov.au/def/placenametype/CHAN> ,
        <https://linked.data.gov.au/def/placenametype/CLIF> ,
        <https://linked.data.gov.au/def/placenametype/CNR> ,
        <https://linked.data.gov.au/def/placenametype/CNTY> ,
        <https://linked.data.gov.au/def/placenametype/COVE> ,
        <https://linked.data.gov.au/def/placenametype/CRAT> ,
        <https://linked.data.gov.au/def/placenametype/DAM> ,
        <https://linked.data.gov.au/def/placenametype/DEEP> ,
        <https://linked.data.gov.au/def/placenametype/DI> ,
        <https://linked.data.gov.au/def/placenametype/DRN> ,
        <https://linked.data.gov.au/def/placenametype/DSRT> ,
        <https://linked.data.gov.au/def/placenametype/DUNE> ,
        <https://linked.data.gov.au/def/placenametype/ENTR> ,
        <https://linked.data.gov.au/def/placenametype/FORD> ,
        <https://linked.data.gov.au/def/placenametype/FRST> ,
        <https://linked.data.gov.au/def/placenametype/GATE> ,
        <https://linked.data.gov.au/def/placenametype/GORG> ,
        <https://linked.data.gov.au/def/placenametype/GULF> ,
        <https://linked.data.gov.au/def/placenametype/HBR> ,
        <https://linked.data.gov.au/def/placenametype/HILL> ,
        <https://linked.data.gov.au/def/placenametype/HMSD> ,
        <https://linked.data.gov.au/def/placenametype/INLT> ,
        <https://linked.data.gov.au/def/placenametype/IS> ,
        <https://linked.data.gov.au/def/placenametype/ISG> ,
        <https://linked.data.gov.au/def/placenametype/ISTH> ,
        <https://linked.data.gov.au/def/placenametype/ISX> ,
        <https://linked.data.gov.au/def/placenametype/JUNC> ,
        <https://linked.data.gov.au/def/placenametype/LAGN> ,
        <https://linked.data.gov.au/def/placenametype/LAKE> ,
        <https://linked.data.gov.au/def/placenametype/LNDG> ,
        <https://linked.data.gov.au/def/placenametype/LOCB> ,
        <https://linked.data.gov.au/def/placenametype/LOCU> ,
        <https://linked.data.gov.au/def/placenametype/LOOK> ,
        <https://linked.data.gov.au/def/placenametype/MT> ,
        <https://linked.data.gov.au/def/placenametype/MTS> ,
        <https://linked.data.gov.au/def/placenametype/MTX> ,
        <https://linked.data.gov.au/def/placenametype/NBHD> ,
        <https://linked.data.gov.au/def/placenametype/OSTN> ,
        <https://linked.data.gov.au/def/placenametype/PAN> ,
        <https://linked.data.gov.au/def/placenametype/PAR> ,
        <https://linked.data.gov.au/def/placenametype/PARK> ,
        <https://linked.data.gov.au/def/placenametype/PASG> ,
        <https://linked.data.gov.au/def/placenametype/PASS> ,
        <https://linked.data.gov.au/def/placenametype/PAST> ,
        <https://linked.data.gov.au/def/placenametype/PEAK> ,
        <https://linked.data.gov.au/def/placenametype/PEAX> ,
        <https://linked.data.gov.au/def/placenametype/PEN> ,
        <https://linked.data.gov.au/def/placenametype/PL> ,
        <https://linked.data.gov.au/def/placenametype/PLAT> ,
        <https://linked.data.gov.au/def/placenametype/PLN> ,
        <https://linked.data.gov.au/def/placenametype/PLNA> ,
        <https://linked.data.gov.au/def/placenametype/POCK> ,
        <https://linked.data.gov.au/def/placenametype/POPL> ,
        <https://linked.data.gov.au/def/placenametype/POPX> ,
        <https://linked.data.gov.au/def/placenametype/PORT> ,
        <https://linked.data.gov.au/def/placenametype/PRSH> ,
        <https://linked.data.gov.au/def/placenametype/PT> ,
        <https://linked.data.gov.au/def/placenametype/RAP> ,
        <https://linked.data.gov.au/def/placenametype/RCH> ,
        <https://linked.data.gov.au/def/placenametype/RDGE> ,
        <https://linked.data.gov.au/def/placenametype/REEF> ,
        <https://linked.data.gov.au/def/placenametype/RES> ,
        <https://linked.data.gov.au/def/placenametype/RESV> ,
        <https://linked.data.gov.au/def/placenametype/RH> ,
        <https://linked.data.gov.au/def/placenametype/RIDG> ,
        <https://linked.data.gov.au/def/placenametype/ROCK> ,
        <https://linked.data.gov.au/def/placenametype/RSID> ,
        <https://linked.data.gov.au/def/placenametype/RSTA> ,
        <https://linked.data.gov.au/def/placenametype/RSTX> ,
        <https://linked.data.gov.au/def/placenametype/SCH> ,
        <https://linked.data.gov.au/def/placenametype/SCRB> ,
        <https://linked.data.gov.au/def/placenametype/SHLF> ,
        <https://linked.data.gov.au/def/placenametype/SHOL> ,
        <https://linked.data.gov.au/def/placenametype/SITE> ,
        <https://linked.data.gov.au/def/placenametype/SND> ,
        <https://linked.data.gov.au/def/placenametype/SOAK> ,
        <https://linked.data.gov.au/def/placenametype/SPIT> ,
        <https://linked.data.gov.au/def/placenametype/SPRG> ,
        <https://linked.data.gov.au/def/placenametype/SPUR> ,
        <https://linked.data.gov.au/def/placenametype/STAT> ,
        <https://linked.data.gov.au/def/placenametype/STR> ,
        <https://linked.data.gov.au/def/placenametype/STRM> ,
        <https://linked.data.gov.au/def/placenametype/SUB> ,
        <https://linked.data.gov.au/def/placenametype/SWP> ,
        <https://linked.data.gov.au/def/placenametype/TANK> ,
        <https://linked.data.gov.au/def/placenametype/VAL> ,
        <https://linked.data.gov.au/def/placenametype/WEIR> ,
        <https://linked.data.gov.au/def/placenametype/WELL> ,
        <https://linked.data.gov.au/def/placenametype/WOOD> ,
        <https://linked.data.gov.au/def/placenametype/WRFL> ,
        <https://linked.data.gov.au/def/placenametype/WTRH> ,
        <https://linked.data.gov.au/def/placenametype/YD> ,
        <https://linked.data.gov.au/def/placenametype/Z> ;
    skos:prefLabel "Place Name Types" ;
.
"""

invalid = """
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

<https://linked.data.gov.au/def/placenametype>
    a skos:ConceptScheme ;
    dcterms:provenance "Generated by Spatial Information, Queensland Government on a dump of PNDB data." ;
    skos:prefLabel "Place Name Types" ;
.
"""
