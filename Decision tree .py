import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter

# Manually extracted dataset from the image
data = [
    [1, 0, 0, 1, "Some", 3, 0, 1, "French", "0-10", 1],
    [1, 0, 0, 1, "Full", 1, 0, 0, "Thai", "30-60", 0],
    [0, 1, 0, 0, "Some", 1, 0, 1, "Burger", "0-10", 1],
    [1, 0, 0, 1, "Full", 1, 1, 0, "Thai", "10-30", 1],
    [1, 0, 0, 0, "Full", 3, 0, 1, "French", ">60", 0],
    [0, 1, 0, 1, "Some", 2, 0, 1, "Italian", "0-10", 1],
    [0, 1, 0, 0, "None", 1, 1, 0, "Burger", "0-10", 0],
    [0, 0, 1, 1, "Some", 2, 1, 1, "Thai", "0-10", 1],
    [0, 0, 1, 0, "Full", 1, 1, 1, "Burger", ">60", 0],
    [1, 0, 1, 1, "Full", 3, 0, 0, "Italian", "10-30", 0],
    [0, 0, 0, 0, "None", 1, 0, 0, "Thai", "0-10", 0],
    [1, 1, 1, 1, "Full", 1, 0, 0, "Burger", "30-60", 1]
]

# Convert categorical columns to numerical
est_map = {'0-10': 0, '10-30': 1, '30-60': 2, '>60': 3}
type_map = {'French': 0, 'Thai': 1, 'Burger': 2, 'Italian': 3}
pat_map = {'None': 0, 'Some': 1, 'Full': 2}

def preprocess(data):
    for row in data:
        row[4] = pat_map[row[4]]  # Convert "None", "Some", "Full" to numbers
        row[9] = est_map[row[9]]  # Convert estimated wait time
        row[8] = type_map[row[8]] # Convert restaurant type
    return np.array(data, dtype=int)  # Convert to NumPy array

data = preprocess(data)
X, y = data[:, :-1], data[:, -1]

# Implementing a simple Decision Tree Classifier from scratch
class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value

class DecisionTree:
    def __init__(self, depth=3):
        self.depth = depth
        self.root = None

    def fit(self, X, y):
        self.root = self._grow_tree(X, y, depth=0)

    def _grow_tree(self, X, y, depth):
        if depth >= self.depth or len(set(y)) == 1:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        best_feature, best_threshold = self._best_split(X, y)
        if best_feature is None:
            return Node(value=Counter(y).most_common(1)[0][0])
        
        left_idx = X[:, best_feature] <= best_threshold
        right_idx = X[:, best_feature] > best_threshold
        left = self._grow_tree(X[left_idx], y[left_idx], depth + 1)
        right = self._grow_tree(X[right_idx], y[right_idx], depth + 1)
        
        return Node(best_feature, best_threshold, left, right)

    def _best_split(self, X, y):
        best_gain, best_feature, best_threshold = 0, None, None
        for feature in range(X.shape[1]):
            thresholds = np.unique(X[:, feature])
            for threshold in thresholds:
                left_idx = y[X[:, feature] <= threshold]
                right_idx = y[X[:, feature] > threshold]
                gain = self._information_gain(y, left_idx, right_idx)
                if gain > best_gain:
                    best_gain, best_feature, best_threshold = gain, feature, threshold
        return best_feature, best_threshold

    def _information_gain(self, y, left, right):
        p = len(left) / (len(left) + len(right))
        return self._entropy(y) - p * self._entropy(left) - (1 - p) * self._entropy(right)

    def _entropy(self, y):
        counts = np.bincount(y)
        probs = counts / len(y)
        return -np.sum([p * np.log2(p) for p in probs if p > 0])

    def predict(self, X):
        return np.array([self._predict_row(row, self.root) for row in X])
    
    def _predict_row(self, row, node):
        if node.value is not None:
            return node.value
        if row[node.feature] <= node.threshold:
            return self._predict_row(row, node.left)
        return self._predict_row(row, node.right)

# Train and test the decision tree
dt = DecisionTree(depth=3)
dt.fit(X, y)

# --- GRAPH VISUALIZATION --- #
def draw_tree(node, graph, pos=None, level=0, x=0, y=0, layer_width=2):
    if pos is None:
        pos = {}
    
    node_id = id(node)
    if node.value is not None:
        label = f"Leaf: {node.value}"
    else:
        label = f"X[{node.feature}] ≤ {node.threshold}"

    pos[node_id] = (x, y)
    graph.add_node(node_id, label=label)
    
    if node.left:
        left_id = id(node.left)
        graph.add_edge(node_id, left_id)
        draw_tree(node.left, graph, pos, level + 1, x - layer_width / (level + 1), y - 1, layer_width)

    if node.right:
        right_id = id(node.right)
        graph.add_edge(node_id, right_id)
        draw_tree(node.right, graph, pos, level + 1, x + layer_width / (level + 1), y - 1, layer_width)

    return graph, pos

# Create a graph and draw the tree
graph = nx.DiGraph()
graph, pos = draw_tree(dt.root, graph)

plt.figure(figsize=(10, 6))
labels = nx.get_node_attributes(graph, 'label')
nx.draw(graph, pos, with_labels=True, labels=labels, node_size=3000, node_color="lightblue", font_size=8, edge_color="gray")
plt.title("Decision Tree Visualization")
plt.show()
