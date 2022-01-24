import os

def rename(group, exercise, exercise_new):
    """Rename a group exercise.

    Args:
        group ([type]): [description]
        exercise ([type]): [description]
    """
    exercise_dir_old = f"praxis_{group}/{exercise}/"
    exercise_dir_new = f"praxis_{group}/{exercise_new}/"

    import_old = f"praxis_{group}.{exercise} "
    import_new = f"praxis_{group}.{exercise_new} "
    os.system(
        f"""
        # rename exercise directory
        mv {exercise_dir_old} {exercise_dir_new}

        # fix import name
        sed -i 's/{import_old}/{import_new}/g' praxis_{group}/praxis.py

        # commit changes to repo
        git add {exercise_dir_old} {exercise_dir_new} {exercise_dir_new}praxis.py
        git commit -m \"praxis: rename '{group}.{exercise}' to '{group}.{exercise_new}'\"
    """
    )
