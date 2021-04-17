def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    sentences = ["This is good", "python is good", "harry is a good boy",
                        "Subscribe to code with harry"]

    query = input("Please enter the query string ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse=True)]
    # print(sortedSentScore)
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of  {score}")
