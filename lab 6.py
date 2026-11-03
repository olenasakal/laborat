def swap_first_last_letters(text):
    if text.endswith('.'):
        text = text[:-1]
        has_dot = True
    else:
        has_dot = False
        
    words = text.split()
    processed_words = []
    
    for word in words:
        if len(word) <= 1:
            processed_words.append(word)
        else:
            new_word = word[-1] + word[1:-1] + word[0]
            processed_words.append(new_word)
            
    result = " ".join(processed_words)
    if has_dot:
        result += '.'
        
    return result

text_input = "Привіт світ програмування."

print("Початковий рядок:")
print(text_input)

result_text = swap_first_last_letters(text_input)

print("Результат після перестановки першої і останньої букви в кожному слові:")
print(result_text)
