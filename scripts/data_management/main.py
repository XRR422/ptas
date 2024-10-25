import os, sys
sys.path.append(os.getcwd())
from scripts.data_management.fetch_site_content import *
from setting.global_dirs import *

import datetime
import logging
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%y_%m_%d_%H_%M_%S')

if __name__ == "__main__":
    base_url = "http://www.drps.ed.ac.uk/24-25/"
    start_url = base_url
    keyword = "accessibility"
    filename = os.path.join(DIR_DATACONTAINER, f"pages_with_keyword-{keyword}_{formatted_time}.csv")
    
    log_filename = f"{DIR_MININGLOG}/crawlLogger_{formatted_time}.log"
    logger = logging.getLogger('crawlLogger')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_filename, mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.info("Logger configured.")
    
    # Create the csv file
    df = pd.DataFrame(columns=['URL', 'Sentence', 'Keyword'])
    df.to_csv(filename)
    logger.info(f"{filename} created.")
    
    # Start the crawling process and save results
    crawl_searcher = crawl_class(logger=logger, csvfilename=filename)
    finish_or_not = crawl_searcher.crawl_and_search(base_url, start_url, keyword)
    
    if finish_or_not:
        logger.info(f"Mining for keywords{keyword} complete.")
        