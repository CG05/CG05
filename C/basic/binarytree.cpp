#include <iostream>
#define NULL 0

using namespace std;

template <typename T>
class Tree;

template <typename T>
class TreeNode {
	friend class Tree<T>;
	private:
		T data;
		TreeNode* left;
		TreeNode* right;
	public:
		TreeNode(T data = 0, TreeNode* left = NULL, TreeNode* right = NULL){
			this->data = data;
			this->left = left;
			this->right = right;
		}
		friend ostream& operator<<(ostream& os, const TreeNode<T>& node){
			os << " [data] " << node.data << endl;
			if(node.left != NULL){
				os << "[left] " << node.left->data << endl;
			}
			if(node.right != NULL){
				os << "[right] " << node.right->data << endl;
			}
			return os;
		}
};

template <typename T>
class Tree{
	private:
		TreeNode<T>* root;
	public:
		Tree(T data = 0){
			root = new TreeNode<T>(data);
		}
	
		void buildSearchTree(){
			insertNode(new TreeNode<int>(3));
			insertNode(new TreeNode<int>(10));
			insertNode(new TreeNode<int>(14));
			insertNode(new TreeNode<int>(2));
			insertNode(new TreeNode<int>(5));
			insertNode(new TreeNode<int>(11));
			insertNode(new TreeNode<int>(16));
		}
	
		TreeNode<T>* getRoot(){
			return root;
		}
	
		void visit(TreeNode<T>* current){
			cout << current->data << " ";
		}
	
		void insertNode(TreeNode<T>* node){
			if(search(root, node->data) == NULL){
				TreeNode<T>* parent = NULL;
				TreeNode<T>* current = root;
				
				while (current != NULL){
					parent = current;
					if(node->data < parent->data){
						current = current->left;
					}else{
						current = current->right;
					}
				}
				if(node->data < parent->data){
					parent->left = node;
				}else{
					parent->right = node;
				}
				cout << "Inserted " << node->data << endl;
			}
		}
	
	void preorder(TreeNode<T>* current){
		if(current != NULL){
			visit(current);
			preorder(current->left);
			preorder(current->right);
		}
	}
	
	TreeNode<T>* search(TreeNode<T>* current, T data){
		if(current == NULL){
			return NULL;
		}
		if(data == current->data){
			return current;
		}else if(data < current->data){
			search(current->left, data);
		}else{
			search(current->right, data);
		}
	}
};

int main(){
	Tree<int> tree(8);
	tree.buildSearchTree();
	
	cout << "Preorder >> ";
	tree.preorder(tree.getRoot());
	cout << endl;
	
	int number;
	cout << "Input number to search >> ";
	cin >> number;
	
	TreeNode<int>* found = tree.search(tree.getRoot(), number);
	
	if(found != NULL){
		cout << "Found node." << endl;
		cout << *found;
	}else{
		cout << "Not found node." << endl;
	}
}
