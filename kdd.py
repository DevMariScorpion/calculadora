import time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def process_file(filename):
    with open(filename, 'r') as file:
        words = []
        for line in file:
            words.extend(line.split())
    return words


def main():
    filename = 'texto.txt'  
    
    
    words = process_file(filename)
    
    
    start_time = time.time()
    bubble_sorted_words = bubble_sort(words.copy())
    bubble_sort_time = time.time() - start_time
    print(f'Bubble Sort:\n{bubble_sorted_words}')
    print(f'Tempo de execução: {bubble_sort_time:.6f} segundos\n')
    
    
    start_time = time.time()
    selection_sorted_words = selection_sort(words.copy())
    selection_sort_time = time.time() - start_time
    print(f'Selection Sort:\n{selection_sorted_words}')
    print(f'Tempo de execução: {selection_sort_time:.6f} segundos\n')
    
  
    start_time = time.time()
    sorted_words = words.copy()
    sorted_words.sort()
    sort_time = time.time() - start_time
    print(f'Sort (Método Nativo):\n{sorted_words}')
    print(f'Tempo de execução: {sort_time:.6f} segundos\n')
    
    
    best_method = min((('Bubble Sort', bubble_sort_time), 
                        ('Selection Sort', selection_sort_time), 
                        ('Sort', sort_time)), key=lambda x: x[1])[0]
    print(f'Melhor método: {best_method}')
    
   
    output_filename = 'sorted_words.txt'
    if best_method == 'Bubble Sort':
        best_sorted_words = bubble_sorted_words
    elif best_method == 'Selection Sort':
        best_sorted_words = selection_sorted_words
    else:
        best_sorted_words = sorted_words
    
    with open(output_filename, 'w') as file:
        for word in best_sorted_words:
            file.write(word + '\n')

if __name__ == '__main__':
    main()
