DRPS_keys_of_interest = {
    "Course Outline": ["Summary", "Course description"],
    #"Course Delivery Information": ["Feedback"],
    "Learning Outcomes": ["Learning Outcomes"],
    "Additional Information": ["Graduate Attributes and Skills", "Keywords"]
}

DRPS_values_of_interest = []
for key_i in DRPS_keys_of_interest.keys():
    for v_i in DRPS_keys_of_interest[key_i]:
        DRPS_values_of_interest.append(v_i)

schoolurl_dic = {
    "cx_s_su747.htm": "School of Informatics",
    "cx_s_su819.htm": "School of Education and Sport",
    "cx_s_su796.htm": "School of Health in Social Science"
}

sub_urls_of_school = {
    "cx_s_su747.htm": ['cx_sb_epcc.htm', 'cx_sb_epcd.htm', 'cx_sb_infd.htm', 'cx_sb_infr.htm'],
    "cx_s_su819.htm": ['cx_sb_edua.htm', 'cx_sb_redu.htm', 'cx_sb_sprt.htm'],
    "cx_s_su796.htm": ['cx_sb_clps.htm', 'cx_sb_cnst.htm', 'cx_sb_issh.htm', 'cx_sb_nust.htm', 'cx_sb_shss.htm']
}

positive_accessibility_words = [
    "inclusive", "equitable", "universal", "user-friendly", "adaptable", 
    "assistive", "affordable", "efficient", "accommodating", "empowering",
    "barrier-free", "accessible", "comprehensive", "flexible", "supportive",
    "usable", "welcoming", "enhanced", "reachable", "convenient", 
    "open", "connected", "engaging", "enabling", "progressive", "Web Content Accessibility guidelines", "WCAG",
    "PSBAR", "access", "accessibility"
]

negative_accessibility_words = [
    "inaccessible", "exclusive", "limited", "complicated", "expensive", 
    "difficult", "barrier", "restrictive", "challenging", "problematic",
    "unaccommodating", "inefficient", "isolating", "segregated", "obsolete",
    "unreachable", "demanding", "outdated", "burdensome", "unfriendly",
    "discriminatory", "hindered", "nonfunctional", "alienating", "prohibitive"
]

neutral_accessibility_words = ["design", "disabled", "impairement"]

Accessibility_List = positive_accessibility_words + negative_accessibility_words + neutral_accessibility_words

Chatbot_accessibility_words_ls = ["Accessibility", "Inclusive design", "Disability rights", "Adaptive tools"]
Chatbot_accessibility_words = ','.join(Chatbot_accessibility_words_ls)