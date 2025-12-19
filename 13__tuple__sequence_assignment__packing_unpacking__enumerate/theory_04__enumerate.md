## Удобное сочетание индекса и значения в одной итерации


```python
fruits = ['apple', 'lemon', 'orange']

for i, fruit in enumerate(fruits):
    print(i, fruit)


# 0 apple
# 1 lemon
# 2 orange
```

## Установка начального значения индекса

```python
fruits = ['apple', 'lemon', 'orange']

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)


# 1 apple
# 2 lemon
# 3 orange
```
