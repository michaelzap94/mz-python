import asyncio
import aioftp
import csv
import gzip
import io

async def get_mp3(host, login, password):
    async with aioftp.Client.context(host, user=login, password=password) as client:
        files = await client.list(recursive=True)
        for e in files:
            print(e)
            #print(path, info)
            # if info["type"] == "file" and path.suffix == ".mp3":
            #     await client.download(path)

async def get_mp3(host, login, password):
    #paths = ['45540_3688113_mp.txt.gz', '44888_3688113_mp.txt.gz', '44940_3688113_mp.txt.gz', '44406_3688113_mp.txt.gz', '45294_3688113_mp.txt.gz', '42694_3688113_mp.txt.gz', '44604_3688113_mp.txt.gz', '44287_3688113_mp.txt.gz', '45095_3688113_mp.txt.gz', '41230_3688113_mp.txt.gz', '45079_3688113_mp.txt.gz', '44656_3688113_mp.txt.gz', '40662_3688113_mp.txt.gz', '44038_3688113_mp.txt.gz', '43650_3688113_mp.txt.gz', '41896_3688113_mp.txt.gz', '43256_3688113_mp.txt.gz', '45046_3688113_mp.txt.gz', '44736_3688113_mp.txt.gz', '42574_3688113_mp.txt.gz', '44748_3688113_mp.txt.gz', '44434_3688113_mp.txt.gz', '39514_3688113_mp.txt.gz', '44131_3688113_mp.txt.gz', '44707_3688113_mp.txt.gz', '41001_3688113_mp.txt.gz', '42811_3688113_mp.txt.gz', '44328_3688113_mp.txt.gz', '40678_3688113_mp.txt.gz', '45125_3688113_mp.txt.gz', '44224_3688113_mp.txt.gz', '39393_3688113_mp.txt.gz', '41663_3688113_mp.txt.gz', '44350_3688113_mp.txt.gz', '44424_3688113_mp.txt.gz', '42254_3688113_mp.txt.gz', '39395_3688113_mp.txt.gz', '39754_3688113_mp.txt.gz', '41491_3688113_mp.txt.gz', '43412_3688113_mp.txt.gz', '45233_3688113_mp.txt.gz', '38401_3688113_mp.txt.gz', '44374_3688113_mp.txt.gz', '43145_3688113_mp.txt.gz', '44148_3688113_mp.txt.gz', '39135_3688113_mp.txt.gz', '41584_3688113_mp.txt.gz', '45502_3688113_mp.txt.gz', '44414_3688113_mp.txt.gz', '44750_3688113_mp.txt.gz', '43126_3688113_mp.txt.gz', '37024_3688113_mp.txt.gz', '44622_3688113_mp.txt.gz', '41462_3688113_mp.txt.gz', '35151_3688113_mp.txt.gz', '45164_3688113_mp.txt.gz', '36756_3688113_mp.txt.gz', '43078_3688113_mp.txt.gz', '39802_3688113_mp.txt.gz', '44958_3688113_mp.txt.gz', '40454_3688113_mp.txt.gz', '39023_3688113_mp.txt.gz', '42957_3688113_mp.txt.gz', '43224_3688113_mp.txt.gz', '43813_3688113_mp.txt.gz', '42246_3688113_mp.txt.gz', '45374_3688113_mp.txt.gz', '35205_3688113_mp.txt.gz', '45244_3688113_mp.txt.gz', '44300_3688113_mp.txt.gz', '36997_3688113_mp.txt.gz', '44185_3688113_mp.txt.gz', '45956_3688113_mp.txt.gz']

    async with aioftp.Client.context(host, user=login, password=password) as client:
        # for path in paths:
        #     await client.download(path)
        await client.download('45540_3688113_mp.txt.gz')
        with gzip.open('45540_3688113_mp.txt.gz', "rt") as f:
            # reader = csv.DictReader(
            #             io.TextIOWrapper(f, encoding="utf-8-sig"),
            #             delimiter="|",
            #         )

            # for feed in reader:
            #     print(feed)

            feed_reader = csv.reader(  # feed is without headers
                f, dialect="feed_dialect", quoting=csv.QUOTE_MINIMAL
            )

            for row in feed_reader:
                print(row)
