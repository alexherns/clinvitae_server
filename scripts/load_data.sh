set -e

SOURCE_DIR=`dirname $BASH_SOURCE`

DATA_PATH=$1
DOWNLOAD_PATH="$DATA_PATH/variants.zip"
VARIANTS_DATA="$DATA_PATH/variant_results.tsv"
VARIANT_SAMPLE_FILE="$DATA_PATH/variant_sampling.tsv"
DB_SCHEMA_FILE="$DATA_PATH/schema.sql"
DB_FILE="$DATA_PATH/variants.db"

echo "Will export database to $DB_FILE"

# download data from server
wget -O $DOWNLOAD_PATH http://clinvitae.invitae.com/download
# unzip
unzip -d $DATA_PATH $DOWNLOAD_PATH 
# lowercase and covert spaces to underscore
head -n1 $VARIANTS_DATA | tr '[:upper:] ' '[:lower:]_' > $VARIANT_SAMPLE_FILE
# grab some data
head -n10000 $VARIANTS_DATA | tail -n +2 >> $VARIANT_SAMPLE_FILE
# predict schema but clean up " NOT NULL" because we will be flexible
csvsql -i sqlite -t --no-constraints --tables variants $VARIANT_SAMPLE_FILE > $DB_SCHEMA_FILE
rm $VARIANT_SAMPLE_FILE
# load the actual variants into db
python $SOURCE_DIR/load_variants.py $DB_SCHEMA_FILE $VARIANTS_DATA $DB_FILE

