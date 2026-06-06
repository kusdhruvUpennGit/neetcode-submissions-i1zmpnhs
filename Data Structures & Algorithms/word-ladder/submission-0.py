from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If the target word is not in the dictionary, no valid transformation exists
        if endWord not in wordList:
            return 0

        # All words are assumed to have the same length
        word_length = len(beginWord)

        # Map each wildcard pattern to all words matching that pattern
        # Example: "hot" -> "*ot", "h*t", "ho*"
        pattern_to_words = defaultdict(list)

        # Build the wildcard pattern map
        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_to_words[pattern].append(word)

        # Standard BFS queue: (current_word, current_distance)
        queue = deque([(beginWord, 1)])

        # Track visited words to avoid cycles and repeated work
        visited = set([beginWord])

        while queue:
            current_word, distance = queue.popleft()

            # If we reached the target, return the number of words in the path
            if current_word == endWord:
                return distance

            # Generate all wildcard patterns for the current word
            for i in range(word_length):
                pattern = current_word[:i] + "*" + current_word[i + 1:]

                # Explore all neighbors that share this wildcard pattern
                for neighbor in pattern_to_words[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

                # Clear the list after use so we do not reprocess the same pattern again
                pattern_to_words[pattern] = []

        # If BFS ends without finding endWord, no transformation exists
        return 0
