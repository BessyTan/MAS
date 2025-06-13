from crewai import Task

class EthicalAITasks:
    @staticmethod
    def create_research_task(agent):
        return Task(
            description="""Gather comprehensive and up-to-date information on key ethical considerations 
            related to AI in content creation. Focus on topics such as:
            - Bias in AI content generation (algorithmic, data, representational)
            - Plagiarism and copyright challenges
            - Authenticity and transparency
            - Disclosure (e.g., deepfakes)
            - Job displacement
            - Data privacy
            
            For each point, provide at least one specific real-world example or recent case study from 
            reputable sources. Output must be a structured markdown list with clear sub-headings and 
            cited sources where applicable.""",
            expected_output="""A detailed summary of ethical concerns, including relevant examples and 
            data points, organized by category, with sources.""",
            agent=agent
        )

    @staticmethod
    def create_outline_task(agent, research_task):
        return Task(
            description="""Based on the provided research, create a detailed blog post outline for a 
            target audience of marketing professionals and AI enthusiasts. The outline should include:
            - A compelling title
            - A strong introduction (hook, thesis)
            - 3-4 main body sections addressing specific ethical issues
            - A dedicated section on potential solutions/best practices
            - A powerful conclusion with a call to reflection or action
            
            Define the desired tone as informative, slightly cautionary, and forward-looking.""",
            expected_output="""A structured blog post outline with headings, subheadings, and brief 
            descriptions of content for each section, along with tone guidelines.""",
            agent=agent,
            context=[research_task]
        )

    @staticmethod
    def create_drafting_task(agent, outline_task, research_task):
        return Task(
            description="""Write a comprehensive and engaging blog post (1000-1500 words) strictly 
            following the provided outline and incorporating the research findings. Ensure:
            - Balanced perspective
            - Clear arguments
            - Compelling language
            - Natural integration of specific examples and data points
            - Maintenance of the specified informative, slightly cautionary, and forward-looking tone""",
            expected_output="A first draft of the blog post, ready for editorial review.",
            agent=agent,
            context=[outline_task, research_task]
        )

    @staticmethod
    def create_editing_task(agent, drafting_task):
        return Task(
            description="""Review and meticulously refine the drafted blog post for:
            - Clarity and grammar
            - Spelling and punctuation
            - Overall flow and coherence
            - Well-supported arguments
            - Objective and comprehensive presentation of ethical considerations
            - Elimination of repetitive phrasing
            - Impact and readability improvements
            - Strong and impactful conclusion
            - Robust ethical arguments""",
            expected_output="A polished, final version of the blog post, ready for publication.",
            agent=agent,
            context=[drafting_task]
        ) 