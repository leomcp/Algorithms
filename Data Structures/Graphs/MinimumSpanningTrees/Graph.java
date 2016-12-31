
package MinimumSpanningTrees;

public class Graph {
    
    private final int MAX_VERTS=20;
    private Vertex vertexList[];  //list of vertices
    private int adjMat[][];       // adjacency matrix
    private int nVerts;           // current number of Vertices
    private StackX stack;
    
    //----------------------------------------------------------
    public Graph(){               //constructor
        vertexList =new Vertex[MAX_VERTS];
        adjMat=new int[MAX_VERTS][MAX_VERTS];
        nVerts=0;
        for(int j=0;j<MAX_VERTS;j++)          //set adjacency 
            for(int k=0;k<MAX_VERTS;k++)
                adjMat[j][k]=0;
        stack=new StackX();
    }
    //----------------------------------------------------------
    public void addVertex(char lab){
        vertexList[nVerts++]=new Vertex(lab);
    }
    //----------------------------------------------------------
    public void addEdge(int start,int end){
        adjMat[start][end]=1;
        adjMat[end][start]=1;
    }
    //----------------------------------------------------------
    public void displayVertex(int v){
        System.out.print(vertexList[v].label);
    }
    //----------------------------------------------------------
    public void mst(){      // Minimum Spanning Tree (Depth First)
        vertexList[0].wasVisited=true;
        stack.push(0);
        
        while(!stack.isEmpty()){ 
            int currentVertex=stack.peek();
            //get next unvisited neighbour 
            int v=getAdjUnvisitedVertex(currentVertex);
            if(v==-1)
                stack.pop();
            else{
                vertexList[v].wasVisited=true;
                stack.push(v);
                
                displayVertex(currentVertex);
                displayVertex(v);
                System.out.print(" ");
            }
        } // end of while loop
        
        //stack is empty, so we are done 
        for(int j=0;j<nVerts;j++)
            vertexList[j].wasVisited=false;
    }
    //----------------------------------------------------------
    // return an invisited vertes adjacent to v
    public int getAdjUnvisitedVertex(int v){
        for(int j=0;j<nVerts;j++)
            if(adjMat[v][j]==1 && vertexList[j].wasVisited==false)
                return j;
        return -1;         
               
    
    
    } 
}
