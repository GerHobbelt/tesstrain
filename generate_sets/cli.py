# -*- coding: utf-8 -*-
"""Generate Sets of Training Data TextLine + Image Pairs"""

import argparse
import os

from generate_sets.training_sets import (
    TrainingSets,
    DEFAULT_OUTDIR_PREFIX,
    DEFAULT_MIN_CHARS,
    DEFAULT_USE_SUMMARY,
    DEFAULT_USE_REVERT,
    SUMMARY_SUFFIX
)


########
# MAIN #
########
PARSER = argparse.ArgumentParser(description="generate pairs of textlines and image frames from existing OCR and image data")
PARSER.add_argument(
    "data",
    type=str,
    help="path to local alto|page file corresponding to image")
PARSER.add_argument(
    "-i",
    "--image",
    required=False,
    help="path to local image file tif|jpg|png corresponding to ocr. (default: read from OCR-Data)")
PARSER.add_argument(
    "-o",
    "--output",
    required=False,
    help="optional: output directory, re-created if already exists. (default: <script-dir>/<{}-ocr-name>)".format(DEFAULT_OUTDIR_PREFIX))
PARSER.add_argument(
    "-m",
    "--minchars",
    required=False,
    type=int,
    default=int(DEFAULT_MIN_CHARS),
    help="optional: minimum chars required for a line to be included into set (default: {})".format(DEFAULT_MIN_CHARS))
PARSER.add_argument(
    "-s",
    "--summary",
    required=False,
    action='store_true',
    default=DEFAULT_USE_SUMMARY,
    help="optional: print all lines in additional file (default: {}, pattern: <default-output-dir>{})".format(DEFAULT_USE_SUMMARY, SUMMARY_SUFFIX))
PARSER.add_argument(
    "-r",
    "--rtl",
    required=False,
    action='store_true',
    default=DEFAULT_USE_REVERT,
    help="optional: attempt to switch reading order right-to-left (default: {})".format(DEFAULT_USE_REVERT))

ARGS = PARSER.parse_args()
PATH_OCR = ARGS.data
PATH_IMG = ARGS.image
FOLDER_OUTPUT = ARGS.output
MIN_CHARS = ARGS.minchars
SUMMARY = ARGS.summary
REVERT = ARGS.rtl

if os.path.exists(PATH_OCR) and os.path.exists(PATH_IMG):
    print("[INFO   ] generate trainingsets of '{}' with '{}' (min: {}, sum: {}, rtl: {})".format(
        PATH_OCR, PATH_IMG, MIN_CHARS, SUMMARY, REVERT))
    TRAINING_DATA = TrainingSets(PATH_OCR, PATH_IMG)
    RESULT = TRAINING_DATA.create(
        folder_out=FOLDER_OUTPUT,
        min_chars=MIN_CHARS,
        summary=SUMMARY,
        revert=REVERT)
    print(
        "[SUCCESS] created '{}' training data sets in '{}', please review".format(
            len(RESULT), TRAINING_DATA.path_out))
else:
    print(
        "[ERROR  ] missing OCR '{}' or Image Data '{}'!".format(
            PATH_OCR,
            PATH_IMG))
