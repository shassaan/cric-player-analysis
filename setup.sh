#!/bin/bash

# Install Spark 3.5 via Homebrew or manually if not present
# brew install apache-spark

# Set Java to version 17
export JAVA_HOME=$(/usr/libexec/java_home -v17)
export PATH="$JAVA_HOME/bin:$PATH"

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
pip install pyspark

# Set Hadoop user to avoid UGI issues
export HADOOP_USER_NAME=hassaan

mkdir -p data warehouse

# Download sample JSON if not present
cat <<EOF > data/sample.json
{"player": "Babar Azam", "year": 2015, "bio": {"full_name": "Babar Azam", "birthplace": "Lahore, Pakistan", "debut": "2015-05-31", "role": "Batsman", "batting_style": "Right-hand bat", "bowling_style": "Right-arm medium", "country": "Pakistan"}, "icc_ranking": 15, "season_stats": {"matches": 10, "innings": 13, "balls_faced": 1215, "runs_scored": 815, "average": 80, "strike_rate": 80, "not_outs": 2, "outs": 8, "bowled": 1, "caught": 0, "lbw": 2, "highest_score": 165, "hundreds": 3, "fifties": 5}, "match_performance": [{"match_id": 1, "runs": 104, "balls_faced": 76, "fours": 0, "sixes": 2, "dot_balls": 14, "minutes_at_crease": 37, "dismissal": "bowled", "opposition": "South Africa", "venue": "Sydney", "match_format": "ODI"}]}
EOF

chmod +x run.sh