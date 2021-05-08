```

     _____________________________/\/\______________________________/\/\_____
    _/\/\/\__/\/\____/\/\/\______/\/\______/\/\/\____/\/\__/\/\__/\/\/\/\/\_
   _/\/\/\/\/\/\/\______/\/\____/\/\____/\/\__/\/\__/\/\/\/\______/\/\_____
  _/\/\__/\__/\/\__/\/\/\/\____/\/\____/\/\__/\/\__/\/\__________/\/\_____
 _/\/\______/\/\__/\/\/\/\/\__/\/\/\____/\/\/\____/\/\__________/\/\/\___
________________________________________________________________________

```

### Malort: JSON -> Relational DB Column Types

Malort is a tool for taking nested JSON data and trying to sniff out the appropriate relational db column types from the keys and values. It currently only supports Redshift, but the column mappers can be easily extended to other DBs.

The Problem
-----------
A producer is dumping semi-structured .json or delimited json blobs into a directory/S3 and you need to warehouse it somewhere. You don't know the schema, but want to find out if it's stable enough to break out into columns, or if you need to dump the whole blob into a JSON column type.

Why
-----
Because for (mostly) structured documents where we're expecting the schema to rarely change, we'd rather have the speed and familiar query/index-ability of table columns rather than dumping the entire blob into a single column.

How
------
Malort will read through a directory of .json or flat text files (optionally gzipped) with delimited JSON blobs and generate relevant statistics on each key. It uses the Dask libary to parallelize these computations.

For example, let's look at a directory with two JSON files, and one text file with newline-delimited JSON:
```json
{"intfield": 5,
 "floatfield": 2.345,
 "parentkey": {
     "datefield": "2014-09-26 17:00:00",
     "charfield": "fixedlength"
 },
 "varcharfield": "var"}

{"intfield": 10,
 "floatfield": 4.7891,
 "parentkey": {
     "datefield": "2014-09-26 17:00:00",
     "charfield": "fixedlength"
 },
 "varcharfield": "varyin"}
 ```

 ```
{"intfield": 15,"floatfield": 3.0012,"parentkey":{"charfield": "fixedlength","datefield": "2014-09-26 17:00:00"}, "varcharfield": "varyingle"}
{"intfield": 20,"floatfield": 10.8392,"parentkey" :{"charfield": "fixedlength","datefield": "2014-09-26 17:00:00"},"varcharfield": "varyinglengt"}
```

Malort will calculate relevant statistics for each key, with both the base key and the nested key path:
```python
>>> import malort as mt
>>> result = mt.analyze('dir', delimiter='\n')
>>> result.stats
{'floatfield': {'base_key': 'floatfield',
                'float': {'count': 4,
                          'fixed_length': False,
                          'max': 10.8392,
                          'max_precision': 6,
                          'max_scale': 4,
                          'mean': 5.243,
                          'min': 2.345}},
 'intfield': {'base_key': 'intfield',
              'int': {'count': 4, 'max': 20, 'mean': 12.5, 'min': 5}},
 'parentkey.charfield': {'base_key': 'charfield',
                         'str': {'count': 4,
                                 'max': 11,
                                 'mean': 11.0,
                                 'min': 11,
                                 'sample': ['fixedlength',
                                            'fixedlength',
                                            'fixedlength']}},
 'parentkey.datefield': {'base_key': 'datefield', 'datetime': {'count': 4}},
 'varcharfield': {'base_key': 'varcharfield',
                  'str': {'count': 4,
                          'max': 12,
                          'mean': 7.5,
                          'min': 3,
                          'sample': ['varyin', 'varyingle', 'varyinglengt']}}}
```

Malort has determined the type(s) for each key, as well as relevant statistics for that type. Malort can then be used to guess the Redshift column types:

```python
>>> result.get_redshift_types()
{'parentkey.charfield': 'char(11)',
 'parentkey.datefield': 'TIMESTAMP',
 'varcharfield': 'varchar(12)',
 'floatfield': 'REAL',
 'intfield': 'SMALLINT'}
 ```

Malort supports the ability to print the entire result as a Pandas DataFrame:
```python
>>> df = result.to_dataframe()
                   key      base_key  count      type    mean      max     min  max_precision  max_scale fixed_length                                   sample redshift_types
0  parentkey.charfield     charfield      4       str  11.000  11.0000  11.000            NaN        NaN         None  [fixedlength, fixedlength, fixedlength]       char(11)
1             intfield      intfield      4       int  12.500  20.0000   5.000            NaN        NaN         None                                     None       SMALLINT
2         varcharfield  varcharfield      4       str   7.500  12.0000   3.000            NaN        NaN         None                 [var, varyin, varyingle]    varchar(12)
3           floatfield    floatfield      4     float   5.243  10.8392   2.345              6          4        False                                     None           REAL
4  parentkey.datefield     datefield      4  datetime     NaN      NaN     NaN            NaN        NaN         None                                     None      TIMESTAMP
```

Install
-------
`$ pip install malort`

API
---
* `result = malort.analyze(path, parse_timestamps=True)`

```python
Analyze a given directory of either .json, flat text files
with newline-delimited JSON, or gzipped files with newline-delimted JSON to get relevant key statistics.

Parameters
----------
path: string
    Path to directory
parse_timestamps: boolean, default True
    If True, will attempt to regex match ISO8601 formatted parse_timestamps
```

* `result.stats`: Dictionary of key statistics
* `result.get_conflicting_types`: Return only stats where there are multiple types detected for a given key
* `result.get_redshift_types`: Guess the Amazon Redshift column types for the result keys
* `result.gen_redshift_jsonpaths`: Generate Redshift [jsonpaths](http://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html#copy-from-json-examples-using-jsonpaths) file
* `result.to_dataframe`: Export the result set to a dataframe
* `result.get_cleaned_column_names`: Clean up the result keys into underscored/camel-cased column names

Adding New Type Mappers
-----------------------
New type mappers must have functions that map from a given input type (bool, str, int, float, date) to a database column type. For example, the `RedshiftMapper` integer mapper:
```python
@staticmethod
def ints(stat):
    if stat['min'] > -32768 and stat['max'] < 32767:
        return 'SMALLINT'
    elif stat['min'] > -2147483648 and stat['max'] < 2147483647:
        return 'INTEGER'
    else:
        return 'BIGINT'
```

This allows malort to be easily extended to other Databases.

Why is it named Malort?
-----------------------
Because this is kind of a distasteful thing to do in the first place.

Couldn't I have done this with sed/awk/xargs/mapreduce?
-------------------------------------------------------
Yes.

How fast is it?
---------------
With timestamp parsing turned on, I used Malort to process 2.1 GB of files (1,326,794 nested JSON blobs) in 8 minutes. There are undoubtedly ways to do it faster. Speed will depend on a number of factors, including nesting depth.

Should I use the column type results verbatim?
----------------------------------------------
Probably not- they're meant to be a guide, not a CREATE TABLE statement. It's up to you to determine whether your data represents a large and representative enough sample to set fixed-width columns with certainty, or whether you might anticipate schema changes in the future. Like a lot of data tools, it's meant to help guide your engineering judgement. Additionally, it does round/truncate statistics to three decimal points, so there will be floating point errors in the calculation.
