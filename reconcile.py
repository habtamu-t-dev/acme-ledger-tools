import configparser


def load_config(path="config.ini"):
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg["acme"]


def reconcile(inbound, outbound):
    return round(sum(inbound) - sum(outbound), 2)


if __name__ == "__main__":
    print("Acme ledger reconcile tool. Provide config.ini to run.")
