"""A simple main file to showcase the template."""

import argparse
import logging.config

from google.cloud import storage

"""
This module is an example for a single Python application with some
top level functions. The tests directory includes some unitary tests
for these functions.

This is one of two main files samples included in this
template. Please feel free to remove this, or the other
(sklearn_main.py), or adapt as you need.
"""

LOGGER = logging.getLogger()


def _list_files_by_prefix(bucket_name, prefix):
  storage_client = storage.Client()
  # Note: Client.list_blobs requires at least package version 1.17.0.
  blobs = storage_client.list_blobs(
      bucket_name, prefix=prefix, delimiter=None)
  # n_objs = len(blobs)
  # LOGGER.info("Found %d objects" % n_objs)

  N = 5
  k = 0
  for blob in blobs:
    k += 1
    print("Sample name found in bucket: %s" % blob.name)
    if k > N:
      break


def download_prepare_data(bucket_name, prefix):
  """Download and prepare the data for training.

  Args:
    bucket_name: Name of the bucket where the data is stored
    prefix: Prefix to the path of all the files
  """
  _list_files_by_prefix(bucket_name, prefix)


def train_and_evaluate(bucket_name, prefix):
  """Train and evaluate the model."""
  download_prepare_data(bucket_name, prefix)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--bucket-name", required=True)
  parser.add_argument("--prefix", required=True)

  args = parser.parse_args()

  bucket_name = args.bucket_name
  prefix = args.prefix

  train_and_evaluate(bucket_name, prefix)
