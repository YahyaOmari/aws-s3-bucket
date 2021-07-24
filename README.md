# Steps I have been taken.

## For [aws s3 bucket](aws-s3-bucket.py) file

1. I downloaded S3 bucket files using boto3 package.
2. Then decompress the files using glob package.
3. Read the files.
4. I saved the db host, db name, db user, db password and port in .env file, and included the .env file to .gitignore file. Using dotenv package. I used it because it makes configuration easier and better security.
5. To connect to the db I used psycopg2.
