#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
  if n <= 0:
    return[]
  if n == 1:
    return[1]
  if n == 2:
    return[1,1]
  if n > 2:
    triangle = []
    new = []
    triangle.append([1])
    triangle.append([1,1])
    
    for i in range(3, n+1):
      for j in range(0, i-1):
        if new == []:
          new.append(1)
          continue
        number = triangle[-1][j-1] + triangle[-1][j]
        new.append(number)
        if j == i-2:
          new.append(1)
          triangle.append(new)
          new = []

    return triangle
