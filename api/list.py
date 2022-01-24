"""[summary]."""
from util.log import log
from util.utils import (
    get_exercise_mods,
    get_exercise_name,
    exec
)
from subprocess import check_output, STDOUT
import csv
from util.log_colour import LogColour

# It is required to import the praxis modules/exercises, so that listing the 
# exercises, filters the praxis modules from the system modules.
import util.imports

def list(groups):
    """List all exercises in groups.

    Creates a file with the result, and reads that file with columns.
    This solution is much too slow.

    Args:
        groups ([type]): [description]
    """
    mods = get_exercise_mods(*groups)

    # header
    header = [
        'TECH',
        'EXERCISE',
        'DESCRIPTION',
        'SCORE',
        'QUESTIONS',
        'SOLUTION (ctrl + click)',
        'STATUS',
    ]

    # body
    body = {}

    for field in header:
        body[field] = []

    for mod in mods:
        for exe in mods[mod]:

            body['TECH'].append(mod)
            exe_name = get_exercise_name(exe)
            body['EXERCISE'].append(exe_name)
            body['DESCRIPTION'].append(exe.description)
            body['SCORE'].append(exe.score)
            body['QUESTIONS'].append(len(exe.problem_statements))
            solution = exe.__file__[0:-len('praxis.py')]
            body['SOLUTION (ctrl + click)'].append(solution + 'solution')

            # exercise readiness
            todo_cnt = f"cat {solution}/solution/* | grep TODO | wc -l"
            res = check_output(todo_cnt, stderr=STDOUT, shell=True)
            todo_cnt = int(res.decode('utf-8').strip() )
            if todo_cnt > 0:
                body['STATUS'].append('TODO')
            else:
                body['STATUS'].append('OK')

    # write the table as csv
    colour_header = header.copy()
    colour_header = [LogColour.get_code(1,32,40)] + colour_header
    colour_header.append(LogColour.get_code(0,0,0))

    output_path = 'asset/exercise_list.csv'
    output = open(output_path, 'w')
    csv_writer = csv.writer(output)
    csv_writer.writerow(colour_header)

    col_count = len(header)
    row_count = len(body[header[0]])

    for r in range(0, row_count):
        row = [LogColour.get_code(1,30,47)]
        for c in range(0, col_count):
            cell = body[header[c]][r]
            row.append(cell)
        row.append(LogColour.get_code(0,0,0))
        csv_writer.writerow(row)

    output.close()

    res = exec(f"column -t -s',' {output_path}" )
    print('')
    log(res)
    print('')
