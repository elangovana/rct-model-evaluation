import argparse
import logging
import os
import sys

import pandas as pd


class PreprocessRCTIMDB:
    """
    Create control and contrast set using https://github.com/allenai/contrast-sets/tree/main/IMDb/data
    """

    def __init__(self):
        pass

    def process(self, dataset_tsv_original_file, dataset_tsv_contrast_file):
        original_df = pd.read_csv(dataset_tsv_original_file, delimiter="\t", header=0,
                                  names=["case_label", "case_text"])
        contrast_df = pd.read_csv(dataset_tsv_contrast_file, delimiter="\t", header=0,
                                  names=["control_label", "control_text"])

        df = original_df.merge(contrast_df, left_index=True, right_index=True)

        return df

    def process_outfile(self, dataset_tsv_original_file, dataset_tsv_contrast_file, output_file):
        df = self.process(dataset_tsv_original_file, dataset_tsv_contrast_file)
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        df.to_json(output_file, orient='records')


def run_main():
    parser = argparse.ArgumentParser()

    parser.add_argument("inputcasefile",
                        help="The case file")

    parser.add_argument("inputcontrolfile",
                        help="The control file")

    parser.add_argument("outputfile",
                        help="The output file")

    parser.add_argument("--log-level", help="Log level", default="INFO", choices={"INFO", "WARN", "DEBUG", "ERROR"})

    args = parser.parse_args()
    # Set up logging
    logging.basicConfig(level=logging.getLevelName(args.log_level), handlers=[logging.StreamHandler(sys.stdout)],
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    print(args.__dict__)

    PreprocessRCTIMDB().process_outfile(args.inputcasefile, args.inputcontrolfile, args.outputfile)


if __name__ == "__main__":
    run_main()
