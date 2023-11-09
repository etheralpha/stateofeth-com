import sys
sys.path.append("..")
import utilities

def get_migalabs_marketshare_data():
  if utilities.use_test_data:
    response = {'status': 200, 'attempts': 1, 'data': [{"timestamp":"2023-10-03T04:37:09Z","data":[{"client_name":"lighthouse","node_count":2867},{"client_name":"prysm","node_count":2206},{"client_name":"teku","node_count":1303},{"client_name":"nimbus","node_count":836},{"client_name":"lodestar","node_count":252},{"client_name":"grandine","node_count":213},{"client_name":"unknown","node_count":28}]}]}
    # utilities.print_data("fetch", response)
    return response
  else:
    print("AAAAAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    # url = "https://monitoreth.io/data-api/api/eth/v1/nodes/consensus/validators/client_diversity"
    # payload = {}
    # headers = {
    #   'X-Api-Key': utilities.migalabs_token
    # }
    # response = fetch_json(url, "GET", payload, headers)
    # return response

def process_migalabs_marketshare_data(raw_data):
  # example migalabs raw data:
    # raw_data = {'status': 200, 'attempts': 1, 'data': [{
    #   "timestamp": "2023-10-03T04:37:09Z",
    #   "data": [
    #     {
    #       "client_name": "lighthouse",
    #       "node_count": 2867
    #     },
    #     {
    #       "client_name": "prysm",
    #       "node_count": 2206
    #     },
    #     {
    #       "client_name": "teku",
    #       "node_count": 1303
    #     },
    #     {
    #       "client_name": "nimbus",
    #       "node_count": 836
    #     },
    #     {
    #       "client_name": "lodestar",
    #       "node_count": 252
    #     },
    #     {
    #       "client_name": "grandine",
    #       "node_count": 213
    #     },
    #     {
    #       "client_name": "unknown",
    #       "node_count": 28
    #     }
    #   ]
    # }]}

  main_clients = ["lighthouse", "nimbus", "teku", "prysm", "lodestar", "erigon", "grandine"]
  threshold_percentage = 0.5 # represented as a percent, not a decimal
  sample_size = 0
  reformatted_data = []
  filtered_data = [{"name": "other", "value": 0}]
  marketshare_data = []
  extra_data = {}
  final_data = {}

  # reformat data into a list of dicts
  for item in raw_data["data"][0]["data"]:
    reformatted_data.append({"name": item["client_name"].lower(), "value": item["node_count"]})
    sample_size += item["node_count"]
  # utilities.pprint(["reformatted_data", reformatted_data])
  # utilities.pprint(["sample_size", sample_size])

  # filter out items either under the threshold and not in the main_clients list
  for item in reformatted_data:
    if item["name"] in main_clients:
      filtered_data.append({"name": item["name"], "value": item["value"]})
    elif (item["value"] / sample_size * 100) >= threshold_percentage:
      filtered_data.append({"name": item["name"], "value": item["value"]})
    else:
      filtered_data[0]["value"] += item["value"]
  # utilities.pprint(["filtered_data", filtered_data])

  # calculate the marketshare for each client
  for item in filtered_data:
    marketshare = item["value"] / sample_size
    marketshare_data.append({"name": item["name"], "value": marketshare, "accuracy": "no data"})
  # utilities.pprint(["marketshare_data", marketshare_data])

  # sort the list by marketshare descending
  sorted_data = sorted(marketshare_data, key=lambda k : k['value'], reverse=True)
  # utilities.pprint(["sorted_data", sorted_data])

  # supplemental data
  extra_data["data_source"] = "migalabs"
  extra_data["has_majority"] = False
  extra_data["has_supermajority"] = False
  extra_data["danger_client"] = ""
  if sorted_data[0]["value"] >= .50:
    extra_data["has_majority"] = True
    extra_data["danger_client"] = sorted_data[0]["name"]
  if sorted_data[0]["value"] >= .66:
    extra_data["has_supermajority"] = True
  extra_data["top_client"] = sorted_data[0]["name"]
  # pprint(["extra_data", extra_data])

  # create final data dict
  final_data["distribution"] = sorted_data
  final_data["other"] = extra_data
  utilities.print_data("processed", final_data, "final_data_migalabs")

  return final_data

def migalabs_marketshare():
  raw_data = get_migalabs_marketshare_data()
  utilities.save_to_file("../_data/raw/migalabs_raw.json", raw_data["data"])
  processed_data = process_migalabs_marketshare_data(raw_data)
  utilities.save_to_file("../_data/migalabs.json", processed_data)
