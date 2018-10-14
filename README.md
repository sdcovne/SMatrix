## What is it?

SMatrix is a lightweight and open source tool to perform basic operations on squares matrices. I developed it while preparing my exam of linear algebra (I'm a first-year physics student) because I needed a fast tool to check my calculations while doing exercises.

## What does it do?

SMatrix allows you to compute rapidly determinants and adjugates of square matrices. 

## Who is it for?

SMatrix is recommended for undergraduate students who have to take a linear algebra exam.  

## How is it developed?

SMatrix is developed completely in Python3. It uses [pyQt5](https://pypi.org/project/PyQt5/) for the user interface and [numpy](http://www.numpy.org/) for the calculations.

### Why it does calculate adjugate matrix and not inverse matrix?

When you have to deal with inverses matrices, usually you have to deal with fractions. Without using a specific library as Simpy, fractions are rendered as decimals and often you end up with decimals with more than 10 figures. Even if you're working on small matrix, let's say 4x4, is overwhelming seeing 16 10-figures decimals numbers. Furthermore Numpy's approximation aren't 100% accurate on big decimals numbers.

For those reasons I preffered to work with adjugates matrices. You should also considering that once the determinant and the adjugate of a matrix are known is just a matter of basic arithmetics compute the inverse of that matrix.
