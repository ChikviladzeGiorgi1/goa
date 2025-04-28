numbers = [x for x in range(1, 11)]
print(numbers)

quares = [x**2 for x in range(1, 6)]
print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)

4)words = ["apple", "banana", "cherry", "date"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c', 'd']

5)words = ["hello", "world", "python", "code"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON', 'CODE']

6)divisible_by_3 = [x for x in range(1, 51) if x % 3 == 0]
print(divisible_by_3)  # Output: [3, 6, 9, ..., 48]

7)words = ["cat", "elephant", "dog", "giraffe", "lion"]
long_words = [word for word in words if len(word) > 4]
print(long_words)  # Output: ['elephant', 'giraffe']

8)celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0, 104.0]

9)primes = [x for x in range(2, 101) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print(primes)

10)sentence = "This is an amazing example of list comprehension"
vowels = "aeiouAEIOU"
filtered_words = [word for word in sentence.split() if any(v in word for v in vowels) and len(word) > 5]
print(filteredwords)  # Output: ['amazing', 'example', 'comprehension']

11)fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for  in range(18)]
print(fibonacci)  # Output: [0, 1, 1, 2, 3, 5, ..., 4181]
