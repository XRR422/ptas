import pandas as pd

# Data for Graduate Mindsets
mindsets_data = {
    "Mindset Category": [
        "Enquiry and Lifelong Learning",
        "Aspiration and Personal Development",
        "Outlook and Engagement"
    ],
    "Mindsets Description": [
        "This mindset focuses on the proactive approach of students toward learning and knowledge, supported by both faculty and the students' initiative.",
        "Mindsets here evolve over time, shaped by individual values and attitudes towards personal goals and development.",
        "This mindset concerns the engagement with communities and the world, evolving with experiences and individual values."
    ],
    "Reflection Questions": [
        "- What is your current mindset in this area?\n- Are these attitudes well-established or still evolving?\n- How important is this area to you?\n- What impact does this mindset have on your actions and behavior?\n- What experiences have contributed to developing your mindset?\n- What experiences will help further explore, refine, and strengthen your mindset?",
        "- What is your current mindset in this area?\n- Are these attitudes well-established or still evolving?\n- How important is this area to you?\n- What impact does this mindset have on your actions and behavior?\n- What experiences have contributed to developing your mindset?\n- What experiences will help further explore, refine, and strengthen your mindset?",
        "- What is your current mindset in this area?\n- Are these attitudes well-established or still evolving?\n- How important is this area to you?\n- What impact does this mindset have on your actions and behavior?\n- What experiences have contributed to developing your mindset?\n- What experiences will help further explore, refine, and strengthen your mindset?"
    ]
}

# Data for Graduate Skills
skills_data = {
    "Skill Category": [
        "Research and Enquiry", "Research and Enquiry", "Research and Enquiry", "Research and Enquiry",
        "Research and Enquiry", "Research and Enquiry", "Research and Enquiry", "Research and Enquiry",
        "Personal and Intellectual Autonomy", "Personal and Intellectual Autonomy", "Personal and Intellectual Autonomy",
        "Personal and Intellectual Autonomy", "Personal and Intellectual Autonomy", "Personal Effectiveness", "Personal Effectiveness",
        "Personal Effectiveness", "Personal Effectiveness", "Personal Effectiveness", "Personal Effectiveness",
        "Personal Effectiveness", "Personal Effectiveness", "Communication", "Communication", "Communication",
        "Communication", "Communication", "Communication"
    ],
    "Skill Subcategory": [
        "Problem Solving", "Analytical Thinking", "Critical Thinking", "Knowledge Integration and Application",
        "Independent Research", "Handling Complexity and Ambiguity", "Digital Literacy", "Numeracy",
        "Ethics and Social Responsibility", "Self-awareness and Reflection", "Independent Learning and Development",
        "Creativity and Inventive Thinking", "Decision Making", "Leadership", "Planning, Organising and Time Management",
        "Commercial / Professional / Situational Awareness", "Team Working", "Assertiveness and Confidence",
        "Change Management", "Enterprise and Entrepreneurship", "Flexibility", "Interpersonal Skills",
        "Verbal Communication and Presentation", "Cross-cultural Communication", "Written Communications",
        "Influencing and Negotiation Skills", "Social Media"
    ],
    "Key Aspects": [
        "Create, identify, and evaluate options to solve complex problems. Analyse facts and situations, apply creative thinking to develop solutions, and ask questions.",
        "Analyse, synthesise, critically and methodically appraise thoughts to break down complex problems into manageable components.",
        "Capability to evaluate information thoroughly; identify assumptions, detect false logic or reasoning, and define terms accurately to make an informed judgement.",
        "Use information and knowledge effectively to abstract meaning from information and share knowledge across fields, including quantitative skills.",
        "Conduct research and enquiry into issues through research design, collection and analysis of data, and synthesis and reporting.",
        "Understand contextually relevant ethics and values, self-awareness, mental flexibility and openness, resilience, and a commitment to lifelong learning.",
        "Basic scientific, economic, and technological literacies, familiarity with ICT literacy/data and information management, and IT skills.",
        "Manipulate numbers, general mathematical awareness, and application in practical contexts like measuring and estimating. Proficiency with numbers and measures.",
        "Develop awareness of ethical dimensions and responsibilities, recognize and address ethical dilemmas and social responsibility issues.",
        "Be critically self-aware, self-reflective and self-manage to maximize potential, develop resilience, and learn from setbacks.",
        "Importance of lifelong learning skills, think independently, exercise judgment, and adapt to changing environments.",
        "Manage creative processes, think outside the box, adapt, and manage complexity and self-direction.",
        "Make, implement, and review decisions based on facts, situations, and creative thinking. Collaborate and debate to strengthen one's views.",
        "Select appropriate leadership styles, set objectives, motivate, monitor performance, coach and mentor. Work effectively across cultures.",
        "Use project and time management tools, prioritize, plan, and use resources effectively. Resilience and recovery from setbacks.",
        "Understand business landscapes, work collaboratively, build relationships, innovate, and take calculated risks.",
        "Perform effectively in teams, recognize and utilize individuals' different skills, persuade, negotiate, and influence others.",
        "Direct tasks and people confidently, lead and follow appropriately, use judgment to question others when necessary.",
        "Responsive to changes, manage and initiate change effectively, manage projects, and communicate persuasively.",
        "Demonstrate innovation, creativity, collaboration, and risk-taking in commercial, professional, or situational contexts.",
        "Adapt emotions, thoughts, and behaviors to diverse, uncertain, or unfamiliar environments.",
        "Use appropriate communication styles, understand others' needs, deal effectively with conflict.",
        "Develop oral communication of complex ideas and arguments, enhance verbal skills including listening and questioning.",
        "Sensitive to diversity, operate globally, thrive in a globalised society with awareness of other cultures.",
        "Communicate complex ideas in writing using various media, produce clear, structured written work.",
        "Negotiate, persuade, influence, build and maintain relationships, develop emotional intelligence and empathy.",
        "Understand social media forms, communicate effectively through them, manage digital footprint, and promote oneself effectively."
    ]
}

# Creating DataFrames
df_mindsets = pd.DataFrame(mindsets_data)
df_skills = pd.DataFrame(skills_data)

# Saving to Excel
mindsets_path = "./data_container/UOE_Graduate_Attributes_25_01_11/Graduate_Mindsets.xlsx"
skills_path = "./data_container/UOE_Graduate_Attributes_25_01_11/Graduate_Skills.xlsx"


df_mindsets.to_excel(mindsets_path, index=False, sheet_name='GraduateMindsets')

df_skills.to_excel(skills_path, index=False, sheet_name='GraduateSkills')