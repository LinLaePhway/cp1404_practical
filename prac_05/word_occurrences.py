def main():
    user_input = input("Text: ")
    words = user_input.split()
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    for word, count in sorted(word_counts.items()):
        print(f"{word} : {count}")


main()
