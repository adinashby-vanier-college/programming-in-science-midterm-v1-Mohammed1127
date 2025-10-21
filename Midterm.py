import math

# Q1: Calculate the area of a circle
def area_of_circle(radius) :

    area = round((math.pi) * (radius**2), 2)
    
    return area



# Q2: Hollow Right Triangle
def hollow_right_triangle(n) :
    
    answer = ""

    if n < 4 :

        answer += "The triangle height should be at least 4."

    else :

        for i in range(1, n+1) :

            if i == 1 or i == n :

                answer += i * "*" + '\n'

            else :

                answer += "*" + (i-2)*" " + "*" + '\n'
    

    return answer.rstrip()


        
# Q3: Inverted Pyramid
def inverted_pyramid(n): 

    result = "" 

    if n < 3 :

        result += "The pyramid height should be at least 3."

    else : 

        for j in range(1, n+1) :

            result += (j-1) * " " + ((2*n -1)-(2*j -2)) * "*" + '\n'

    return result.rstrip()


# ----------------------------------------------------------------
print(area_of_circle(10))
print()

print(area_of_circle(1))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()