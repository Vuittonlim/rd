# Clean data
# Minimal cleaning needed, as it is mostly clean
# Rename columns to lowercase to avoid potential clashes with sql
# Add one more column that sums up total tap in and tap out
import pandas as pd
pd.set_option('display.max_columns', None) # Shows all columns

def transform():
    df = pd.read_csv('../data/transport_node_train_202310.csv')
    df.rename(columns={
        'YEAR_MONTH': 'year_month',
        'DAY_TYPE': 'day_type',
        'TIME_PER_HOUR': 'time_per_hour',
        'PT_TYPE': 'pt_type',
        'PT_CODE' : 'pt_code',
        'TOTAL_TAP_IN_VOLUME': 'total_tap_in_volume',
        'TOTAL_TAP_OUT_VOLUME':'total_tap_out_volume'
    }, inplace=True)

    # The total volume of tap in and tap out for each entry
    df['total_volume'] = df['total_tap_in_volume'] + df['total_tap_out_volume']
    return df

