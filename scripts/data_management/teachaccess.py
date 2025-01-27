import pandas as pd

# Data for the course
data = [
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Understanding Disability",
        "Submodule Content": "Features five posts by Nim Ralph discussing how disability is understood and its impact on disabled people's experiences, along with the construction of various models of disability.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Models of Disability: Keys to Perspectives",
        "Submodule Content": "Explores different paradigms for defining and framing disability, including how they influence societal and governmental strategies to address the needs of disabled people.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "World Report on Disability",
        "Submodule Content": "A report from the WHO and World Bank contextualising disability in life, health, society, and work. Key chapters include: Disability in different settings, supporting people with disabilities, and strategies for creating accessible environments.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "PWDA Disability Language Guide",
        "Submodule Content": "Video resource discussing how language affects perceptions of people with disabilities, emphasising the harm caused by disrespectful language.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Disability Language Style Guide",
        "Submodule Content": "Developed by the National Centre on Disability and Journalism, this guide highlights the diversity of disability and the importance of language awareness.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Ableism/Language",
        "Submodule Content": "Examines ableism as a systemic issue and highlights ableist language in expressions, colloquialisms, and slang. Includes a list of ableist terms and emphasises the need to eliminate them from vocabulary.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Disability Etiquette – A Starting Guide",
        "Submodule Content": "Overview of the rules of etiquette for interacting with people with various types of disabilities.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Etiquette: Interacting With People With Disabilities",
        "Submodule Content": "Discusses general etiquette for working and interacting with people with disabilities.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 1: Overview of Disability",
        "Module Overview": "Explore concepts of disability, including definitions, types, and models. Gain foundational understanding alongside appropriate language and emerging terminology.",
        "Module Objectives": "Define the term disability. Explain how neurodivergence presents itself in learners and other individuals. Use appropriate disability language to respectfully support learners with disabilities",
        "Submodules": "Neurodiversity and Digital Accessibility",
        "Submodule Content": "Provides definitions of neurodivergence and tools for creating neuroinclusive spaces using digital accessibility. Emphasises supporting diverse thought and individuality while recognising that the strategies may not work for every learner.",
    },
    # Module 2 entries
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "An Introduction to Accessibility",
        "Submodule Content": "Outlines the guiding principles and benefits of accessibility for all types of disabilities.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "What Is Digital Accessibility",
        "Submodule Content": "Video overview of assistive technologies and standards that enhance digital access for the disabled.",
    },
    # More Module 2 and Module 3 entries would follow a similar pattern
]

# Adding remaining entries for Module 2 and Module 3

additional_data = [
    # Module 2 continued
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Accessibility Principles",
        "Submodule Content": "Introduces accessibility requirements for websites, web applications, and other digital tools.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Designing for Accessibility with POUR",
        "Submodule Content": "Video on the POUR principles - Perceivable, Operable, Understandable, Robust.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Web Accessibility Perspectives - Compilation of 10 Topics/Videos",
        "Submodule Content": "Examples of how accessibility benefits everyone across various situations.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Assistive Technologies",
        "Submodule Content": "Video overview of technology aids for visual, hearing, and autism spectrum disabilities.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Designing for Accessibility",
        "Submodule Content": "Dos and don'ts when designing for people with disabilities.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Personas – A Simple Introduction",
        "Submodule Content": "Article on creating user personas based on research to represent user needs and behaviors.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "Book Excerpt: A Web for Everyone",
        "Submodule Content": "Discusses personas in accessibility design, emphasising the importance of direct consultation with disabled persons.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 2: Accessible Design Overview",
        "Module Overview": "Explore key concepts of accessibility and design learning experiences that support learners with disabilities.",
        "Module Objectives": "Define digital accessibility. Apply strategies and tools for accessible design. Use personas to create accessible learning experiences.",
        "Submodules": "How to Create UX Personas",
        "Submodule Content": "Video on basic user research techniques for creating effective personas.",
    },
    # Module 3
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "What Is Universal Design for Learning (UDL)?",
        "Submodule Content": "Video explaining the UDL framework and its core principles.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "About Universal Design for Learning",
        "Submodule Content": "Provides material on UDL principles and their application to create inclusive spaces.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Universal Design for Learning: A Guide for Educators",
        "Submodule Content": "Overview of UDL guidelines and tips for their implementation.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Implementing UDL",
        "Submodule Content": "Guidance on applying UDL in the classroom with real-world examples.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Course Design",
        "Submodule Content": "Applying UDL principles to syllabi, learning goals, assessments, and instructional practices.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Media & Materials",
        "Submodule Content": "Combines UDL principles with technology and digital media to enhance learning environments.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Creating Accessible Learning Environments",
        "Submodule Content": "Key strategies for accessible learning environments including communication and space design.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "What Is Plain Language?",
        "Submodule Content": "Explains the benefits of using clear and simple language to enhance accessibility.",
    },
    {
        "Course": "Introduction to Disability and Accessible Design",
        "Modules": "Module 3: Universal Design Overview",
        "Module Overview": "Learn about universal design and its application in educational contexts through UDL. Incorporate plain language to support all learners.",
        "Module Objectives": "Examine the principles of UDL. Identify UDL principles in instructional practices. Apply plain language in lesson design.",
        "Submodules": "Federal Plain Language Guidelines",
        "Submodule Content": "Official guidelines to promote clear writing under the Plain Writing Act of 2010.",
    },
]

data = data + additional_data

# Create the DataFrame
df = pd.DataFrame(data)

# Save as CSV
file_path = "./data_container/TeachAccess/organised_course_content.csv"
df.to_csv(file_path, index=False)
