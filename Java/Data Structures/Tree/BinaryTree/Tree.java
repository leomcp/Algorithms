
package BinaryTree;

import java.util.Stack;

public class Tree {
    private Node root;
    //--------------------------------------------------------------------------
    public Tree(){
        root=null;
    }
    //--------------------------------------------------------------------------
    public Node find(int key){
        Node current =root;
        while(current.iData!=key){
            if(key<current.iData)
                current=current.leftChild;
            else
                current=current.rightChild;
            if(current==null)
                return null;
        }
        return current;
    }
    //--------------------------------------------------------------------------
    public void insert(int id,double dd){
        Node newNode =new Node();
        newNode.iData=id;
        newNode.dData=dd;
        if(root==null)
            root=newNode;
        else{
            Node current=root;
            Node parent;
            while(true){
                parent=current;
                if(id<current.iData){
                    current=current.leftChild;
                    if(current==null){
                        parent.leftChild=newNode;
                        return;
                    }
                }
                else{
                    current=current.rightChild;
                    if(current==null){
                        parent.rightChild=newNode;
                        return;
                    }        
                }
            }
        }
    }
    //--------------------------------------------------------------------------
    public boolean delete(int key){
        Node current=root;
        Node parent=root;
        boolean isLeftChild=true;
        
        while(current.iData!=key){
            parent=current;
            if(key<current.iData){
                isLeftChild=true;
                current=current.leftChild;
            }
            else{
                isLeftChild=false;
                current=current.rightChild;
            }
            if(current==null)
                return false;
        }
            if(current.leftChild==null && current.rightChild==null){
                if(current==root)
                    root=null;
                else if(isLeftChild)
                    parent.leftChild=null;
                else
                    parent.rightChild=null;
            }
            
            else if(current.rightChild==null)
                if(current==root)
                    root=current.leftChild;
                else if(isLeftChild)
                    parent.leftChild=current.leftChild;
            
                else if(current.leftChild==null)
                    if(current==root)
                        root=current.rightChild;
                    else if(isLeftChild)
                        parent.leftChild=current.rightChild;
                    else
                        parent.rightChild=current.rightChild;
            
            else{
                 Node successor=getSuccessor(current);   
                 if(current==root)
                     root=successor;
                 else if(isLeftChild)
                     parent.leftChild=successor;
                 else
                     parent.rightChild=successor;
                 
                 successor.leftChild=current.leftChild;
            }
        
        return true;
    }
    //--------------------------------------------------------------------------
    private Node getSuccessor(Node delNode){
        Node successorParent =delNode;
        Node successor=delNode;
        Node current=delNode.rightChild;
        while(current!=null){
            successorParent=successor;
            successor=current;
            current=current.leftChild;
        }
        if(successor!=delNode.rightChild){
            successorParent.leftChild=successor.rightChild;
            successor.rightChild=delNode.rightChild;
        }
        return successor;
    }
    //--------------------------------------------------------------------------
    public void traverse(int traverseType){
        switch(traverseType){
            case 1 : System.out.print("\n Preorder Traversal :");
                     preOrder(root);
                     break;
            case 2 : System.out.print("\n Inorder Traversal :");
                     inOrder(root);
                     break; 
            case 3 : System.out.print("\n Postorder Traversal :");
                     postOrder(root);
                     break;          
        }
        System.out.println();
    }
    //--------------------------------------------------------------------------
    private void preOrder(Node localroot){
        if(localroot!=null){
            System.out.print(localroot.iData+" ");
            preOrder(localroot.leftChild);
            preOrder(localroot.rightChild);
        }
    }
    //--------------------------------------------------------------------------
    private void inOrder(Node localroot){
        if(localroot!=null){
        inOrder(localroot.leftChild);
        System.out.print(localroot.iData+" ");
        inOrder(localroot.rightChild);
        }
    }
    //--------------------------------------------------------------------------
    private void postOrder(Node localroot){
        if(localroot!=null){
            postOrder( localroot.leftChild);
            postOrder(localroot.rightChild);
            System.out.print(localroot.iData+" ");
        }
    }
    //--------------------------------------------------------------------------
    public void displayTree(){
        Stack globalStack=new Stack();
        globalStack.push(root);
        int nBlanks=32;
        boolean isRowEmpty=false;
        System.out.println(
                "..............................................................."
        );
        while(isRowEmpty==false){
            Stack localStack=new Stack();
            isRowEmpty=true;
            
            for(int j=0;j<nBlanks;j++)
                System.out.print(' ');
            
            while(globalStack.isEmpty()==false){
                Node temp=(Node) globalStack.pop();
                if(temp!=null){
                    System.out.print(temp.iData);
                    localStack.push(temp.leftChild);
                    localStack.push(temp.rightChild);
                    
                    if(temp.leftChild!=null || temp.rightChild!=null)
                        isRowEmpty=false;
                }
                else{
                    System.out.print("--");
                    localStack.push(null);
                    localStack.push(null);
                }
                for(int j=0;j<nBlanks*2-2;j++)
                    System.out.print(' ');
            }
            System.out.println();
            nBlanks/=2;
            while(localStack.isEmpty()==false)
                globalStack.push(localStack.pop());
        }
        System.out.println(
                "..............................................................."
        );
    }
    //--------------------------------------------------------------------------
}
