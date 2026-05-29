class TrieNode {
public:
    // Pointers to child nodes for each lowercase letter
    TrieNode* children[26];

    // Marks whether a word ends at this node
    bool isEnd;

    TrieNode() {
        // Initialize all children to null
        for (int i = 0; i < 26; i++) {
            children[i] = nullptr;
        }

        // Initially, no word ends here
        isEnd = false;
    }
};

class WordDictionary {
public:
    // Root of the trie
    TrieNode* root;

    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(string word) {
        TrieNode* node = root;

        // Insert each character into the trie
        for (char c : word) {
            int index = c - 'a';

            // Create node if path does not exist
            if (node->children[index] == nullptr) {
                node->children[index] = new TrieNode();
            }

            // Move to next node
            node = node->children[index];
        }

        // Mark the end of a complete word
        node->isEnd = true;
    }

    // DFS helper for searching with wildcard support
    bool dfs(string& word, int pos, TrieNode* node) {
        // If we reached the end of the word,
        // return whether this node marks a complete word
        if (pos == word.size()) {
            return node->isEnd;
        }

        char c = word[pos];

        // If current character is a wildcard, try all possible children
        if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (node->children[i] != nullptr) {
                    if (dfs(word, pos + 1, node->children[i])) {
                        return true;
                    }
                }
            }

            // No child path matched
            return false;
        }

        // Normal character case
        int index = c - 'a';

        // If path doesn't exist, word is not found
        if (node->children[index] == nullptr) {
            return false;
        }

        // Continue searching next character
        return dfs(word, pos + 1, node->children[index]);
    }

    bool search(string word) {
        return dfs(word, 0, root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
