from aws import S3
import datetime
import pandas as pd

RAWDATA_BUCKET = 'kpu-gradutation-team-rawdata-dev'

S3_CLIENT = S3()

dt_obj = datetime.datetime.now(datetime.timezone.utc)

print(dt_obj)

raw_files = [raw_file["Key"] for raw_file in S3_CLIENT.get_keys(Bucket=RAWDATA_BUCKET,
                                                                Prefix="/kpu/rawdata/{:04d}/{:02d}/{:02d}/{:02d}".format(
                                                                                                               dt_obj.year,
                                                                                                               dt_obj.month,
                                                                                                               dt_obj.day,
                                                                                                               dt_obj.hour),
                                                                is_sorted=False)
             if raw_file.get('Key', '').endswith('.csv')]
print("raw file count : ", len(raw_files))
print(raw_files)

new_report_df = pd.DataFrame(columns=['timestamp_from', 'timestamp_to', 'status'])
merged_df = pd.concat(
    [pd.read_csv(S3_CLIENT.read_file(Bucket=RAWDATA_BUCKET, Key=raw_file)['Body']) for raw_file in raw_files],
    join='outer', sort=False)
merged_df = merged_df.replace({pd.np.nan: None})