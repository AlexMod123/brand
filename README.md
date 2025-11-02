# Brand analizer

### Example file in format csv

```name,brand,price,rating
poco x5 pro,xiaomi,299,4.4
iphone se,apple,429,4.1
galaxy z flip 5,samsung,999,4.6
redmi 10c,xiaomi,149,4.1
iphone 13 mini,apple,599,4.5

```

### Command for start from cli

```
python -m src.main --files test/fixture/products1.csv --report average-rating
```

### Example output

```
+---------+----------+
| Brand   |   Rating |
+=========+==========+
| Apple   |      4.8 |
+---------+----------+
| Xiaomi  |      4.6 |
+---------+----------+
| Samsung |      4.5 |
+---------+----------+
```
