# datamimic

Generate dataset that mimic realistic workloads

## Goals

The goal of datamimic is to provide a flexible and easy to use open source tool to support generating datasets with statistical properties that resembles realistic data. It provides ability of generating numerical/categorical data from a number of configurable distributions, with custom NDV (number of distinct values) ratios, nullability and sortedness. 

The main motivation behind datamimic is to study the effectiveness of encodings, compressions and indexing techniques used in [parquet](https://parquet.apache.org/) format with respect to table scan with a predicate on a variety of datasets with distinct statistical properties. 

It also serves as part of the testing infrastructures for exploring the idea of bringing additional indexes and data structures to parquet.

## Build
Run
```Bash
pip install -r requirements.txt
```
inside project root directory.

## Usage

```Bash
python bin/main.py <path_to_configuration_file>
```

Datamimic accpts a yaml configuration file, see an example at [example.yaml](/example.yaml), which specifies the desired data schema, statistical properties, data size and output format, etc.

