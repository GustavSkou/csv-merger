import pandas as pd
import glob
from entrieswidgets import Entries
from entrieswidgets import Checkboxes


class CsvMerger:
    @staticmethod
    def merge():
        new_file_location = Entries.file_location
        folder_location = Entries.given_folder_location
        folder = glob.glob(folder_location + "/*.csv")
        file_name = Entries.given_file_name
        new_filetype = "." + "csv"

        Checkboxes.check_state()
        for item in Checkboxes.all_checkboxes:
            if item.nr == 0:
                if item.is_checked:
                    index_onoff = True
                else:
                    index_onoff = False
            else:
                if item.is_checked:
                    header_onoff = True
                else:
                    header_onoff = False

        print("Files to merge: ", end="")
        print(folder_size := len(glob.glob(folder_location + "/*.csv")), end=": ")
        print(folder)

        data_frames = {}
        all_data_frames = []

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

        merged_df.to_csv(new_file_location + file_name + new_filetype, index=index_onoff, header=header_onoff)
