#!/usr/bin/env python3
import pandas
visitors = [100, 150, 120, 200, 500]
errors = [23, 14, 15, 16, 25]
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=[
                      "Mon", "Tues", "Wed", "Thu", "fri"])
print(df)
means = df["errors"].mean()
medians = df["errors"].median()

print("Mean = " + str(means))
print("Median = ", (medians))
