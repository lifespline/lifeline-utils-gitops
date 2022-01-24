"""[summary]."""
from util.log import log
from util.utils import (
    get_exercise_mods,
    get_exercise_name,
    print_br
)
import sys
import subprocess
from asset.description import (
    exit_description,
    score_description,
    no_score_desc
)
from util.log_colour import LogColour as lc

def _show_solution(problem_stat):
    """Show the solution of the problem statement. If the solution is inline, it will be displayed in the terminal, a new vscode window will open up otherwise, with the directory containing the solution src.

    Args:
        problem_stat ([type]): [description]
    """
    prob_sol = problem_stat['solution']['content']
    prob_sol_type = problem_stat['solution']['type']

    if prob_sol_type == 'inline':
        log(prob_sol)

    elif prob_sol_type == 'file':
        subprocess.run(["code", prob_sol])

    elif prob_sol_type == 'dir':
        subprocess.run(["code", "-n", prob_sol])

def _open_group_dir(group):
    """Open the directory with the solution to the group exercises.

    Args:
        problem_stat ([type]): [description]
    """
    path = f'/home/dipm/src/lifeline-praxis/praxis_{group}'
    subprocess.run(["code", "-n", path])

def _update_score(group, score):
    """Update the group score.
    """
    log(lc.get_code(1,31) + no_score_desc + lc.get_code(0,0,0))

def _input_score(group):
    """Request user score for the exercise group. If the user input is 'skip', 
    the score won't be affected.

    Args:
        group (`str`): Exercise group.
    """
    log(score_description)
    score = input()

    if score and score.lower() != 'skip': 
        _update_score(group, score)
    else:
        log(lc.get_code(1,31) + no_score_desc + lc.get_code(0,0,0))

def _exit_practice(group, score='skip'):
    """Exit the group practice, either scoring or nor scoring the exercise 
    group.

    Args:
        group ([type]): [description]
        score (str, optional): [description]. Defaults to 'skip'.
    """
    _input_score(group)
    sys.exit(0)

def _show_problem_statement(problem_stat):
    """[summary]

    Args:
        problem_stat ([type]): [description]
    """
    prob_stat = problem_stat['problem_statement']['content']
    prob_stat_type = problem_stat['problem_statement']['type']

    if prob_stat_type == 'inline':
        log(lc.get_code(1,32) + prob_stat + lc.get_code(0,0,0))
    elif prob_stat_type == 'file':
        subprocess.run(["code", prob_stat])
    elif prob_stat_type == 'dir':
        subprocess.run(["code", prob_stat])

    log(exit_description)
    ans = input()

    return ans

def practice(group, exercise):
    """List all exercises in groups.

    Creates a file with the result, and reads that file with columns.
    This solution is much too slow.

    Args:
        groups ([type]): [description]
    """
    exercises = get_exercise_mods(group)[group]
    for exe in exercises:
        if not exercise or get_exercise_name(exe) == exercise:

            print()
            for problem_stat in exe.problem_statements:
                
                ans = _show_problem_statement(problem_stat)

                if ans == 'e':
                    _exit_practice(group)

                elif ans == 's':
                    _show_solution(problem_stat)

                elif ans == 'o':
                    _open_group_dir(group)

                elif ans == 'k':
                    # skip the current group exercise
                    continue

            _input_score(group)
