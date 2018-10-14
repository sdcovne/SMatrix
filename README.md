## What is it?

SMatrix is a lightweight and open source tool to perform basic operations on squares matrices. I developed it while preparing my exam of linear algebra (I'm a first-year physics student) because I needed a fast tool to check my calculations while doing exercises.

## What does it do?

SMatrix allows you to compute rapidly determinants and adjugates of square matrices. 

## Who is it for?

SMatrix is recommended for undergraduate students who have to take a linear algebra exam.  

## How is it developed?

SMatrix is developed completely in Python3. It uses [pyQt5](https://pypi.org/project/PyQt5/) for the user interface and [numpy](http://www.numpy.org/) for the calculations.

### Why it does calculate adjugate matrix and not inverse matrix?

![\Large A^{-1} = \frac{1}{|A|} \cdot A](https://latex.codecogs.com/svg.latex?x%3D%5Cfrac%7B-b%5Cpm%5Csqrt%7Bb%5E2-4ac%7D%7D%7B2a%7D)
