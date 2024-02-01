from collections import defaultdict


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, sentence):
        '''
        i: {
            ' ': {
                l: {
                    o: {

                    }
                }
            }
        }
        '''
        current_node = self.root
        for c in sentence:
            if c not in current_node:
                current_node[c] = {}
            current_node = current_node[c]
        current_node['#'] = sentence


    def search(self, keyword, current_node=None):
        if not current_node:
            current_node = self.root

        for c in keyword:
            if c not in current_node:
                return []
            current_node = current_node[c]
        ans = []
        for k in current_node:
            if k == '#':
                ans.append(current_node[k])
            else:
                ans += self.search('', current_node[k])
        return ans


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        # Store sentence and its freq in a dictionary
        self.sent_freq_map = defaultdict(int)
        for i in range(len(sentences)):
            s, t = sentences[i], times[i]
            self.sent_freq_map[s] = t

        # Initialize a tire datastructure
        self.trie = Trie()
        for s in sentences:
            self.trie.insert(s)

        # Have a variable to store all user inputs
        self.keyword = ''


    def input(self, c: str) -> List[str]:
        if c == '#':
            # Stores inputted sentence in the system
            self.sent_freq_map[self.keyword] += 1
            self.trie.insert(self.keyword)
            self.keyword = ''
            return []
        else:
            self.keyword += c
            # Search results returned based on the keyword search
            search_res = self.trie.search(self.keyword)
            print(search_res)

            # Suppose search_res is ['apple', 'banana', 'orange'], and self.sent_freq_map is {'apple': 3, 'banana': 5, 'orange': 2}.

            # For each sentence in search_res, the lambda function computes a tuple:

            # For 'apple': (-self.sent_freq_map['apple'], 'apple') = (-3, 'apple')
            # For 'banana': (-self.sent_freq_map['banana'], 'banana') = (-5, 'banana')
            # For 'orange': (-self.sent_freq_map['orange'], 'orange') = (-2, 'orange')
            # After sorting based on the tuples:

            # 'banana' comes first because it has the highest frequency (5).
            # 'apple' comes next with frequency (3).
            # 'orange' comes last with frequency (2).

            search_res.sort(key = lambda x: (-self.sent_freq_map[x], x) )
            return search_res[:3]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)