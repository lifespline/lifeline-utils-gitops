import os


def delete(group, exercise):
    """Delete a group exercise.

    Args:
        groups ([type]): [description]
    """
    exercise_dir = f"praxis_{group}/{exercise}/"
    os.system(
        f"""
        # delete exercise directory
        rm -rf {exercise_dir}

        # delete exercise import
        sed -i '/from praxis_{group}.{exercise} import praxis/d' praxis_{group}/praxis.py

        # sort group imports
        isort praxis_{group}/praxis.py

        # commit group exercise deletion to repo
        git add {exercise_dir} praxis_{group}/praxis.py
        git commit -m \"praxis: delete '{group}.{exercise}'\"
    """
    )

