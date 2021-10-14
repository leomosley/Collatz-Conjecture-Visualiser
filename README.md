# Collatz Conjecture Visualiser

This program visualises the Collatz Conjecture by plotting a graph with the y points being the numbers in the sequence and the x points being the number that the y point is in the sequence.

## The Conjecture

The Collatz Conjecture was created in the 1930s by Lothar Conjecture. The conjecture basically states that if you have any positive integer greater than 1, and you apply this simple function:
![](https://sites.dartmouth.edu/mathsociety/files/2019/11/gyorda_article_1_picture.png)

Eventually if you keep applying this function to each number it outputs you will eventually arrive at a loop: 4->2->1, 4 is even so we dived by 2 which gives us 2, which is also even so we divide by 2 again wich gives us 1, 1 is even so we triple it and add 1 which brings us back to 4. The Collatz Conjecture states that for any positive integer you will end up at this loop, so far there has not been a single case that disproves this.


### Collatz Conjecture Algorithim 

```python
def f(x):
    n = 0
    while x != 1:
        
        if x % 2 == 0:
            x /= 2
        else:
            x = (3*x) + 1
        
        n += 1
        print(f"x = {str(n)}, y = {str(intx))}
```

## The Visualiser
The way this visualiser works is that it takes a input by the user and applies the function to it and stores each value in a text file named "points.txt". Then using the matplotlib module it draws a graph with those points. 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
