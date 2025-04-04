import pandas as pd        

data = {
    "name":["John", "Alice", "Bob"],
    "age":[25, 30, 22],
    "Height":[175.5, 160.0, 180]
}
Labels = ["student1", "student2", "student3"]
df = pd.DataFrame(data, index=Labels)
print(df)
print(df.info())