import pandas as pd 
import os, sys
from setting.global_dirs import *
from setting.variables_config import *
from scripts.analysis.functions_for_visualization import *

def load_drps_full_df(data_version: str)->pd.DataFrame:
    data_version_dic = data_version
    schoolurl_ls = os.listdir(data_version_dic)
    schoolname_ls = [schoolurl_dic['_'.join(i.split('_')[1:]).replace('.csv', '')] for i in schoolurl_ls]

    # initial dic - full database containing all three schools
    school_dic = {}
    df_ls = []
    for school, schoolid in zip(schoolurl_ls, schoolname_ls):
        df = pd.read_csv(os.path.join(data_version_dic, school), usecols=lambda column : column != 'Unnamed: 0')
        df["School"] = schoolid
        school_dic[schoolid] = df.copy()
        df_ls.append(school_dic[schoolid])
    full_df = pd.concat(df_ls, axis=0, ignore_index=True)
    col_order = ["YEAR", "School", "Course title", "Summary", "Course description", "Learning Outcomes", "Graduate Attributes and Skills", "Keywords", "URL"]
    full_df = full_df[col_order]
    return full_df

def get_number_of_courses_per_school(df: pd.DataFrame)->dict:
    school_count = df.groupby("School")["Course title"].count().reset_index()
    school_count = {
        "School of Education and Sport": int(school_count[school_count["School"] == "School of Education and Sport"]["Course title"].values[0]),
                    "School of Health in Social Science": int(school_count[school_count["School"] == "School of Health in Social Science"]["Course title"].values[0]),
                    "School of Informatics": int(school_count[school_count["School"] == "School of Informatics"]["Course title"].values[0])}
    return school_count


def plot_pie_percentage_course_have_accessibility(title: str, percentage: float, labels: list, figure_size=(6.4, 3.2)):
    sizes = [int(percentage*100), 100-int(percentage*100)]
    explode = (0.1, 0)
    
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    ax.set_title(title)
    plt.show()
    return fig

def plot_histogram_times_of_accessibility_info(title: str, rt_words_times: dict, figure_size=(6.4, 3.2)):
    keys = list(rt_words_times.keys())
    values = list(rt_words_times.values())
    plt.bar(keys, values, edgecolor='black')
    plt.xlabel('Keywords')
    plt.ylabel('Counts')
    plt.title(title)
    plt.xticks(rotation=90)
    plt.show()
    
## get percentage of courses in each school that have infromation of accessibility
def get_num_courses_in_schools_have_accessibility_info(df: pd.DataFrame, info_cols: list, school: str):
    df_school = df[df["School"]==school]
    sum_of_info = df_school[info_cols].replace({'o': '0'}, regex=True).to_numpy().astype(int).sum(axis=1)
    num_greater_than_zero = sum_of_info[sum_of_info>0].shape[0]
    return num_greater_than_zero

def get_times_of_accessibility_info_in_schools(df: pd.DataFrame, info_cols: list, school: str, keywords_list: list):
    df_school = df[df["School"]==school]
    info_by_school = df_school[info_cols]
    rt_word_times = {}
    for keyword in keywords_list:
        times = 0
        for col in info_cols:
            pattern = re.compile(rf'\b\w*{keyword}\w*\b', flags=re.IGNORECASE)
            temp_list = info_by_school[col].to_list()
            for text in temp_list:
                total_matches = len(pattern.findall(text))
                times += total_matches
        rt_word_times[keyword] = times
    return rt_word_times