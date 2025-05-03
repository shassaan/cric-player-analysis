#!/bin/bash

# Activate environment (if applicable)
source venv/bin/activate

# Set required environment
export JAVA_HOME=$(/usr/libexec/java_home -v17)
export PATH="$JAVA_HOME/bin:$PATH"
export HADOOP_USER_NAME=hassaan

spark-submit \
  --packages org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.4.2 \
  iceberg_local.py