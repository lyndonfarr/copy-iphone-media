import os, os.path, pathlib, sys, time
from datetime import datetime
from shutil import copy2
from sys import argv

months = {
    "jan": "01",
    "feb": "02",
    "mar": "03",
    "apr": "04",
    "may": "05",
    "jun": "06",
    "jul": "07",
    "aug": "08",
    "sep": "09",
    "oct": "10",
    "nov": "11",
    "dec": "12",
}

def getFileName(filename, extension, destination, duplicate_count = 1):
    if not os.path.isfile(f'{destination}/{filename}{extension}'):
        return f'{filename}{extension}'
    return getFileName(f'{filename}-{duplicate_count}', extension, destination, duplicate_count + 1)

def getFormattedDateTime(date_time_array):
    created_year = date_time_array[-1]
    created_month_hr = date_time_array[1].lower()
    created_month = months[created_month_hr]
    created_day_raw = date_time_array[2]
    created_day = created_day_raw if len(created_day_raw) == 2 else f'0{created_day_raw}'
    created_time = date_time_array[3].replace(':', '.')
    return f'{created_year}-{created_month}-{created_day} {created_time}'

def throwMediaItemError(iphone_media_item, message):
    print(f'Error with media item {iphone_media_item}: {message}. Skipping.')

input_args = sys.argv[2:]
arg_count = len(input_args)

if arg_count == 0:
    print('Give me some arguments!')
    exit()

print(f'Copying {arg_count} pieces of media from iphone to desktop...')

destination = sys.argv[1]

if not os.path.isdir(destination):
    os.mkdir(destination)

loopcounter = 0
tracker = {}
for iphone_media in input_args:
    loopcounter = loopcounter + 1

    tracker[iphone_media] = 'THISISNOTAFILEWHICHEXISTS.DJHGFIUYD'

    file_extension = pathlib.Path(iphone_media).suffix

    if not file_extension:
        throwMediaItemError(iphone_media, 'No file extension')
        continue

    created_datetime = time.ctime(os.path.getmtime(iphone_media))
    created_datetime_array = created_datetime.split()

    if not len(created_datetime_array) == 5:
        throwMediaItemError(iphone_media, 'Incorrect number of elements in date time array')
        continue

    created_datetime_formatted = getFormattedDateTime(created_datetime_array)

    if len(created_datetime_formatted) < 19:
        throwMediaItemError(iphone_media, 'Datetime formatted length incorrect')
        continue

    filename = getFileName(created_datetime_formatted, file_extension, destination)

    tracker[iphone_media] = filename

    copy2(iphone_media, f'{destination}/{filename}')

failed_count = 0
for iphone_media in input_args:
    if not os.path.exists(f'{destination}/{tracker[iphone_media]}'):
        print(f'{iphone_media} did not successfully copy.')
        failed_count = failed_count + 1

successfully_copied_count = len(os.listdir(destination))
print(f'Looped through {loopcounter} times.')
print(f'Successfully copied {successfully_copied_count} media items.')
print(f'{failed_count} items were unsuccessful.')