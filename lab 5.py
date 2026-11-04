def vector_norm(vector):
    if not vector:
        return 0
    return max(abs(x) for x in vector)

def process_vectors(v1, v2):
    norm1 = vector_norm(v1)
    norm2 = vector_norm(v2)
    
    print(f"Вектор 1: {v1} (Норма = {norm1})")
    print(f"Вектор 2: {v2} (Норма = {norm2})")
    
    if norm1 < norm2:
        v1 = [x ** 2 for x in v1]
        print("\nНорма першого вектора менша. Заміну проведено у першому векторі.")
    elif norm2 < norm1:
        v2 = [x ** 2 for x in v2]
        print("\nНорма другого вектора менша. Заміну проведено у другому векторі.")
    else:
        v1 = [x ** 2 for x in v1]
        v2 = [x ** 2 for x in v2]
        print("\nНорми векторів однакові. Заміну проведено в обох векторах.")
        
    return v1, v2

vector_a = [-3, 5, -1]
vector_b = [2, -4, 1]

print("--- До обробки ---")
updated_a, updated_b = process_vectors(vector_a, vector_b)

print("\n--- Після обробки ---")
print(f"Новий вектор 1: {updated_a}")
print(f"Новий вектор 2: {updated_b}")
