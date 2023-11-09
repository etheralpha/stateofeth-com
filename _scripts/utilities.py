import requests
import os
import time
import json
import copy
import pprint
from datetime import datetime, timezone


current_time = round(time.time()) # seconds
date = datetime.now(timezone.utc).strftime('%Y-%m-%d') # yyyy-mm-dd
print(f"Epoch: {current_time}")
print(f"Date: {date}")

pp = pprint.PrettyPrinter(indent=4)
use_test_data = True
print_fetch_data = False
print_processed_data = True
pretty_print = True
exit_on_fetch_error = True
exit_on_save_error = True
exit_on_report_error = False

rated_token = os.environ.get("RATED_API_KEY")
migalabs_token = os.environ.get("MIGALABS_API_KEY")
google_form_error_report_url = os.environ.get("ERROR_REPORT_ENDPOINT")

# enter values for local testing
# rated_token = ""
# google_form_error_report_url = ""


def fetch_json(url, method="GET", payload={}, headers={}, retries=2):
  print(f"Fetch: {url}")
  response = {"status": 0, "attempts": 0, "data": None}
  try: 
    while response["attempts"] <= retries and (response["status"] != 200 or response["data"] == None):
      rate_limited_domains = ["rated.network"]
      rate_limited = any(domain in url for domain in rate_limited_domains)
      if (rate_limited or response["attempts"] > 0):
        time.sleep(1.05)
      response["attempts"] = response["attempts"] + 1
      r = requests.request(method, url, headers=headers, data=payload)
      response = {"status": r.status_code, "attempts": response["attempts"], "data": r.json()}
  except:
    error = f"Fetch failed: {url}"
    report_error(error)
    if exit_on_fetch_error:
      raise SystemExit(error)
    else:
      print(error)
  finally:
    print_data("fetch", response, label=None)
    return response

def save_to_file(rel_path, data):
  if not rel_path.startswith("/"):
    rel_path = "/" + rel_path
    abs_path = os.path.dirname(__file__) + rel_path
  # skip file save if using test data
  if use_test_data:
    return
  else:
    todays_data =  {
      "date":date,
      "timestamp":current_time,
      "data":data
    }
    # check if file exists yet
    if os.path.isfile(abs_path):
      try:
        with open(abs_path, 'r') as f:
          all_data = json.load(f)
          # check if there's already data for today
          if date != all_data[-1]['date'] and all_data[-1]['data'] != None:
            # append todays data to historical data and write to file
            all_data.append(todays_data)
            with open(abs_path, 'w') as f:
              json.dump(all_data, f, indent=None, separators=(',', ':'))
            f.close()
            print(f"{rel_path} data has been updated")
          # if the data was null then overwrite it
          elif date == all_data[-1]['date'] and all_data[-1]['data'] == None:
            del all_data[-1]
            # append todays data to historical data and write to file
            all_data.append(todays_data)
            with open(abs_path, 'w') as f:
              json.dump(all_data, f, indent=None, separators=(',', ':'))
            f.close()
            print(f"{rel_path} data has been updated")
          else:
            print(f"{rel_path} data for the current date was already recorded")
      except:
        # file is empty or malformed data
        error = f"ERROR: {rel_path} file read error"
        report_error(error)
        if exit_on_save_error:
          raise SystemExit(error)
        else:
          print(error)
    else:
      # create new file with today's data
      all_data = []
      all_data.append(todays_data)
      with open(abs_path, 'w') as f:
        json.dump(all_data, f, indent=None, separators=(',', ':'))
      f.close()
      print(f"{rel_path} data has been updated")

def report_error(error, context=""):
  if use_test_data:
    return
  else:
    data = {
      # "entry.2112281434": "name",    # text
      # "entry.1600556346": "option3", # dropdown
      # "entry.819260047": ["option2", "option3"], #checkbox multiple
      # "entry.1682233942": "option5"  # checkbox single
      "entry.76518486": error,
      "entry.943255668": context
    }
    try:
      requests.post(google_form_error_report_url, data)
      print("Error submitted")
    except:
      error = f"ERROR: {path} file read error"
      if exit_on_report_error:
        raise SystemExit(error)
      else:
        print(error)


def print_file(rel_path):
  # add leading / to relative path if not present
  if not rel_path.startswith("/"):
    rel_path = "/" + rel_path
  abs_path = os.path.dirname(__file__) + rel_path
  if os.path.isfile(abs_path):
    with open(abs_path, 'r') as f:
      contents = json.load(f)
      if pretty_print:
        pprint(contents)
      else:
        print(contents)
  else:
    print("not file")

def print_data(context, data, label=None):
  if context == "fetch" and print_fetch_data:
    if label:
      print(f"{label}:")
    if pretty_print:
      pp.pprint(data)
    else:
      print(data)
  if context == "processed" and print_processed_data:
    if label:
      print(f"{label}:")
    if pretty_print:
      pp.pprint(data)
    else:
      print(data)

def pprint(data):
  pp.pprint(data)
