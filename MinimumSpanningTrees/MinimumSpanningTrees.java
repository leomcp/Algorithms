/*
   -----------MINIMUM SPANNING TREES--------------

The algorithms is used to minimise the connections of the given Graph, such that the 
graph contains minimum number of edges necessary to connect the vertices.The algorithm
for creating the minimum spanning tree is almost identical to that used for searching.
It can be based on both BFS or DFS.

 */
package MinimumSpanningTrees;

public class MinimumSpanningTrees {

    public static void main(String[] args) {
        // TODO code application logic here
        Graph theGraph=new Graph();
        theGraph.addVertex('A');
        theGraph.addVertex('B');
        theGraph.addVertex('C');
        theGraph.addVertex('D');
        theGraph.addVertex('E');
        
        theGraph.addEdge(0, 1);
        theGraph.addEdge(0, 2);
        theGraph.addEdge(0, 3);
        theGraph.addEdge(0, 4);
        theGraph.addEdge(1, 2);
        theGraph.addEdge(1, 3);
        theGraph.addEdge(1, 4);
        theGraph.addEdge(2, 3);
        theGraph.addEdge(2, 4);
        theGraph.addEdge(3, 4);
        
        System.out.print("Minimum spanning tree :");
        theGraph.mst();
        System.out.println();
    }
}


/*
OUTPUT : Minimum spanning tree :AB BC CD DE 
*/