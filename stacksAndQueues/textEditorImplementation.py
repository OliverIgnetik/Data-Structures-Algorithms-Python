"""
Implement Text Editor Undo Redo
We aim to implement rudimentary undo & redo.

You will be provided a set of actions to perform. 
Once all actions are performed you will return the current state
the system should be in after all actions in actions are performed.

We will be operating on characters and the "state" of the system will be
a string that we are building.

These are the actions possible:
1. INSERT: Inserts a single character to the end of the string
2. DELETE: Removes the last character in the string
3. UNDO: Reverses the most recent action
4. REDO: Redoes the most recent action undone

Your inputs will only be single characters. There are only 4 input actions as enumerated above.

Example 1:
Input:
INSERT 'a'
INSERT 'b'

Output: "ab"

Example 2:
Input:
INSERT 'a'
INSERT 'b'
UNDO

Output: "a"

Example 3:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO

Output: "ab"

Example 4:
Input:
INSERT 'a'
INSERT 'b'
UNDO
REDO
REDO # Does nothing

Output: "ab"
"""
from enum import Enum


class Solution:
    def performEditorActions(self, actions):
        """
        Interface
        ----
        :type actions: list of list of str
        :rtype: str

        Approach 
        ----
        1. Make use of a stack for both redos and undos

        2. Keep track of history for redos

        3. 
        """

        # It stores the ans string
        progress_string = ''

        # Make a Stack for storing undo and redo operations
        undo_stack = []
        redo_stack = []

        # Iterate through all the actions
        for action in actions:
            action_name = action[0]

            # Clear the redo stack in case of Insert operation
            if action_name == "INSERT":
                string = action[1]

                first_char = ""
                if len(string) > 0:
                    first_char = string[0]

                # update the progress string
                progress_string = self.perform_insert_char(
                    first_char, undo_stack, progress_string)
                # the redo stack is cleared when we insert
                redo_stack.clear()

            # Clear the redo stack in case of Delete operation
            elif action_name == "DELETE":
                progress_string = self.perform_delete_char(
                    undo_stack, progress_string)
                redo_stack.clear()

            # Case for Undo
            elif action_name == "UNDO":
                # Only perform undo if undo stack is not empty
                if len(undo_stack) > 0:

                    undo_action = undo_stack.pop()

                    # Perform action according to action present at top of undo stack
                    if undo_action.action_type == ActionType.INSERT:
                        progress_string = self.perform_insert_char(
                            undo_action.character,
                            redo_stack,
                            progress_string
                        )
                    elif undo_action.action_type == ActionType.DELETE:
                        progress_string = self.perform_delete_char(
                            redo_stack,
                            progress_string
                        )

            # Case for Redo
            elif action_name == "REDO":

                # Only perform redo if redo stack is not empty
                if (len(redo_stack) != 0):
                    redo_action = redo_stack.pop()

                    # Perform action according to action present at top of redo stack
                    if redo_action.action_type == ActionType.INSERT:
                        progress_string = self.perform_insert_char(
                            redo_action.character,
                            undo_stack,
                            progress_string
                        )
                    elif redo_action.action_type == ActionType.DELETE:
                        progress_string = self.perform_delete_char(
                            undo_stack,
                            progress_string
                        )
            # Case of Exception (This wouldn't be there in our test cases)
            else:
                raise Exception("unsupported action type")

        return progress_string

    # Function for inserting character in the ans string
    def perform_insert_char(self, c, dest_stack, progress_string):
        # we invert the operation and push it to the appropriate stack
        """
        1. if we are inserting we push the delete action to the undo stack
        2. if we are redoing an insert we push the delete action to the undo stack
        3. if we are undoing an insert we push the delete action to the redo stack
        """
        opposite_action = Action(ActionType.DELETE)
        dest_stack.append(opposite_action)

        return progress_string + c

    # Function for deleting character in the ans string
    def perform_delete_char(self, dest_stack, progress_string):
        """
        1. if we are deleting we push the insert action to the undo stack
        2. if we are redoing a delete we push the insert action to the undo stack
        3. if we are undoing a delete we push the insert action to the redo stack
        """
        last_char = progress_string[-1:]

        opposite_action = Action(ActionType.INSERT, last_char)
        dest_stack.append(opposite_action)

        return progress_string[:-1]

# Class for action type and action character


class Action:
    def __init__(self, action_type, character=None):
        self.action_type = action_type
        self.character = character

# Enum is an Abstract Data Type


class ActionType(Enum):
    INSERT = 'INSERT'
    DELETE = 'DELETE'
    UNDO = 'UNDO'
    REDO = 'REDO'
