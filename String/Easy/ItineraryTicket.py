"""
     * <pre>
     * !Walking Rebot:
     *
     * Instructions:Implement the walk method. this method takes in a string path
     * where each character in the string corresponds to a potential movements of the robot.
     * the robot can move up, down, left and right represented by the character 'U','D','L' and 'R' respectively.
     * All other character may be ignored.
     *
     * Assume the robot's initial position is at (0,0).
     * The output of this method is the robot's final x and y coordinates relative
     * to the initial position.
     *
     * !Approach:
     * Step1: Initialize the robot's position at (0, 0)
     * Step2: alternate over each character in the path
     * Step3: Move up, Move Down, Move left, Move right
     * Step4: Ignore other character
     * </pre>
"""

from typing import Dict, Optional


def get_source(ticket_map: Dict[str, str]) -> Optional[str]:
    rev_map = {v: k for k, v in ticket_map.items()}
    for key in ticket_map:
        if key not in rev_map:
            return key
    return None


def itinerary(tickets: Dict[str, str]) -> None:
    source = get_source(tickets)
    while source in tickets:
        print(f"Source: {source} -> ", end="")
        source = tickets[source]
    print(f"Destination: {source}")


if __name__ == "__main__":
    tickets = {
        "Chennai": "Bengaluru",
        "Mumbai": "Delhi",
        "Goa": "Chennai",
        "Delhi": "Goa"
    }
    itinerary(tickets)
