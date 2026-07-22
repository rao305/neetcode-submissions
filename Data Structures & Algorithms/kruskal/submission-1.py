class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        
        # We keep track of the size of each component so that when we union
        # two components, we can attach the smaller one under the larger one.
        # This helps keep the tree shallow and makes future operations faster.
        size = [1] * n

        # This function finds the root parent of a node.
        # The root tells us which connected component the node belongs to.
        def find(x):
            # If x is not its own parent, it means x is not the root.
            if parent[x] != x:
                # Path compression:
                # We recursively find the real root and directly connect x to it.
                # This makes future find operations much faster.
                parent[x] = find(parent[x])
            return parent[x]

        # This function tries to merge the components of a and b.
        # It returns True if a merge happened, and False if they were
        # already in the same component.
        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # If both nodes already have the same root, they are already connected.
            # Adding this edge would create a cycle, so we should skip it.
            if root_a == root_b:
                return False

            # Union by size:
            # Always attach the smaller component under the larger one
            # to keep the structure balanced.
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            # Make root_b point to root_a, which merges the two components.
            parent[root_b] = root_a

            # Update the size of the new merged component.
            size[root_a] += size[root_b]

            return True

        # Kruskal's algorithm starts by sorting all edges from smallest
        # weight to largest weight.
        edges.sort(key=lambda edge: edge[2])

        # This stores the total weight of the MST we are building.
        total_weight = 0

        # This counts how many edges we have successfully added to the MST.
        edges_used = 0

        # Try edges from smallest weight to largest weight.
        for u, v, w in edges:
            # Only add the edge if it connects two different components.
            if union(u, v):
                total_weight += w
                edges_used += 1

                # A spanning tree for n nodes always has exactly n - 1 edges.
                # Once we reach that, we can stop early.
                if edges_used == n - 1:
                    return total_weight

        # If we never reached n - 1 edges, the graph was not fully connected,
        # so a valid MST does not exist.
        return -1