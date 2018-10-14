## What is it?

SMatrix is a lightweight and open source tool to perform basic operations on squares matrices. I developed it while preparing my exam of linear algebra (I'm a first-year physics student) because I needed a fast tool to check my calculations while doing exercises.

## What does it do?

SMatrix allows you to compute rapidly determinants and adjugates of square matrices. 

## Who is it for?

SMatrix is recommended for undergraduate students who have to take a linear algebra exam.  

## How is it developed?

SMatrix is developed completely in Python3. It uses [pyQt5](https://pypi.org/project/PyQt5/) for the user interface and [numpy](http://www.numpy.org/) for the calculations.

### Why it does calculate adjugate matrix and not inverse matrix?
$A^{-1}$

[img](http://www.sciweavers.org/tex2img.php?eq=A%5E%7B-1%7D%20%3D%20%5Cfrac%7B1%7D%7B%7CA%7C%7D%20%5Ccdot%20A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0[/img])

[img](http://www.sciweavers.org/tex2img.php?eq=A%5E%7B-1%7D%20%3D%20%5Cfrac%7B1%7D%7B%7CA%7C%7D%20%5Ccdot%20A&bc=White&fc=Black&im=jpg&fs=12&ff=modern&edit=0)[/img]
