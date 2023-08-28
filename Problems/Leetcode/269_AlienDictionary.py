class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alien_order(self, words: List[str]) -> str:
        # Time: O(c) where c is number of characters
        # Space: O(V + E) V-Nodes, E-Edges

        # Make a graph
        char_graph = {}
        # This will contain a char and characters that come after a character. Ex: b: [a, c]
        for word in words:
            for c in word:
                char_graph[c] = []

        # Populate the graph
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            min_length = min(len(w1), len(w2))
            # [apes, ape], retun empty string
            if len(w1) > len(w2) and w1[:min_length] == w2[:min_length]:
                return ""
            # If characters are different, store it graph the char and the chars that come after it
            for j in range(min_length):
                if w1[j] != w2[j]:
                    char_graph[w1[j]].append(w2[j])
                    break

        visited = {}
        res = []
        # DFS
        def is_cycle(c):
            if c in visited:
                return visited[c]
            # Mark the node visited
            visited[c] = True
            # Do DFS for all neighbors
            for neighbor in char_graph[c]:
                if is_cycle(neighbor):
                    return True
            visited[c] = False
            res.append(c)
            return False

        # Iterate graph
        for c in sorted(char_graph.keys(), reverse=True):
            if is_cycle(c):
                return ""

        res.reverse()
        return ''.join(res)
