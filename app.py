import sys;
import json;
# Check 
# 23-24
from crawler.community.bitcointalk import bitcointalk;

configpath = "./bitcointalk-config.json";

crawler = None;

with open(configpath, "r") as configfile:
    config = json.loads(configfile.read());

    print("community : " + config["community"]);
    if (config["community"] == "bitcointalk"):
        crawler = bitcointalk();
    else:
        print("There is no crawler");

    if (crawler == None):
        sys.exit();

    if ("pages" in config):
        print(
            "start crawling pages : " + str(config["pages"]["startpage"]) + " to : " + str(config["pages"]["endpage"]));
        crawler.crawlingPages(int(config["pages"]["startpage"]), int(config["pages"]["endpage"]));

    if ("page" in config):
        print("start crawling page : " + str(config["page"]["pageno"]));
        crawler.crawlingPage(int(config["page"]["pageno"]));
