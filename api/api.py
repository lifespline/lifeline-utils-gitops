import argparse
from asset.description import description
from api.list import list
from api.new import new
from api.delete import delete
from api.practice import practice
from api.rename import rename

def _api():
    """The API contract.
    
    Defines the API endpoints.

    Returns:
        [type]: [description]
    """
    api = argparse.ArgumentParser(description=description)

    # see api.list.list
    help = """
    List exercise groups: -l <group-1> [<group-2> ... <group-N>]
    """
    api.add_argument(
        "-l", "--list",
        help=help,
        nargs='*',
        type=str
    )

    # see api.practice.practice
    help = """
    Practice a full group exercises: -p <group>
    Practice a group exercise: -p <group> <exercise>
    """
    api.add_argument(
        "-p", "--practice",
        help=help,
        type=str,
        nargs='+'
    )

    # see api.score.score
    help = """
    Score an exercise : -s <group> <exercise> <score=[0-5]>
    """
    api.add_argument(
        "-s", "--score",
        help=help,
        type=str,
        nargs=3
    )
    
    # see api.new.new
    help = """
    Add a new exercise: -n <group> <exercise>
    """
    api.add_argument(
        "-n", "--new",
        help=help,
        type=str,
        nargs=2
    )

    # see api.rename.rename
    help = """
    Rename an existing exercise: -r <group> <exercise> <renamed-exercise>
    Rename an existing group: -r <group> <renamed-group>
    """
    api.add_argument(
        "-r", "--rename",
        help=help,
        type=str,
        nargs=3
    )
    
    # see api.delete.delete
    help = """
    Delete an existing exercise: -d <group> <exercise>
    Delete an existing group: -d <group>
    """
    api.add_argument(
        "-d", "--delete",
        help=help,
        type=str,
        nargs=2
    )

    return api


def handle_request():
    """Handle a request to the API

    Returns:
        [type]: [description]
    """
    api = _api()

    request = api.parse_args()

    list_request = request.list
    new_request = request.new
    rename_request = request.rename
    del_request = request.delete
    practice_request = request.practice

    # praxis --list
    if list_request is not None:
        groups = list_request
        list(groups)

    # praxis --new
    elif new_request:
        group, exercise = new_request
        new(group, exercise)

    # praxis --rename
    elif rename_request:
        group, exercise, exercise_new = rename_request
        rename(group, exercise, exercise_new)

    # praxis --delete
    elif del_request:
        group, exercise = del_request
        delete(group, exercise)

    # praxis --practice
    elif practice_request:
        group = None
        exercise = None

        if len(practice_request) == 1:
            group = practice_request[0]
        else:
            group, exercise = practice_request

        practice(group, exercise)

    return request
