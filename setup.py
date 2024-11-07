from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    description="A simple math quiz game from Homework 2 of Data Science for Survival Skills ",
    author="Maria del Mar Moreno",
    author_email="mar.moreno@alumnos.upm.es",
    packages=find_packages(),
    install_requires=[
        # dependencies from requirements.txt
    ],
    entry_points={
        "console_scripts": [
            "math_quiz=math_quiz.math_quiz:math_quiz_game", 
        ],
    },
    
)
