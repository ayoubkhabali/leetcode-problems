class Solution(object):
    def isCircularSentence(self, sentence):
        sen_list = sentence.split(" ")
        last_char = None

        for i in range(len(sen_list)):
            word = sen_list[i]

            if last_char is None:
                last_char = word[-1]
                continue

            if last_char != word[0]:
                return False

            last_char = word[-1]

        return last_char == sen_list[0][0]
