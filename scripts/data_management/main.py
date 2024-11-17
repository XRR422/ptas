import os, sys
sys.path.append(os.getcwd())
from scripts.data_management.fetch_site_content import *
from setting.global_dirs import *
from setting.variables_config import *

import datetime
import logging
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%y_%m_%d_%H_%M_%S')
YEARS = ["24-25"]
SCHOOL_CODES = sub_urls_of_school.keys()

def fetch_sites_match_any_keywords():
    local_cw = Accessibility_List.copy()
    for YEAR in YEARS:
        for SCHOOL_CODE in SCHOOL_CODES:
            for keyword in local_cw:
                ls_suburl_of_school = sub_urls_of_school[SCHOOL_CODE]
                base_url = f"http://www.drps.ed.ac.uk/{YEAR}/dpt/"
                DIR_DATACONTAINER_WITH_DATE = os.path.join(DIR_DATACONTAINER, formatted_time)
                if not os.path.exists(DIR_DATACONTAINER_WITH_DATE):
                    os.mkdir(DIR_DATACONTAINER_WITH_DATE)
                filename = os.path.join(DIR_DATACONTAINER_WITH_DATE, f"{YEAR}_{SCHOOL_CODE}_keyword-{keyword}.csv")
                log_filename = f"{DIR_MININGLOG}/crawlLogger_{formatted_time}.log"
                logger = logging.getLogger('crawlLogger')
                logger.setLevel(logging.INFO)
                file_handler = logging.FileHandler(log_filename, mode='w')
                formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
                logger.info("Logger configured. Record to mine sites match with any of keywords.")
                logger.info(f"{filename} created.")
                for suburl in ls_suburl_of_school:
                    start_url = f"{base_url}{suburl}"
                    url_filter = suburl.replace('_sb_', '').replace('.htm', '')
                    # Create the csv file
                    df = pd.DataFrame(columns=['URL', 'Sentence', 'Keyword'])
                    df.to_csv(filename)
                    # Start the crawling process and save results
                    crawl_searcher = crawl_class(logger=logger, csvfilename=filename)
                    finish_or_not = crawl_searcher.crawl_and_search(base_url, start_url, keyword, url_filter)
                    
                    if finish_or_not["status"]:
                        logger.info(f"Mining for keywords {keyword} is {finish_or_not['comment']}.")
                    else:
                        logger.info(f"Mining for keywords {keyword} is unsuccess. The last url attempted to access is {finish_or_not['last_visit']}. Reason: {finish_or_not['comment']}")

def fetch_sites_relevant_to_keywords():
    local_kw = Chatbot_accessibility_words
    for YEAR in YEARS:
        for SCHOOL_CODE in SCHOOL_CODES:
            ls_suburl_of_school = sub_urls_of_school[SCHOOL_CODE]
            base_url = f"http://www.drps.ed.ac.uk/{YEAR}/dpt/"
            DIR_DATACONTAINER_WITH_DATE = os.path.join(DIR_DATACONTAINER, formatted_time)
            if not os.path.exists(DIR_DATACONTAINER_WITH_DATE):
                os.mkdir(DIR_DATACONTAINER_WITH_DATE)
            filename = os.path.join(DIR_DATACONTAINER_WITH_DATE, f"{YEAR}_{SCHOOL_CODE}.csv")
            log_filename = f"{DIR_MININGLOG}/crawlLogger_{formatted_time}.log"
            logger = logging.getLogger('crawlLogger')
            logger.setLevel(logging.INFO)
            file_handler = logging.FileHandler(log_filename, mode='w')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info("Logger configured. Record to mine sites relevant to keywords semantic space.")
            logger.info(f"{filename} created.")
            for suburl in ls_suburl_of_school:
                start_url = f"{base_url}{suburl}"
                url_filter = suburl.replace('_sb_', '').replace('.htm', '')
                # Create the csv file
                df = pd.DataFrame(columns=['URL', 'Sentence', 'Keyword'])
                df.to_csv(filename)
                # Start the crawling process and save results
                crawl_searcher = crawl_class(logger=logger, csvfilename=filename)
                finish_or_not = crawl_searcher.fetch_by_chatgpt(base_url, start_url, local_kw, url_filter)
                
                if finish_or_not["status"]:
                    logger.info(f"Mining for keywords {local_kw} is {finish_or_not['comment']}.")
                else:
                    logger.info(f"Mining for keywords {local_kw} is unsuccess. The last url attempted to access is {finish_or_not['last_visit']}. Reason: {finish_or_not['comment']}")



if __name__ == "__main__":
    fetch_sites_relevant_to_keywords()
    
                    