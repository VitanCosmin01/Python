import emoji


def text_to_emoji(text):
    return emoji.emojize(text)


input_text = input("Enter text with emoji aliases: ")
converted_text = text_to_emoji(input_text)
print("Converted text with emojis:", converted_text)
