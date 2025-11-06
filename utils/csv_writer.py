from csv import DictWriter
from datetime import datetime
from os import path

# Windows doesn't support having : in the file name.
CSV_FILE_NAME = str(str(datetime.today())[:16]).replace(":", "-") + ".csv"

# NOTE: Make sure header do not repeat.
CSV_FILE_HEADER = ["id", "name", "2", "3"]

#
CSV_FILE_HEADER.append("datetime")


class CSV:

    @staticmethod
    def init(overwrite=False):
        """
        Initialize the CSV file by writing the header to it.

        Args:
            overwrite (bool): If true, overwrite the existing CSV file.
        """
        if not path.exists(CSV_FILE_NAME) or overwrite:
            with open(CSV_FILE_NAME, "w", newline="", encoding="utf-8-sig") as csvfile:
                filewriter = DictWriter(csvfile, fieldnames=CSV_FILE_HEADER)
                filewriter.writeheader()

    @staticmethod
    def write_record(row_dict: dict, remove_extra: bool = False):
        """
        Write a record to the CSV file.

        Args:
            row_dict (dict): A dictionary containing the data to be written to the CSV file.
            remove_extra (bool, optional): If true, remove any keys from rowDict that are not in CSV_FILE_HEADER. Defaults to False.

        Returns:
            None
        """
        row_dict["datetime"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # get the lock to write on the CSV file by opening it in append mode.
        with open(CSV_FILE_NAME, "a", newline="", encoding="utf-8-sig") as csvfile:
            filewriter = DictWriter(csvfile, fieldnames=CSV_FILE_HEADER)

            # Remove extra keys from dict to avoid errors
            if remove_extra:
                for e in set(row_dict.keys()) - set(CSV_FILE_HEADER):
                    del remove_extra[e]

            # finally, write a record on CSV file.
            filewriter.writerow(row_dict)
