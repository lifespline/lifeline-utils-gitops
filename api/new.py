import os


def new(group, exercise):
    """Create a new group exercise.

    Args:
        groups ([type]): [description]
    """
    exercise_dir = f"praxis_{group}/{exercise}/"
    score = f"{exercise_dir}/score.json"
    dt_token=["YYYY-MM-DDTHH:MM:SS", "+%Y-%m-%d %H:%M:%S"]
    os.system(
        f"""
        # create exercise directory
        mkdir -p {exercise_dir} {exercise_dir}/solution

        # init group exercise assets (if non-existing)
        cp -n asset/praxis.py {exercise_dir}
        cp -n asset/problem_statements.json {exercise_dir}
        cp -n asset/score.json {exercise_dir}
        cp -n asset/description.json {exercise_dir}
        cp -n asset/.gitignore {exercise_dir}
        cp -n asset/solution.md {exercise_dir}/solution/
        sed -i "s/{dt_token[0]}/$(date '{dt_token[1]}')/" {score}

        # update/create group assets
        echo \"\nfrom praxis_{group}.{exercise} import praxis\n\" >> praxis_{group}/praxis.py
        echo \"\nimport praxis_{group}.praxis\n\" >> util/imports.py

        # each group exercise adds the group to util/import, we need to remove
        # duplicates
        isort util/imports.py

        # commit group exercise to repo
        git add {exercise_dir} praxis_{group}/praxis.py util/imports.py
        git commit -m \"praxis: create '{group}.{exercise}'\"
    """
    )
