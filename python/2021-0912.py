class Solution:
    """
    @param s: A string
    @return: the length of last word
    """

    def lengthOfLastWord(self, s):
        word_list = s.split(" ")
        return len(word_list[-1]) if len(word_list) else 0


if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"), 5)
    print(Solution().lengthOfLastWord("Hello LintCode"), 8)
