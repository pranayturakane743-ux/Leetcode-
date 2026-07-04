#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
    void backtrack(std::vector<std::string>& result, std::string current, int open, int close, int n) {
        // Base case: if the string is complete
        if (current.length() == 2 * n) {
            result.push_back(current);
            return;
        }

        // Add an opening parenthesis if we still have some left
        if (open < n) {
            backtrack(result, current + "(", open + 1, close, n);
        }

        // Add a closing parenthesis if it won't break the well-formed rule
        if (close < open) {
            backtrack(result, current + ")", open, close + 1, n);
        }
    }

    std::vector<std::string> generateParenthesis(int n) {
        std::vector<std::string> result;
        backtrack(result, "", 0, 0, n);
        return result;
    }
};