# Extract key and print it .
# raw_log = "tenant_id:auth_01; status:success; runtime_ms:45; user_id:102"
# req = ["tenant_id", "status"]

def PrintRawLogs(logs):
    new_dict1 = []
    new_dict = logs.split(";");

    for i in new_dict:
        new_dict1.append(i.split(":")[0].strip())

    return new_dict1

raw_log = "tenant_id:auth_01; status:success; runtime_ms:45; user_id:102"
print(PrintRawLogs(raw_log))