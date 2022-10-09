import pandas as pd
import glob

print("Files to merge: ", end="")
print(folder_size := len(glob.glob("files/*.csv")), end=": ")
print(folder := glob.glob("files/*.csv"))
data_frames = {}
all_data_frames = []
merged_df = pd.DataFrame()

for x in range(1, folder_size + 1):
    data_frames["df_{0}".format(x)] = pd.read_csv(folder[x - 1], sep=';')
    all_data_frames.append(data_frames["df_{0}".format(x)])
    print(folder[x - 1])
    print(data_frames["df_{0}".format(x)])

print("Merged file:")
merged_df = pd.concat(all_data_frames)
merged_df = merged_df.dropna(how='all')
merged_df = merged_df.reset_index(drop=True)
print(merged_df)

merged_df.to_csv("merged-file.csv")
