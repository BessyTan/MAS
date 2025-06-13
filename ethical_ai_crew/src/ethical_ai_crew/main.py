#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv

from datetime import datetime

from ethical_ai_crew.crew import EthicalAICrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def ensure_output_directory():
    """Create the output directory if it doesn't exist."""
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def save_blog_post(content):
    """Save the generated blog post to a markdown file."""
    output_path = os.path.join("output", "ethical_ai_content_blog_post.md")
    with open(output_path, "w", encoding="utf-8") as f:
        # Access the output attribute of CrewOutput
        if hasattr(content, 'output'):
            f.write(content.output)
        else:
            f.write(str(content))
    print(f"\nBlog post saved to: {output_path}")

def run():
    """
    Run the crew with default settings.
    This is the entry point for the run_crew command.
    """
    main()

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for required API keys
    required_keys = ["OPENAI_API_KEY", "SERPER_API_KEY"]
    missing_keys = [key for key in required_keys if not os.getenv(key)]
    
    if missing_keys:
        print(f"Error: Missing required API keys: {', '.join(missing_keys)}")
        print("Please ensure these keys are set in your .env file")
        return
    
    try:
        # Create output directory
        ensure_output_directory()
        
        # Initialize and run the crew
        print("Initializing Ethical AI Crew...")
        crew = EthicalAICrew().create_crew()
        
        print("\nStarting the content creation process...")
        result = crew.kickoff()
        
        # Save the final output
        save_blog_post(result)
        
        print("\nContent creation process completed successfully!")
        
    except Exception as e:
        print(f"\nError during crew execution: {str(e)}")
        raise

if __name__ == "__main__":
    main()

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        EthicalAICrew().create_crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EthicalAICrew().create_crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        EthicalAICrew().create_crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
