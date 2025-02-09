import pandas as pd


# my_dict = {'A': {1: 1,
#                  2: 4,
#                  3: 6},
#            'B': {1: 2,
#                  2: 7,
#                  3: 10},
#            'C': {1: 3,
#                  2: 11,
#                  3: 16}}
#
# my_df = pd.DataFrame(my_dict)
#
# # print column C of my_df
# print(my_df['C'])

# pets = {
#     'species': ['cat', 'dog', 'parrot', 'cockroach'],
#     'name': ['Dr. Mittens Lamar', 'Diesel', 'Peach', 'Richard'],
#     'legs': [4, 4, 2, 6],
#     'wings': [0, 0, 2, 4],
#     'looking_for_home': ['no', 'no', 'no', 'yes']
# }
# df = pd.DataFrame(pets)
# print(df.info())


data = {
    "col-0": ["val-00", "val-01", "val-02"],
    "col-1": ["val-10", "val-11", "val-12"],
    "col-2": ["val-20", "val-21", "val-22"],
    "col-3": ["val-30", "val-31", "val-32"],
    "col-4": ["val-40", "val-41", "val-42"],
}

df = pd.DataFrame(data)
# print(f"=== old\n{df}")

df.columns = ["col0", "col1", "col2", "col3", "col4"]
# print(f"=== new\n{df}")

# print(f"=== axes\n{df.axes}")
# print(f"=== info:\n{df.info()}")
# print(df.info())

print(df.head())
print(df[0, "col0"])