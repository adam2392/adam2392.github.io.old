Title: Graphs and their usage in causality
Date: 2022-5-4
Category: causality
Tags: causality, machine learning
Slug: graphs-causality
Authors: Adam Li
Summary: A summary of graphs in causal inference.

# What are graphs and what do they imply?

Graphs are mathematical objects defined with a tuple `(V, E)`, where V is a set of vertices and E are a set of edges connecting said vertices. For example:

    $$G = (\{X, Y, Z\}, \{(X, Y), (Y, Z)\})$$

is a graph. Graphs as their name suggest are "graphical" representations of things that have "relationships" with other things. The graphical aspect is nice because we can easily draw the graph in question as such.

$\begin{tikzpicture}\node (v0) at (-2.20,1.52) {A};
\node (v1) at (1.40,-1.62) {D};
\node (v2) at (-0.512,-0.127) {E};
\draw [->] (v0) edge (v2);
\draw [->,<-] (v1) edge (v2);\end{tikzpicture}$

# Recommended Pipeline