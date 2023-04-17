def sayHi(name):
    print("Hi, " + name)

# Return values with functions


def area_triangle(base, height):
    return base*height/2

# floor division


def convrt_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


sayHi("Interwire")
print(area_triangle(10, 5))
hours, minutes, seconds = convrt_seconds(5000)
print(hours, minutes, seconds)
