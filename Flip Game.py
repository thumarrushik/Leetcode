class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        vector<string> result;
        int n = s.length();
        for (int a1 = 0; a1 < n - 1; a1++) {
            if (s[a1] == '+' && s[a1 + 1] == '+') { 
                s[a1] = s[a1 + 1] = '-';
                result.push_back(s);
                s[a1] = s[a1 + 1] = '+';
            }
        }
        return result;
    }
};


/*
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

*/
